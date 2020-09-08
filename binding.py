import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Admin_Anmelden import Admin_Anmelden
from Altersabfrage import Altersabfrage
from anmelden import anmelden
from Fahrt import Fahrt
from Fahrtbeginn import Fahrtbeginn
from Fahrtende import Fahrtende
from Fahrten_Liste import Fahrten_Liste
from Home import Home
from Mitarbeiter_anlegen import Mitarbeiter_anlegen
from Start import Start
from Unter25 import Unter25
from Zweck import Zweck
from adminmenu import adminmenu
from Mitarbeiter_verwalten import Mitarbeiter_verwalten
from Profilauswahl import Profilauswahl
from Kennzeichen import Kennzeichen
from logbook_controller import LogbookController

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
        window = Start()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.auswahl)
        self.close()
        self.window.show()

    #Profilauswahl
    def auswahl(self):
        self.window = QtWidgets.QMainWindow()
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
        self.window.show()

    #Nutzer wurde ausgewählt
    def selectedUser(self,window):
        accName = window.list.currentItem().text()
        self.backend.selectDriver(accName)
        window.pushButton_2.clicked.connect(self.anmelden)
        
    #anmelden
    def anmelden(self):
        self.window = QtWidgets.QMainWindow()
        window = anmelden()
        window.setupUi(self.window)
        selectedAcc = str(self.backend.accManager.selectedAccount['name'])
        window.lineEdit.setText(selectedAcc)
        window.pushButton.clicked.connect(self.auswahl)
        window.pushButton_2.clicked.connect(lambda: self.verifyPin(window))
        pixmap = QtGui.QPixmap(self.backend.accManager.selectedAccount['picture'])
        window.label.setPixmap(pixmap)
        self.close()
        self.window.show()

    def verifyPin(self,window):
        if self.backend.checkPin(window.lineEdit_2.text()):
            self.home()
        
    #adminanmelden
    def adminanm(self,modus):
        self.window = QtWidgets.QDialog()
        window = Admin_Anmelden()
        window.setupUi(self.window)
        if modus == 1:
            window.pushButton.clicked.connect(self.auswahl)
        else:
            window.pushButton.clicked.connect(self.home)
        window.pushButton_2.clicked.connect(lambda: self.verifyAdminPin(window,modus))
        self.close()
        self.window.show()

    def verifyAdminPin(self,window,modus):
        if self.backend.checkAdminPin(window.lineEdit.text()):
            self.adminmenu(modus)
        
    #home
    def home(self):
        self.window = QtWidgets.QMainWindow()
        window = Home()
        window.setupUi(self.window)
        selName = str(self.backend.driverInfo['name'])
        selAdress = str(self.backend.driverInfo['adress'])
        window.Daten_Mitarbeiter.setText(selName + "\n" + selAdress)
        pixmap = QtGui.QPixmap(self.backend.driverInfo['picture'])
        window.Profilbild.setPixmap(pixmap)
        window.Neue_Fahrt.clicked.connect(self.backend.passDriverName)
        window.Neue_Fahrt.clicked.connect(lambda: self.fahrtbeginn(1))
        window.Angehoriger.clicked.connect(self.altersabfrage)
        window.Buch.clicked.connect(self.fahrtenliste)
        window.comboBox.activated.connect(
            lambda: self.indexChanged(window))
        self.close()
        self.window.show()

    #Hilfsfunktion combobox
    def indexChanged(self,window):
        index = window.comboBox.currentIndex()
        if  index == 0:
            self.start()
            self.backend.logout()
        elif index == 1:
            self.adminanm(0)
        
    #adminmenu
    def adminmenu(self,modus):
        self.window = QtWidgets.QMainWindow()
        window = adminmenu()
        window.setupUi(self.window)
        window.Mitarbeiter_verwalten.clicked.connect(self.mitarbeiter_verwalten)
        window.pushButton_2.clicked.connect(self.kennzeichen)
        window.Daten_auslesen.clicked.connect(self.adminmenu)#TODO
        if modus == 1:
            window.zuruck.clicked.connect(self.auswahl)
        else:
            window.zuruck.clicked.connect(self.home)
        self.close()
        self.window.show()

    #altersabfrage
    def altersabfrage(self):
        self.window = QtWidgets.QDialog()
        window = Altersabfrage()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.backend.passNameFamilyMember)
        window.pushButton.clicked.connect(lambda: self.fahrtbeginn(2))
        window.pushButton_2.clicked.connect(self.unter25)
        window.pushButton_3.clicked.connect(self.home)
        self.close()
        self.window.show()

    #fahrt
    def fahrt(self):
        self.window = QtWidgets.QMainWindow()
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
        self.window.show()

    #fahrtbeginn
    def fahrtbeginn(self,back):
        self.window = QtWidgets.QMainWindow()
        window = Fahrtbeginn()
        window.setupUi(self.window)
        if back == 2:
            window.comboBox.setCurrentIndex(2)
            window.comboBox.setDisabled(True)
            window.Bestatigen.clicked.connect(self.backend.startRide)
            window.Bestatigen.clicked.connect(self.fahrt)
        if back == 1 or back == 2:
            window.Zuruck.clicked.connect(self.home)
        elif back == 0:
            window.Zuruck.clicked.connect(self.fahrt)
        window.Bestatigen.clicked.connect(lambda: self.changed(window))
        self.close()
        self.window.show()

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

    
    #fahrtenliste
    def fahrtenliste(self):
        self.window = QtWidgets.QDialog()
        window = Fahrten_Liste()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.home)

        self.backend.lbMonitor.loadLogbook()
        window.table.setRowCount(len(self.backend.lbMonitor.logbook['rides']))
        window.table.setColumnCount(10)
        index = 0

        for j in self.backend.lbMonitor.logbook['header']:
            window.KFZ_feld.setText(j['KFZ-Kennzeichen'])
            window.Beginn.setText(j['Anfangsdatum'])
            window.Ende.setText(j['Enddatum'])
            window.AnfangsKMStand_feld.setText(j['Anfangskilometerstand'])
            window.EndKMStand_feld.setText(j['Endkilometerstand'])
            
        for i in self.backend.lbMonitor.logbook['rides'] :
            window.table.setItem(index,0,QtWidgets.QTableWidgetItem(i['Name']))
            window.table.setItem(index,1,QtWidgets.QTableWidgetItem(i['Datum']))
            window.table.setItem(index,2,QtWidgets.QTableWidgetItem(i['Anfangskilometerstand']))
            window.table.setItem(index,3,QtWidgets.QTableWidgetItem(i['Endkilometerstand']))
            window.table.setItem(index,4,QtWidgets.QTableWidgetItem(i['gefahrene Kilometer']))
            window.table.setItem(index,5,QtWidgets.QTableWidgetItem(i['Art der Fahrt']))
            window.table.setItem(index,6,QtWidgets.QTableWidgetItem(i['Zweck der Fahrt']))
            window.table.setItem(index,7,QtWidgets.QTableWidgetItem(i['Fahrtanfang']))
            window.table.setItem(index,8,QtWidgets.QTableWidgetItem(i['Fahrtende']))
            if i['Bestaetigt'] == 'Ja' :
                window.table.setItem(index,9,QtWidgets.QTableWidgetItem(i['Bestaetigt']))
            else :
                window.listbutton = QtWidgets.QPushButton('bestätigen')
                window.listbutton.setFlat(True)
                window.listbutton.clicked.connect(lambda index : self.backend.signRideAfterwards(index))
                window.listbutton.clicked.connect(lambda index: window.table.removeCellWidget(index,9))
                window.listbutton.clicked.connect(lambda index : window.table.setItem(index,9,QtWidgets.QTableWidgetItem('Ja')))
                window.table.setCellWidget(index,9,window.listbutton)
                
            index += 1
        
        window.table.verticalHeader().hide()
        window.table.horizontalHeader().hide()
        window.table.resizeColumnsToContents()
        self.close()
        self.window.show()

    #fahrtende
    def fahrtende(self):
        self.window = QtWidgets.QDialog()
        window = Fahrtende()
        window.setupUi(self.window)
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
        self.window.show()

    #kennzeichen
    def kennzeichen(self):
        self.window = QtWidgets.QDialog()
        window = Kennzeichen()
        window.setupUi(self.window)   
        window.pushButton.clicked.connect(self.adminmenu)
        window.pushButton_2.clicked.connect(lambda: self.backend.writeLicensePlateAndStartKmToConfig(window.lineEdit.text(),window.lineEdit_2.text()))
        window.pushButton_2.clicked.connect(self.adminmenu)
        self.close()
        self.window.show()

    def changePicture(self,window) :
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        window.PIC.setText(file)
        pixmap = QtGui.QPixmap(file)
        window.label.setPixmap(pixmap.scaled(150,150))
        
    
    #mitarbeiter_anlegen
    def mitarbeiter_anlegen(self, account = None):
        self.window = QtWidgets.QMainWindow()
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
        self.window.show()

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
        self.window.show()

    #unter25
    def unter25(self):
        self.window = QtWidgets.QDialog()
        window = Unter25()
        window.setupUi(self.window)
        window.zuruck.clicked.connect(self.home)
        self.close()
        self.window.show()

    def zweckSelection(self,window) :
        if window.lineEdit.text() != "Zweck der Fahrt" :
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
        self.window.show()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gui = Controlling()
    gui.show()
    app.exec_()

    
