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


    file = ''
    accountList = {}
    selectedAccount = {}
    accountSelected = False

