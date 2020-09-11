import os
import backend.route_simulator
import backend.json_reader_writer
import backend.pdf_writer
from datetime import datetime
import threading
import time

class LogbookMonitor :
    def __init__(self,file) :
        self.file = file
        self.pdf_file = file[0:file.rfind('.')+1]+ 'pdf'
        self.name = ''
        self.typeOfRide = ''
        self.purpose = ''
        self.signed = False
        self.date = ''
        self.startKm = ''
        self.endKm = ''
        self.routeKm = ''
        self.sleepTime = 5
        self.rSim = backend.route_simulator.RouteSimulator()
        self.jRW = backend.json_reader_writer.JsonReaderWriter(self.file)
        self.updateThread = threading.Thread(target = self.update , args=())
        self.pdfExporter = backend.pdf_writer.PDFWriter()

    def setDriverName(self, name) :
        self.name = name

    def setTypeOfRide(self,tOR) :
        self.typeOfRide = tOR

    def setPurpose(self, purpose) :
        self.purpose = purpose

    def setSignature(self,signed) :
        self.signed = signed # should be bool

    def updateStartKm(self) :
        self.loadLogbook()
        # startKm needs to be set to the endKm of the last ride
        self.startKm = self.logbook['header'][0]['Endkilometerstand']

    def updateDate(self) :
        self.date = datetime.today().strftime('%d.%m.%Y')

    def getPlace(self, without = None) :
        return self.rSim.randomPlace(without)

    # update routeKm every 5 seconds
    def update(self) :
        while self.rideStarted :
            self.rSim.tlock.acquire()
            self.routeKm = str(self.rSim.routeKm)
            index = self.routeKm.find('.')
            self.routeKm = self.routeKm[0:index+2:]
            self.rSim.tlock.release()
            time.sleep(self.sleepTime)

    # start a new ride
    def newRide(self, place = None) :
        self.rideStarted = True
        self.updateStartKm()
        self.updateDate()
        self.startPlace = place or self.getPlace()
        self.currentRide = {
            'Name' : self.name,
            'Datum' : self.date,
            'Anfangskilometerstand' : self.startKm,
            'Endkilometerstand' : '0',
            'gefahrene Kilometer' : '0',
            'Art der Fahrt' : self.typeOfRide,
            'Zweck der Fahrt' : self.purpose,
            'Fahrtanfang' : self.startPlace,
            'Fahrtende' : '',
            'Bestaetigt' : ''
            }
        self.rSim.startThread()
        self.updateThread.start()

    # calculate endKm from startKm and routeKm
    def calculateKm(self) :
        self.endKm = str(float(self.startKm) +  float(self.routeKm))
        index = self.endKm.find('.')
        self.endKm = self.endKm[0:index+2:]

    # check if signed is set and return the corresponding string
    def applySignature(self) :
        if self.signed :
            return 'Ja'
        else :
            return 'Nein'

    # adjustment stop for endKm
    def adjustEndKm(self,adjustment) :
        # adjustment should be of type float
        self.endKm = str(float(self.endKm)+ adjustment)
        index = self.endKm.find('.')
        self.endKm = self.endKm[0:index+2:]
        self.currentRide['Endkilometerstand'] = self.endKm
        self.routeKm = str(float(self.routeKm)+ adjustment)
        index = self.routeKm.find('.')
        self.routeKm = self.routeKm[0:index+2:]
        self.currentRide['gefahrene Kilometer'] = self.routeKm

    # stop ride and stop both threads
    def endRide(self, place = None) :
        self.rideStarted = False
        self.updateThread.join()
        self.rSim.stopThread()
        self.updateThread = threading.Thread(target = self.update , args=())
        self.calculateKm()
        self.currentRide['Endkilometerstand'] = self.endKm
        self.currentRide['gefahrene Kilometer'] = self.routeKm
        self.currentRide['Fahrtende'] = place or self.getPlace(self.startPlace)

    # document ride to json file
    def documentRide(self) :
        self.currentRide['Bestaetigt'] = self.applySignature()
        self.updateHeader(self.endKm)
        self.jRW.writeRideToJson(self.currentRide['Name'],
                                 self.currentRide['Datum'],
                                 self.currentRide['Anfangskilometerstand'],
                                 self.currentRide['Endkilometerstand'],
                                 self.currentRide['gefahrene Kilometer'],
                                 self.currentRide['Art der Fahrt'],
                                 self.currentRide['Zweck der Fahrt'],
                                 self.currentRide['Fahrtanfang'],
                                 self.currentRide['Fahrtende'],
                                 self.currentRide['Bestaetigt'])

    # load the logbook from json
    def loadLogbook(self) :
        self.logbook = self.jRW.readFromJson()
        if not(self.logbook) :
            self.logbook = {}
            self.logbook['header'] = []
            self.logbook['header'].append({
            'Anfangsdatum' : 'Not initated',
            'Enddatum' : 'Not initated',
            'Anfangskilometerstand' : 'Not initated',
            'Endkilometerstand' : 'Not initated',
            'KFZ-Kennzeichen' : 'Not initated',
            })
            return False
            

    # write logbook header to json file
    def documentHeader(self,hStartKm,hLicensePlate) :
        self.updateDate()
        self.jRW.writeLogbookHeaderToJson(self.date,self.date,hStartKm,hStartKm,hLicensePlate)

    # update the logbook header enddate and endKm
    def updateHeader(self,endKm) :
        self.updateDate()
        self.jRW.updateLogbookHeaderToJson(self.date,endKm)

    # sign ride after documentation
    def signRideAfterwards(self,index) :
        self.jRW.signatureToJsonRide(index)
        self.loadLogbook()

    # check if there are usnigned rides
    def checkUnsignedRides(self) :
        for p in self.logbook['rides'] :
            if p['Bestaetigt'] == 'Nein' :
                return True
        
        return False

    # sign all unsigned rides
    def signAllUnsignedRides(self) :
        for p in self.logbook['rides'] :
            if p['Bestaetigt'] == 'Nein' :
                self.signRideAfterwards(self.logbook['rides'].index(p))
        
        print ('Signing of all rides finished\n')

    # export logbook data to pdf
    def exportToPDF(self, path = os.getcwd() ) :
        self.loadLogbook()
        if not(self.checkUnsignedRides()) :
            file = path + '/'+self.pdf_file
            self.pdfExporter.writeToPDF(file,self.logbook)
        else :
            print ('Some rides havent been signed yet\n')
            return False
            
    file = ''
    logbook = {}
    currentRide = {}
    rideStarted = False
