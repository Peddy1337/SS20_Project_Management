import json_reader_writer

class AccountManager :
    def __init__(self,file) :
        self.file = file
        self.jsonRW = json_reader_writer.JsonReaderWriter(self.file)
        self.loadAccountList()

    # load account list from file
    def loadAccountList(self) :
        self.accountList = self.jsonRW.readFromJson()
        if not(self.accountList) :
            self.accountList = {}
            self.accountList['accounts'] = []

    # add account to file and load new list afterwards
    def addAccount(self,accDetails) :
        self.jsonRW.writeAccountToFile(accDetails['name'],accDetails['picture'],accDetails['pin'],accDetails['adress'])
        self.loadAccountList()

    # edit an account and overwrite file
    def changeAccount(self,targetAccName,accDetails) :
        search = self.searchAccount(targetAccName)
        if type(search) == int :
            self.accountList['accounts'][search] = accDetails
            self.jsonRW.overwriteAccountList(self.accountList)
        else :
            print('Account couldnt be edited')
            return False

    # search account by 'name' attribute index
    def searchAccount(self,targetAccName) :
        for a in self.accountList['accounts'] :
            if a['name'] == targetAccName :
                return self.accountList['accounts'].index(a)
        # if account doesn't exist    
        print('Account not found')
        return False

    # deletes account and overwrite file
    def deleteAccount(self,targetAccName) :
        search = self.searchAccount(targetAccName)
        if type(search) == int :
           del self.accountList['accounts'][search]
           self.jsonRW.overwriteAccountList(self.accountList)
        else :
            print('Account couldnt be deleted')
            return False

    # select account for login return false if account doesn't exists
    def selectAccount(self,targetAccName) :
        search = self.searchAccount(targetAccName)
        if type(search) == int :
            self.accountSelected = True
            self.selectedAccount = self.accountList['accounts'][search]
        else :
            self.deselectAccount()
            print('Account couldnt be selected')
            return False

    # deselect account for logout        
    def deselectAccount(self) :
        self.selectedAccount = {}
        self.accountSelected = False

    # check if pin matches the account pin
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

