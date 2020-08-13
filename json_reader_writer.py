import os
import json

class JsonReaderWriter :
    def __init__(self,file) :
        self.file = file

    def writeAccountToFile(self,name,picturePath,pin,adress) :
        contents = {}
        contents['accounts'] = []
        contents['accounts'].append({
            'name' : name,
            'picture' : picturePath,
            'pin' : pin,
            'adress' : adress
        })
        with open(self.file, 'r+') as outfile :
            if os.path.getsize(self.file) == 0:
                json.dump(contents, outfile, indent=4)
                outfile.close();
            else :
                data = json.load(outfile)
                data['accounts'].extend(contents['accounts'])
                outfile.seek(0)
                json.dump(data, outfile, indent=4)
                outfile.close()
                       
    def readAccountsFromJson(self) :
        with open (self.file) as infile :
            if os.path.getsize(self.file) == 0:
                infile.close()
                return False # return False when the file is empty
            else :
                data = json.load(infile) # return dict when file is not empty
                infile.close()
                return data

    def writeRideToJson(self,name,date,startKm,endKm,drivenKm,typeOfRide,purpose,startTime,endTime,accepted) :
        contents = {}
        contents['rides'] = []
        contents['rides'].append({
            'Name' : name,
            'Datum' : date,
            'Abfangskilometerstand' : startKm,
            'Endkilometerstand' : endKm,
            'gefahrene Kilometer' : drivenKm,
            'Art der Fahrt' : typeOfRide,
            'Zweck der Fahrt' : purpose,
            'Fahrtanfang' : startTime,
            'Fahrtende' : endTime,
            'Bestaetigt' : accepted
        })
        with open(self.file, 'r+') as outfile :
            if os.path.getsize(self.file) == 0:
                outfile.close();
                print('Logbook Header not set\n')
                return False # Logbook Header has to be set before documenting rides
            else :
                data = json.load(outfile)
                data['rides'].extend(contents['rides'])
                outfile.seek(0)
                json.dump(data, outfile, indent=4)
                outfile.close()

    def writeLogbookHeaderToJson(self,startDate,endDate,startKm,endKm,licensePlate) :
        contents = {}
        contents['header'] = []
        contents['header'].append({
            'Anfangsdatum' : startDate,
            'Enddatum' : endDate,
            'Abfangskilometerstand' : startKm,
            'Endkilometerstand' : endKm,
            'KFZ-Kennzeichen' : licensePlate,
        })
        contents['rides'] = []
        with open(self.file, 'a+') as outfile :
            if os.path.getsize(self.file) == 0:
                json.dump(contents, outfile, indent=4)
                outfile.close();
            else :
                print ('Logbook Header already exists\n')
                return False # it is not permitted to change the Logbook Header of an existing Logbook
        
    file = ''


