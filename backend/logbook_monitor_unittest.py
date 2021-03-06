import backend.logbook_monitor

import time

logbook = backend.logbook_monitor.LogbookMonitor('test.json')

logbook.updateDate()

print (logbook.date)

logbook.documentHeader('5370.0','WWP399')

logbook.loadLogbook()

print(logbook.logbook)

print ('--------------------------')


logbook.setDriverName('Bastian Spurzem')

logbook.setTypeOfRide('Privat')

logbook.setPurpose('Privat')

logbook.newRide('Koblenz-Güls, Am Zehnthof 11')

time.sleep(11)

logbook.endRide()

logbook.setSignature(False)

logbook.documentRide()

logbook.exportToPDF()

logbook.loadLogbook()

print(logbook.logbook)

print ('--------------------------')


logbook.setDriverName('Patrick Zöller')

logbook.setTypeOfRide('Geschaeftlich')

logbook.setPurpose('Kundentermin Firma RAC')

logbook.newRide()

time.sleep(6)

logbook.endRide()

logbook.adjustEndKm(0.1)

logbook.setSignature(True)

logbook.documentRide()

logbook.loadLogbook()

print(logbook.logbook)

print ('--------------------------')


if logbook.checkUnsignedRides() :
    logbook.signAllUnsignedRides()

logbook.loadLogbook()

print(logbook.logbook)

print ('--------------------------')


logbook.exportToPDF()
