from account_manager import AccountManager
class LogbookController :
    def __init__(self) :
        self.accountFile = 'accounts.json'
        self.workAdress = 'Remagen, Joseph-Rovan-Allee 6'
        self.licensePlate = LoadLicensePlateFromConfig()
        self.startKm = LoadStartKmFromConfig()
        self.logbookFile = generateLogbookFileName()
        self.accManager = AccountManager(self.accountFile)
        self.lbMonitor = LogbookMonitor(self.logbookFile)
        
    def generateLogbookFileName(self) :
        return self.licensePlate + '_' + self.startKm + '.json'

    def LoadLicensePlateFromConfig() :
        return ''

    def LoadStartKmFromConfig() :
        return ''

    def selectAccount(self,name) :
        self.accManager.selectAccount(name)

    def deselectAccount(self) :
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

