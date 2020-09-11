from backend.account_manager import AccountManager
from backend.logbook_monitor import LogbookMonitor
from backend.car_manager import CarManager
from backend.zweck_manager import ZweckManager

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
        self.driverInfo = {}
        
    def generateLogbookFileName(self) :
        return self.licensePlate + '_' + self.startKm + '.json'

    def writeLicensePlateAndStartKmToConfig(self,licenseP, startKm) :
        self.carManager.saveData(licenseP,startKm)
        self.licensePlate = licenseP
        self.startKm = startKm
        self.logbookFile = self.generateLogbookFileName()
        self.lbMonitor = LogbookMonitor(self.logbookFile)
        self.writeHeader()

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

    def selectDriver(self,name) :
        self.selectAccount(name)
        self.driverInfo = self.accManager.selectedAccount

    def logout(self) :
        self.accManager.deselectAccount()
        self.diverInfo = {}

    def checkPin(self,pin) :
        return self.accManager.checkPin(pin)

    def addAccount(self,name,picture,pin,adress) :
        if picture == '':
            picture = 'defaultUser.png'
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
        self.accManager.changeAccount(name,accDetails)

    def deleteAccount(self,name) :
        self.accManager.deleteAccount(name)

    def passDriverName(self) :
        if self.driverInfo and not(self.lbMonitor.rideStarted) :
            self.lbMonitor.setDriverName(self.driverInfo['name'])
        else :
            print('No Account selected or Ride already started\n')

    def setTypeOfRide(self, tOR) :
        if not(self.lbMonitor.rideStarted) :
            self.lbMonitor.setTypeOfRide(tOR)

    def setPurpose(self,purpose) :
        if not(self.lbMonitor.rideStarted) :
            self.lbMonitor.setPurpose(purpose)

    def passNameFamilyMember(self):
        self.lbMonitor.setDriverName(self.driverInfo['name']+ ' Angehörige/r')

    def startRide(self) :
        self.lbMonitor.newRide()

    def endRide(self) :
        if self.lbMonitor.typeOfRide == 'Dienstlich' or self.lbMonitor.typeOfRide == 'Privat' :
            self.lbMonitor.endRide()
        elif self.lbMonitor.typeOfRide == 'nach Hause' :
            self.lbMonitor.endRide(self.driverInfo['adress'])
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

    def exportLogbook(self, path) :
        self.lbMonitor.exportToPDF(path)
        
