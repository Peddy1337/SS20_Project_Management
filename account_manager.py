import json_reader_writer

class AccountManager :
    def __init__(self,file) :
        self.file = file
        self.jsonRW = json_reader_writer.JsonReaderWriter(self.file)
        self.loadAccountList()

    def loadAccountList(self) :
        self.accountList = self.jsonRW.readFromJson()

    def addAccount(self,accDetails) :
        self.jsonRW.writeAccountToFile(accDetails['name'],accDetails['picture'],accDetails['pin'],accDetails['adress'])
        self.loadAccountList()

    def changeAccount(self,targetAccName,accDetails) :
        search = self.searchAccount(targetAccName)
        if search :
            self.accountList['accounts'][search] = accDetails
            self.jsonRW.overwriteAccountList(self.accountList)
        else :
            print('Account couldnt be edited')
            return False

    def searchAccount(self,targetAccName) :
        for a in self.accountList['accounts'] :
            if a['name'] == targetAccName :
                return self.accountList['accounts'].index(a)
        # if account doesn't exist    
        print('Account not found')
        return False

    def deleteAccount(self,targetAccName) :
        search = self.searchAccount(targetAccName)
        if search :
           del self.accountList['accounts'][search]
           self.jsonRW.overwriteAccountList(self.accountList)
        else :
            print('Account couldnt be deleted')
            return False

    def selectAccount(self,targetAccName) :
        search = self.searchAccount(targetAccName)
        if search :
            self.accountSelected = True
            self.selectedAccount = self.accountList['accounts'][search]
        else :
            self.deselectAccount()
            print('Account couldnt be selected')
            return False
        
    def deselectAccount(self) :
        self.selectedAccount = {}
        self.accountSelected = False

    def checkPin(self,inputPin) :
        if self.accountSelected :
            return inputPin == self.selectedAccount['pin']
        else :
            print('No Account selected')
            return False

    file = ''
    accountList = {}
    selectedAccount = {}
    accountSelected = False

