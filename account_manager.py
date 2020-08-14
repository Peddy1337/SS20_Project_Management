import json_reader_writer

class AccountManager :
    def __init__(self,file) :
        self.file = file
        self.jsonRW = json_reader_writer.JsonReaderWriter(self.file)

    file = ''
    accountList = {}
    selectedAccount = {}
    accountSelected = False

