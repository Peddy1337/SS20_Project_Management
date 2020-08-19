import route_simulator
import json_reader_writer
from datetime import datetime
import threading
import time

class LogbookMonitor :
    def __init__(self,file) :
        self.file = file
        self.name = ''
        self.typeOfRide = ''
        self.purpose = ''
        self.signed = False
        self.date = ''
        self.startKm = ''
        self.endKm = ''
        self.routeKm = ''
        self.sleepTime = 5
        self.rSim = route_simulator.RouteSimulator()
        self.jRW = json_reader_writer.JsonReaderWriter(self.file)
        self.updateThread = threading.Thread(target = self.update , args=()) 

    def setDriverName(self, name) :
        self.name = name

    def setTypeOfRide(self,tOR) :
        self.typeOfRide = tOR

    def setPurpose(self, purpose) :
        self.purpose = purpose

    def setSignature(self,signed) :
        self.signed = signed # should be bool

    def updateDate(self) :
        self.date = datetime.today().strftime('%d.%m.%Y')

    def getTime(self) :
        return datetime.today().strftime('%H:%M:%S')

    def update(self) :
        while self.rideStarted :
            self.rSim.tlock.acquire()
            self.routeKm = str(self.rSim.routeKm())
            self.rSim.tlock.release()
            time.sleep(self.sleepTime)

    def newRide(self) :
        self.rideStarted = True
        self.updateDate()
        self.currentRide = {
            'Name' : self.name,
            'Datum' : self.date,
            'Anfangskilometerstand' : self.startKm,
            'Endkilometerstand' : '0',
            'gefahrene Kilometer' : '0',
            'Art der Fahrt' : self.typeOfRide,
            'Zweck der Fahrt' : self.purpose,
            'Fahrtanfang' : self.getTime(),
            'Fahrtende' : '',
            'Bestaetigt' : ''
            }
        self.rSim.startThread()
        self.updateThread.start()

    def calculateKm(self) :
        self.endKm = str(float(self.startKm) +  float(self.routeKm))

    def applySignature(self) :
        if self.signed :
            return 'Ja'
        else :
            return 'Nein'

    def endRide(self) :
        self.rideStarted = False
        self.updateThread.join()
        self.rSim.stopThread()
        self.calculateKm()
        self.currentRide['Endkilometerstand'] = self.endKm
        self.currentRide['gefahrene Kilometer'] = self.routeKm
        self.currentRide['Fahrtende'] = self.getTime()
        self.currentRide['Bestaetigt'] = self.applySignature()
        self.documentRide()

    def documentRide(self) :
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


    def loadLogbook(self) :
        self.logbook = self.jRW.readFromJson()

    file = ''
    logbook = {}
    currentRide = {}
    rideStarted = False

