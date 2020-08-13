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
            else :
                data = json.load(outfile)
                data['accounts'].extend(contents['accounts'])
                outfile.seek(0)
                json.dump(data, outfile, indent=4)
                       
    def readAccountsFromJson(self) :
        with open (self.file) as infile :
            if os.path.getsize(self.file) == 0:
                return False # return False when the file is empty
            else :
                data = json.load(infile) # return dict when file is not empty
                return data
        
    file = ''


