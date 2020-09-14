import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from frontend.Admin_Anmelden import Admin_Anmelden
from frontend.Altersabfrage import Altersabfrage
from frontend.anmelden import anmelden
from frontend.Fahrt import Fahrt
from frontend.Fahrtbeginn import Fahrtbeginn
from frontend.Fahrtende import Fahrtende
from frontend.Fahrten_Liste import Fahrten_Liste
from frontend.Home import Home
from frontend.Mitarbeiter_anlegen import Mitarbeiter_anlegen
from frontend.Start import Start
from frontend.Unter25 import Unter25
from frontend.Zweck import Zweck
from frontend.adminmenu import adminmenu
from frontend.Mitarbeiter_verwalten import Mitarbeiter_verwalten
from frontend.Profilauswahl import Profilauswahl
from frontend.Kennzeichen import Kennzeichen
from frontend.infoPopup import Popup
from backend.logbook_controller import LogbookController

class Controlling(QtWidgets.QMainWindow):
        
    def __init__(self, parent=None):
        self.backend = LogbookController()
        super(Controlling, self).__init__(parent)

        start = Start()
        start.setupUi(self)
        start.pushButton.clicked.connect(self.auswahl)
        
    #Start
    def start(self):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Start()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.auswahl)
        self.close()

    def checkConfig(self) :
        if self.backend.configured :
            self.anmelden()
        else :
            self.popup = QtWidgets.QWidget()
            self.popup.ui = Popup()
            self.popup.ui.setupUi(self.popup)
            self.popup.ui.label.setText("Konfig nicht gesetzt!\nBitte von einem Admin den\nStartkilometerstand und\ndas Kennzeichen setzten lassen!")
            self.popup.move(290,95)
            self.popup.show()
            
    #Profilauswahl
    def auswahl(self):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Profilauswahl()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(lambda:self.adminanm(1))

        self.backend.accManager.loadAccountList()
        for i in self.backend.accManager.accountList['accounts'] :
            listItem = QtWidgets.QListWidgetItem("name")
            icon = QtGui.QIcon()
            icon.addFile(i['picture'])
            listItem.setIcon(icon)
            listItem.setText(i['name'])
            listItem.setTextAlignment(0x0004)
            listItem.setFont(QtGui.QFont("MS Shell Dlg 2",17))
            window.list.setIconSize(QtCore.QSize(30,30))
            window.list.addItem(listItem)
        window.list.itemSelectionChanged.connect(lambda: self.selectedUser(window))
        self.close()


    #Nutzer wurde ausgewählt
    def selectedUser(self,window):
        accName = window.list.currentItem().text()
        self.backend.selectDriver(accName)
        window.pushButton_2.clicked.connect(self.checkConfig)
        
    #anmelden
    def anmelden(self):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = anmelden()
        window.setupUi(self.window)
        selectedAcc = str(self.backend.accManager.selectedAccount['name'])
        window.lineEdit.setText(selectedAcc)
        window.pushButton.clicked.connect(self.auswahl)
        window.pushButton_2.clicked.connect(lambda: self.verifyPin(window,0))
        pixmap = QtGui.QPixmap(self.backend.accManager.selectedAccount['picture'])
        window.label.setPixmap(pixmap.scaled(161,161))
        self.close()

    def verifyPin(self,window,modus):
        if self.backend.checkPin(window.lineEditPin.text()):
            if modus == 1 :
                self.fahrtenliste(1)
            else :
                self.home()
        
    #adminanmelden
    def adminanm(self,modus):
        self.window = QtWidgets.QDialog()
        window = Admin_Anmelden()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        if modus == 1:
            window.pushButton.clicked.connect(self.auswahl)
            window.pushButton_2.clicked.connect(lambda: self.verifyAdminPin(window,modus))
        elif modus == 2:
            window.pushButton.clicked.connect(self.fahrtenliste)
            window.pushButton_2.clicked.connect(lambda: self.verifyPin(window,1))
        else:
            window.pushButton.clicked.connect(self.home)
            window.pushButton_2.clicked.connect(lambda: self.verifyAdminPin(window,modus))
        self.close()

    def verifyAdminPin(self,window,modus):
        if self.backend.checkAdminPin(window.lineEditPin.text()):
            self.adminmenu(modus)
        
    #home
    def home(self):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Home()
        window.setupUi(self.window)
        selName = str(self.backend.driverInfo['name'])
        selAdress = str(self.backend.driverInfo['adress'])
        window.Daten_Mitarbeiter.setText(selName + "\n" + selAdress)
        pixmap = QtGui.QPixmap(self.backend.driverInfo['picture'])
        window.Profilbild.setPixmap(pixmap.scaled(100,100))
        window.Neue_Fahrt.clicked.connect(self.backend.passDriverName)
        window.Neue_Fahrt.clicked.connect(lambda: self.fahrtbeginn(1))
        window.Angehoriger.clicked.connect(self.altersabfrage)
        window.Buch.clicked.connect(lambda: self.fahrtenliste(0))
        window.comboBox.activated.connect(
            lambda: self.indexChanged(window))
        self.close()

    #Hilfsfunktion combobox
    def indexChanged(self,window):
        index = window.comboBox.currentIndex()
        if  index == 0:
            self.start()
            self.backend.logout()
        elif index == 1:
            self.adminanm(0)

    def export(self) :
        file = QtWidgets.QFileDialog.getExistingDirectory()
        if file != "" :
            if self.backend.exportLogbook(file) :
                self.popup = QtWidgets.QWidget()
                self.popup.ui = Popup()
                self.popup.ui.setupUi(self.popup)
                self.popup.ui.label.setText("Export erfolgreich!")
                self.popup.move(290,95)
                self.popup.show()
            else :
                self.popup = QtWidgets.QWidget()
                self.popup.ui = Popup()
                self.popup.ui.setupUi(self.popup)
                self.popup.ui.label.setText("Export fehlgeschlagen! \nEs wurden noch nicht alle Fahrten bestätigt")
                self.popup.move(290,95)
                self.popup.show()
                
        
    #adminmenu
    def adminmenu(self,modus):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = adminmenu()
        window.setupUi(self.window)
        window.Mitarbeiter_verwalten.clicked.connect(self.mitarbeiter_verwalten)
        window.pushButton_2.clicked.connect(self.kennzeichen)
        window.Daten_auslesen.clicked.connect(self.export)
        if modus == 1:
            window.zuruck.clicked.connect(self.auswahl)
        else:
            window.zuruck.clicked.connect(self.home)
        self.close()

    #altersabfrage
    def altersabfrage(self):
        self.window = QtWidgets.QDialog()
        window = Altersabfrage()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        window.pushButton.clicked.connect(self.backend.passNameFamilyMember)
        window.pushButton.clicked.connect(lambda: self.fahrtbeginn(2))
        window.pushButton_2.clicked.connect(self.unter25)
        window.pushButton_3.clicked.connect(self.home)
        self.close()

    #fahrt
    def fahrt(self):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Fahrt()
        window.setupUi(self.window)
        window.Fahrart_andern.clicked.connect(self.backend.finishRideWithoutSignature)
        window.Fahrart_andern.clicked.connect(lambda: self.fahrtbeginn(0))
        window.Fahrt_beenden.clicked.connect(self.backend.endRide)
        window.Fahrt_beenden.clicked.connect(self.fahrtende)
        window.Name.setText(self.backend.lbMonitor.name)
        window.Art_der_Fahrt.setText(self.backend.lbMonitor.typeOfRide)
        window.Datum_feld.setText(self.backend.lbMonitor.date)
        window.Anfangs_KM_feld.setText(self.backend.lbMonitor.startKm)
        self.close()

    #fahrtbeginn
    def fahrtbeginn(self,back):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Fahrtbeginn()
        window.setupUi(self.window)
        if back == 2:
            window.comboBox.setCurrentIndex(2)
            window.comboBox.setDisabled(True)
        if back == 1 or back == 2:
            window.Zuruck.clicked.connect(self.home)
        elif back == 0:
            window.Zuruck.clicked.connect(self.home)
        window.Bestatigen.clicked.connect(lambda: self.changed(window))
        self.close()

    #Hilfsfunktion combobox 
    def changed(self,window):
        text = window.comboBox.currentText()
        if text == "Dienstlich":
            self.backend.setTypeOfRide(text)
            self.zweck()
        elif text == "Art der Fahrt":
            window.textandern.setHidden(False)
        else:
            self.backend.setTypeOfRide(text)
            self.backend.setPurpose(text)
            self.backend.startRide()
            self.fahrt()

    def createTableItem(self,window) :
        be = QtWidgets.QTableWidgetItem('Ja')
        be.setFlags( QtCore.Qt.NoItemFlags)
        window.table.setItem(window.table.currentRow(),0,be)
    
    #fahrtenliste
    def fahrtenliste(self, modus):
        self.window = QtWidgets.QDialog()
        window = Fahrten_Liste()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        window.pushButton.clicked.connect(self.home)
        window.pushButtonPrivat.clicked.connect(lambda: self.adminanm(2))

        if modus == 1 :
            window.pushButtonPrivat.hide()

        self.backend.lbMonitor.loadLogbook()
        window.table.setRowCount(len(self.backend.lbMonitor.logbook['rides'])+1)
        window.table.setColumnCount(10)
        font = QtGui.QFont()
        font.setPointSize(14)
        h0 = QtWidgets.QTableWidgetItem('Bestätigung')
        h0.setFlags( QtCore.Qt.ItemIsSelectable)
        h0.setFont(font)
        h1 = QtWidgets.QTableWidgetItem('Name')
        h1.setFlags( QtCore.Qt.ItemIsSelectable)
        h1.setFont(font)
        h2 = QtWidgets.QTableWidgetItem('Datum')
        h2.setFlags( QtCore.Qt.ItemIsSelectable)
        h2.setFont(font)
        h3 = QtWidgets.QTableWidgetItem('Anfangskilometerstand')
        h3.setFlags( QtCore.Qt.ItemIsSelectable)
        h3.setFont(font)
        h4 = QtWidgets.QTableWidgetItem('Endkilometerstand')
        h4.setFlags( QtCore.Qt.ItemIsSelectable)
        h4.setFont(font)
        h5 = QtWidgets.QTableWidgetItem('gefahrene Kilometer')
        h5.setFlags( QtCore.Qt.ItemIsSelectable)
        h5.setFont(font)
        h6 = QtWidgets.QTableWidgetItem('Art der Fahrt')
        h6.setFlags( QtCore.Qt.ItemIsSelectable)
        h6.setFont(font)
        h7 = QtWidgets.QTableWidgetItem('Zweck der Fahrt')
        h7.setFlags( QtCore.Qt.ItemIsSelectable)
        h7.setFont(font)
        h8 = QtWidgets.QTableWidgetItem('Fahrtanfang')
        h8.setFlags( QtCore.Qt.ItemIsSelectable)
        h8.setFont(font)
        h9 = QtWidgets.QTableWidgetItem('Fahrtziel')
        h9.setFlags( QtCore.Qt.ItemIsSelectable)
        h9.setFont(font)
        window.table.setItem(0,0,h0)
        window.table.setItem(0,1,h1)
        window.table.setItem(0,2,h2)
        window.table.setItem(0,3,h3)
        window.table.setItem(0,4,h4)
        window.table.setItem(0,5,h5)
        window.table.setItem(0,6,h6)
        window.table.setItem(0,7,h7)
        window.table.setItem(0,8,h8)
        window.table.setItem(0,9,h9)
        index = 0

        for j in self.backend.lbMonitor.logbook['header']:
            window.KFZ_feld.setText(j['KFZ-Kennzeichen'])
            window.Beginn.setText(j['Anfangsdatum'])
            window.Ende.setText(j['Enddatum'])
            window.AnfangsKMStand_feld.setText(j['Anfangskilometerstand'])
            window.EndKMStand_feld.setText(j['Endkilometerstand'])

        self.rideIndex = []
         
        for i in self.backend.lbMonitor.logbook['rides'] :
            if modus == 0 :
                if i['Art der Fahrt'] != 'Privat' :
                    self.rideIndex.append(index)
                    pos = len(self.rideIndex)
                    name = QtWidgets.QTableWidgetItem(i['Name'])
                    name.setFlags( QtCore.Qt.ItemIsSelectable)
                    date = QtWidgets.QTableWidgetItem(i['Datum'])
                    date.setFlags( QtCore.Qt.ItemIsSelectable)
                    skm = QtWidgets.QTableWidgetItem(i['Anfangskilometerstand'])
                    skm.setFlags( QtCore.Qt.ItemIsSelectable)
                    ekm = QtWidgets.QTableWidgetItem(i['Endkilometerstand'])
                    ekm.setFlags( QtCore.Qt.ItemIsSelectable)
                    gkm = QtWidgets.QTableWidgetItem(i['gefahrene Kilometer'])
                    gkm.setFlags( QtCore.Qt.ItemIsSelectable)
                    adf = QtWidgets.QTableWidgetItem(i['Art der Fahrt'])
                    adf.setFlags( QtCore.Qt.ItemIsSelectable)
                    zdf = QtWidgets.QTableWidgetItem(i['Zweck der Fahrt'])
                    zdf.setFlags( QtCore.Qt.ItemIsSelectable)
                    fa = QtWidgets.QTableWidgetItem(i['Fahrtanfang'])
                    fa.setFlags( QtCore.Qt.ItemIsSelectable)
                    fe = QtWidgets.QTableWidgetItem(i['Fahrtende'])
                    fe.setFlags( QtCore.Qt.ItemIsSelectable)
                    window.table.setItem(pos,1,name)
                    window.table.setItem(pos,2,date)
                    window.table.setItem(pos,3,skm)
                    window.table.setItem(pos,4,ekm)
                    window.table.setItem(pos,5,gkm)
                    window.table.setItem(pos,6,adf)
                    window.table.setItem(pos,7,zdf)
                    window.table.setItem(pos,8,fa)
                    window.table.setItem(pos,9,fe)
                    if i['Bestaetigt'] == 'Ja' :
                        be = QtWidgets.QTableWidgetItem(i['Bestaetigt'])
                        be.setFlags( QtCore.Qt.ItemIsSelectable)
                        window.table.setItem(pos,0,be)
                    else :
                        window.listbutton = QtWidgets.QPushButton('bestätigen')
                        window.listbutton.clicked.connect(lambda : self.backend.signRideAfterwards(self.rideIndex[window.table.currentRow()-1]))
                        window.listbutton.clicked.connect(lambda : window.table.removeCellWidget(window.table.currentRow(),0))
                        window.listbutton.clicked.connect(lambda : self.createTableItem(window))
                        window.table.setCellWidget(pos,0,window.listbutton)
            else :
                if i['Art der Fahrt'] != 'Privat' or i['Name'] == self.backend.driverInfo['name'] :
                    self.rideIndex.append(index)
                    pos = len(self.rideIndex)
                    name = QtWidgets.QTableWidgetItem(i['Name'])
                    name.setFlags( QtCore.Qt.ItemIsSelectable)
                    date = QtWidgets.QTableWidgetItem(i['Datum'])
                    date.setFlags( QtCore.Qt.ItemIsSelectable)
                    skm = QtWidgets.QTableWidgetItem(i['Anfangskilometerstand'])
                    skm.setFlags( QtCore.Qt.ItemIsSelectable)
                    ekm = QtWidgets.QTableWidgetItem(i['Endkilometerstand'])
                    ekm.setFlags( QtCore.Qt.ItemIsSelectable)
                    gkm = QtWidgets.QTableWidgetItem(i['gefahrene Kilometer'])
                    gkm.setFlags( QtCore.Qt.ItemIsSelectable)
                    adf = QtWidgets.QTableWidgetItem(i['Art der Fahrt'])
                    adf.setFlags( QtCore.Qt.ItemIsSelectable)
                    zdf = QtWidgets.QTableWidgetItem(i['Zweck der Fahrt'])
                    zdf.setFlags( QtCore.Qt.ItemIsSelectable)
                    fa = QtWidgets.QTableWidgetItem(i['Fahrtanfang'])
                    fa.setFlags( QtCore.Qt.ItemIsSelectable)
                    fe = QtWidgets.QTableWidgetItem(i['Fahrtende'])
                    fe.setFlags( QtCore.Qt.ItemIsSelectable)
                    window.table.setItem(pos,1,name)
                    window.table.setItem(pos,2,date)
                    window.table.setItem(pos,3,skm)
                    window.table.setItem(pos,4,ekm)
                    window.table.setItem(pos,5,gkm)
                    window.table.setItem(pos,6,adf)
                    window.table.setItem(pos,7,zdf)
                    window.table.setItem(pos,8,fa)
                    window.table.setItem(pos,9,fe)
                    if i['Bestaetigt'] == 'Ja' :
                        be = QtWidgets.QTableWidgetItem(i['Bestaetigt'])
                        be.setFlags( QtCore.Qt.ItemIsSelectable)
                        window.table.setItem(pos,0,be)
                    else :
                        window.listbutton = QtWidgets.QPushButton('bestätigen')
                        window.listbutton.clicked.connect(lambda : self.backend.signRideAfterwards(self.rideIndex[window.table.currentRow()-1]))
                        window.listbutton.clicked.connect(lambda : window.table.removeCellWidget(window.table.currentRow(),0))
                        window.listbutton.clicked.connect(lambda : self.createTableItem(window))
                        window.table.setCellWidget(pos,0,window.listbutton)

            index += 1

        window.table.setRowCount(len(self.rideIndex)+1)
        window.table.verticalHeader().hide()
        window.table.horizontalHeader().hide()
        window.table.resizeColumnsToContents()
        self.close()

    #fahrtende
    def fahrtende(self):
        self.window = QtWidgets.QDialog()
        window = Fahrtende()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        window.End_KMStand_feld.setText(self.backend.lbMonitor.endKm)
        window.plus.clicked.connect(self.backend.adjustKmPositive)
        window.plus.clicked.connect(lambda: window.End_KMStand_feld.setText(self.backend.lbMonitor.endKm))
        window.minus.clicked.connect(self.backend.adjustKmNegative)
        window.minus.clicked.connect(lambda: window.End_KMStand_feld.setText(self.backend.lbMonitor.endKm))
        window.pushButton_3.clicked.connect(self.backend.finishRideWithoutSignature)
        window.pushButton_3.clicked.connect(self.home)
        window.pushButton_4.clicked.connect(self.backend.finishRideWithSignature)
        window.pushButton_4.clicked.connect(self.home)
        self.close()

    #kennzeichen
    def kennzeichen(self):
        self.window = QtWidgets.QDialog()
        window = Kennzeichen()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        window.pushButton.clicked.connect(self.adminmenu)
        window.pushButton_2.clicked.connect(lambda: self.backend.writeLicensePlateAndStartKmToConfig(window.lineEdit.text(),window.lineEdit_2.text()))
        window.pushButton_2.clicked.connect(self.adminmenu)
        self.close()

    def changePicture(self,window) :
        fd = QtWidgets.QFileDialog()
        file = fd.getOpenFileName(None,"choose a picture",os.getcwd(),"Images (*.png *.xpm *.jpg)" )[0]
        if file == "" :
            if window.PIC.text() == "" :
                pixmap = QtGui.QPixmap("defaultUser.png")
                window.label.setPixmap(pixmap.scaled(150,150))
        else :    
            window.PIC.setText(file)
            pixmap = QtGui.QPixmap(file)
            window.label.setPixmap(pixmap.scaled(150,150))
        
    
    #mitarbeiter_anlegen
    def mitarbeiter_anlegen(self, account = None):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Mitarbeiter_anlegen()
        window.setupUi(self.window)
        if account :
            window.PIN_feld.setText(account['pin'])
            window.Name.setText(account['name'])
            window.Adresse.setText(account['adress'])
            window.PIC.setText(account['picture'])
            pixmap = QtGui.QPixmap(account['picture'])
            window.label.setPixmap(pixmap.scaled(150,150))
            window.dir_button.clicked.connect(lambda: self.changePicture(window))
            window.pushButton.clicked.connect(self.mitarbeiter_verwalten)
            window.pushButton_2.clicked.connect(lambda :self.backend.editAccount(window.Name.text(),window.PIC.text(),window.PIN_feld.text(),window.Adresse.text()))
            window.pushButton_2.clicked.connect(self.mitarbeiter_verwalten)
        else:
            window.dir_button.clicked.connect(lambda: self.changePicture(window))
            window.pushButton.clicked.connect(self.mitarbeiter_verwalten)
            window.pushButton_2.clicked.connect(lambda :self.backend.addAccount(window.Name.text(),window.PIC.text(),window.PIN_feld.text(),window.Adresse.text()))
            window.pushButton_2.clicked.connect(self.mitarbeiter_verwalten)
        self.close()

    def accountSelection(self,window) :
        if window.list.currentItem() :
            self.mitarbeiter_anlegen(self.backend.accManager.selectedAccount)
        

    def accountDeletion(self,window) :
        if window.list.currentItem() :
            self.backend.deleteAccount(window.list.currentItem().text())
            window.list.takeItem(window.list.row(window.list.currentItem()))


    #mitarbeiter_verwalten
    def mitarbeiter_verwalten(self):
        self.window = QtWidgets.QMainWindow()
        self.window.showFullScreen()
        window = Mitarbeiter_verwalten()
        window.setupUi(self.window)
        window.Zuruck.clicked.connect(lambda :self.adminmenu(1))
        window.Neu.clicked.connect(self.mitarbeiter_anlegen) 
        window.bearbeiten.clicked.connect(lambda : self.accountSelection(window))
        window.loschen.clicked.connect(lambda : self.accountDeletion(window))
        
        self.backend.accManager.loadAccountList()
        for i in self.backend.accManager.accountList['accounts'] :
            listItem = QtWidgets.QListWidgetItem("name")
            icon = QtGui.QIcon()
            icon.addFile(i['picture'])
            listItem.setIcon(icon)
            listItem.setText(i['name'])
            listItem.setTextAlignment(0x0004)
            listItem.setFont(QtGui.QFont("MS Shell Dlg 2",17))
            window.list.setIconSize(QtCore.QSize(30,30))
            window.list.addItem(listItem)
        window.list.itemSelectionChanged.connect(lambda: self.backend.selectAccount(window.list.currentItem().text()))
        self.close()

    #unter25
    def unter25(self):
        self.window = QtWidgets.QDialog()
        window = Unter25()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        window.zuruck.clicked.connect(self.home)
        self.close()

    def zweckSelection(self,window) :
        if window.lineEdit.text() != "Zweck der Fahrt" and window.lineEdit.text() != "" :
            self.backend.addPurposes(window.lineEdit.text())
            self.backend.setPurpose(window.lineEdit.text())
            self.backend.startRide()
            self.fahrt()
        elif len(window.listView.selectedItems()) != 0 :
            self.backend.setPurpose(window.listView.currentItem().text())
            self.backend.startRide()
            self.fahrt()

    #zweck
    def zweck(self):
        self.window = QtWidgets.QDialog()
        window = Zweck()
        window.setupUi(self.window)
        self.window.showFullScreen()
        self.window.resize(800,480)
        
        self.backend.loadPurposes()
        for i in self.backend.purpManager.purposeList['purposes'] :
            listItem = QtWidgets.QListWidgetItem("name")
            listItem.setText(i['Zweck der Fahrt'])
            listItem.setTextAlignment(0x0004)
            listItem.setFont(QtGui.QFont("MS Shell Dlg 2",17))
            window.listView.addItem(listItem)
        window.pushButton.clicked.connect(self.fahrtbeginn)
        window.pushButton_2.clicked.connect(lambda:self.zweckSelection(window))
        self.close()
