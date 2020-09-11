import backend.json_reader_writer

readerAcc = backend.json_reader_writer.JsonReaderWriter('accounts.json')
readerRide = backend.json_reader_writer.JsonReaderWriter('WWP399_2020.json')

readerAcc.writeAccountToFile('Patrick','whatever.png','1234','Neverland')
readerAcc.writeAccountToFile('Bastian','default.png','4321','Somewhere')

data = {}
data['accounts'] = []
data['accounts'].append({
    'name' : 'Accountüberschreiber',
    'picture' : 'bamboozled.png',
    'pin' : '1337',
    'adress' : '....'
    })

readerAcc.overwriteAccountList(data)

data1 = readerAcc.readFromJson()

if data1 :
    for p in data1['accounts']:
            print('Name : ' + p['name'])
            print('Bild : ' + p['picture'])
            print('Pin : ' + p['pin'])
            print('Adresse : ' + p['adress'])
            print('')


readerRide.writeLogbookHeaderToJson('01.01.2020','31.12.2020','110300','125749','WWP399')
readerRide.writeRideToJson('Patrick','02.01.2020','110300','110312','12','geschaeftlich','Kundentermin Firma Bla','11:30:56','13:05:26','Ja')

data2 = readerRide.readFromJson()

if data2 :
    for p in data2['header'] :
        print('Anfangsdatum : ' + p['Anfangsdatum'])
        print('Enddatum : ' + p['Enddatum'])
        print('Anfangskilometerstand : ' + p['Anfangskilometerstand'])
        print('Endkilometerstand : ' + p['Endkilometerstand'])
        print('KFZ-Kennezeichen : ' + p['KFZ-Kennzeichen'])
        print('')
    for d in data2['rides'] :
        print('Name : ' + d['Name'])
        print('Datum : ' + d['Datum'])
        print('Anfangskilometerstand : ' + d['Anfangskilometerstand'])
        print('Endkilometerstand : ' + d['Endkilometerstand'])
        print('gefahrene Kilometer : ' + d['gefahrene Kilometer'])
        print('Art der Fahrt : ' + d['Art der Fahrt'])
        print('Zweck der Fahrt : ' + d['Zweck der Fahrt'])
        print('Fahrtanfang : ' + d['Fahrtanfang'])
        print('Fahrtende : ' + d['Fahrtende'])
        print('Bestaetigt : ' + d['Bestaetigt'])
        print('')
