import json_reader_writer

class ZweckManager :
    def __init__(self,file) :
        self.file = file
        self.jsonRW = json_reader_writer.JsonReaderWriter(self.file)
        self.loadPurposeList()

    #load purpose list from file
    def loadPurposeList(self) :
        self.purposeList = self.jsonRW.readFromJson()
        if len(purposeList) > 20:
            purposeList.pop(0)
            self.jsonRW.updatePurposesList(self.purposeList)

    def addPurpose(self,purpose) :
        self.jsonRW.addPurpose(purpose)
    file = ''
    purposeList = {}
