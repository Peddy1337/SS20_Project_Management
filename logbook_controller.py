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
