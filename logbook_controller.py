from account_manager import AccountManager
from logbook_monitor import LogbookMonitor
from car_manager import CarManager
from zweck_manager import ZweckManager

class LogbookController :
    def __init__(self) :
        self.accountFile = 'accounts.json'
        self.workAdress = 'Remagen, Joseph-Rovan-Allee 6'
        self.adminPin = '1234'
        self.carFile = 'car.json'
        self.carManager = CarManager(self.carFile)
        self.licensePlate = self.loadLicensePlateFromConfig()
        self.startKm = self.loadStartKmFromConfig()
        self.logbookFile = self.generateLogbookFileName()
        self.accManager = AccountManager(self.accountFile)
        self.lbMonitor = LogbookMonitor(self.logbookFile)
        self.purposeFile = 'purpose.json'
        self.purpManager = ZweckManager(self.purposeFile)
        
    def generateLogbookFileName(self) :
        return self.licensePlate + '_' + self.startKm + '.json'

    def writeLicensePlateAndStartKmToConfig(self,licenseP, startKm) :
        self.carManager.saveData(licenseP,startKm)

    def loadStartKmFromConfig(self) :
        success = self.carManager.loadData()
        if success :
            return self.carManager.data['headerParts'][0]['StartKm']
        else :
            self.writeLicensePlateAndStartKmToConfig('Dummy Value', 'Dummy Value')
            self.carManager.loadData()
            return self.carManager.data['headerParts'][0]['StartKm']

    def loadLicensePlateFromConfig(self) :
        success = self.carManager.loadData()
        if success :
            return self.carManager.data['headerParts'][0]['KFZ-Kennzeichen']
        else :
            self.writeLicensePlateAndStartKmToConfig('Dummy Value', 'Dummy Value')
            self.carManager.loadData()
            return self.carManager.data['headerParts'][0]['KFZ-Kennzeichen']

    def addPurposes(self,purpose) :
        self.purpManager.addPurpose(purpose)

    def loadPurposes(self):
        self.purpManager.loadPurposeList()

    def checkAdminPin(self,pin) :
        return pin == self.adminPin

    def selectAccount(self,name) :
        self.accManager.selectAccount(name)

    def logout(self) :
        self.accManager.deselectAccount()

    def checkPin(self,pin) :
        return self.accManager.checkPin(pin)

    def addAccount(self,name,picture,pin,adress) :
        accDetails ={
            'name' : name,
            'picture' : picture,
            'pin' : pin,
            'adress' : adress
            }
        self.accManager.addAccount(accDetails)

    def editAccount(self,name,picture,pin,adress) :
        accDetails ={
            'name' : name,
            'picture' : picture,
            'pin' : pin,
            'adress' : adress
            }
        self.accManager.changeAccount(accDetails)

    def deleteAccount(self,name) :
        self.accManager.deleteAccount(name)

    def passDriverName(self) :
        if self.accManager.accountSelected and not(self.lbMonitor.rideStarted) :
            self.lbMonitor.setDriverName(self.accManager.selectedAccount['name'])
        else :
            print('No Account selected or Ride already started\n')

    def setTypeOfRide(self, tOR) :
        if not(self.lbMonitor.rideStarted) :
            self.lbMonitor.setTypeOfRide(tOR)

    def setPurpose(self,purpose) :
        if not(self.lbMonitor.rideStarted) :
            self.lbMonitor.setPurpose(purpose)

    def startRideFamilyMember(self):
        self.lbMonitor.setDriverName(self.accManager.selectedAccount['name']+ ' Angehörige/r')
        self.setTypeOfRide('privat')
        self.setPurpose('privat')
        self.startRide()

    def startRide(self) :
        self.lbMonitor.newRide()

    def endRide(self) :
        if self.lbMonitor.typeOfRide == 'geschäftlich' or self.lbMonitor.typeOfRide == 'privat' :
            self.lbMonitor.endRide()
        elif self.lbMonitor.typeOfRide == 'nach Hause' :
            self.lbMonitor.endRide(self.accManager.selectedAccount['adress'])
        elif self.lbMonitor.typeOfRide == 'zur Arbeit' :
            self.lbMonitor.endRide(self.workAdress)
        else :
            print('Type of Ride doesnt match known types\n')

    def adjustKmPositive(self) :
        if not(self.lbMonitor.rideStarted) :
            self.lbMonitor.adjustEndKm(0.1)

    def adjustKmNegative(self) :
        if not(self.lbMonitor.rideStarted) :
            self.lbMonitor.adjustEndKm(-0.1)

    def writeHeader(self) :
        self.lbMonitor.documentHeader(self.startKm, self.licensePlate)

    def finishRideWithSignature(self) :
        self.lbMonitor.setSignature(True)
        self.lbMonitor.documentRide()

    def finishRideWithoutSignature(self) :
        self.lbMonitor.setSignature(False)
        self.lbMonitor.documentRide()

    def signRideAfterwards(self, index) :
        self.lbMonitor.signRideAfterwards(index)

    def checkIfUnsignedRides(self) :
        return self.lbMonitor.checkUnsignedRides()

    def signAllRides(self) :
        self.lbMonitor.signAllUnsignedRides()

    def exportLogbook(self) :
        self.lbMonitor.exportToPDF()
        
