import os
import json

class JsonReaderWriter :
    def __init__(self,file) :
        self.file = file
        crt = open(self.file, "a") # create file if it doesn't exist
        crt.close()

    # adds an account to the accounts list
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

    # overwriting should be used for deleting and editing accounts
    def overwriteAccountList(self,accDict) :
        with open(self.file, 'w+') as outfile :
            json.dump(accDict, outfile, indent=4)
            outfile.close()

    # reads from json file and returns a dict object if possible                   
    def readFromJson(self) :
        with open (self.file) as infile :
            if os.path.getsize(self.file) == 0:
                infile.close()
                return False # return False when the file is empty
            else :
                data = json.load(infile) # return dict when file is not empty
                infile.close()
                return data

    # adds a ride to the logbook if the file is not empty (e.g a header is set) otherwise returns false
    def writeRideToJson(self,name,date,startKm,endKm,drivenKm,typeOfRide,purpose,startTime,endTime,accepted) :
        contents = {}
        contents['rides'] = []
        contents['rides'].append({
            'Name' : name,
            'Datum' : date,
            'Anfangskilometerstand' : startKm,
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

    # adds a header to an empty logbook file. returns false if header is already set
    def writeLogbookHeaderToJson(self,startDate,endDate,startKm,endKm,licensePlate) :
        contents = {}
        contents['header'] = []
        contents['header'].append({
            'Anfangsdatum' : startDate,
            'Enddatum' : endDate,
            'Anfangskilometerstand' : startKm,
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

    # updates enddate and endkm from logbook header
    def updateLogbookHeaderToJson(self,endDate,endKm) :
        contents = self.readFromJson()
        if contents :
            contents['header']['Enddatum'] = endDate
            contents['header']['Endkilometerstand'] = endKm
            with open(self.file, 'w+') as outfile :
                json.dump(contents, outfile, indent=4)
                outfile.close()
        else :
            print('Header couldnt be updated\n')
            return False
               
    file = ''


