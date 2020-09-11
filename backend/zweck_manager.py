import backend.json_reader_writer

class ZweckManager :
    def __init__(self,file) :
        self.file = file
        self.jsonRW = backend.json_reader_writer.JsonReaderWriter(self.file)
        self.loadPurposeList()

    #load purpose list from file
    def loadPurposeList(self) :
        self.purposeList = self.jsonRW.readFromJson()
        if self.purposeList :
            if len(self.purposeList) > 20:
                self.purposeList.pop(0)
                self.jsonRW.updatePurposesList(self.purposeList)
        else :
            contents = {}
            contents['purposes'] = []
            self.purposeList = contents

    def addPurpose(self,purpose) :
        self.jsonRW.addPurpose(purpose)
    file = ''
    purposeList = {}
