import json_reader_writer

class CarManager :
    def __init__(self,file) :
        self.file = file
        self.jsonRW = json_reader_writer.JsonReaderWriter(self.file)
        self.loadData()

    def loadData(self) :
        self.data = self.jsonRW.readFromJson()

    def saveData(self,licensePlate,startKm)
        self.jsonRW.saveLicensePlateAndStartKm(licensePlate,startKm)

    data = {}
