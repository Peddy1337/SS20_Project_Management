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
        self.backend.accManager.selectAccount(accName)
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
        if self.backend.accManager.checkPin(window.lineEdit_2.text()):
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
        window.pushButton_2.clicked.connect(lambda: self.adminmenu(modus))
        self.close()
        self.window.show()

    #home
    def home(self):
        self.window = QtWidgets.QMainWindow()
        window = Home()
        window.setupUi(self.window)
        selName = str(self.backend.accManager.selectedAccount['name'])
        selAdress = str(self.backend.accManager.selectedAccount['adress'])
        window.Daten_Mitarbeiter.setText(selName + "\n" + selAdress)
        pixmap = QtGui.QPixmap(self.backend.accManager.selectedAccount['picture'])
        window.Profilbild.setPixmap(pixmap)
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
        window.Fahrart_andern.clicked.connect(lambda: self.fahrtbeginn(0))
        window.Fahrt_beenden.clicked.connect(self.fahrtende)
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
            window.Bestatigen.clicked.connect(self.fahrt)
        if back == 1 or back == 2:
            window.Zuruck.clicked.connect(self.home)
        elif back == 0:
            window.Zuruck.clicked.connect(self.fahrt)
        window.comboBox.activated.connect(lambda: self.changed(window))
        self.close()
        self.window.show()

    #Hilfsfunktion combobox 
    def changed(self,window):
        text = window.comboBox.currentText()
        if text == "Dienstlich":
            window.Bestatigen.clicked.connect(self.zweck)
        elif text == "Art der Fahrt":
            print("andern")
        else:
            window.Bestatigen.clicked.connect(self.fahrt)

    
    #fahrtenliste
    def fahrtenliste(self):
        self.window = QtWidgets.QDialog()
        window = Fahrten_Liste()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.home)

        #self.backend.logbook_monitor.loadLogbook()
        #for i in self.backend.logbook_monitor.logbook['accounts'] :
        #    listItem = QtWidgets.QListWidgetItem("name")
        #    icon = QtGui.QIcon()
        #    icon.addFile(i['picture'])
        #    listItem.setIcon(icon)
        #    listItem.setText(i['name'])
        #    listItem.setTextAlignment(0x0004)
        #    listItem.setFont(QtGui.QFont("MS Shell Dlg 2",17))
        #    window.list.setIconSize(QtCore.QSize(30,30))
        #    window.list.addItem(listItem)
            
        self.close()
        self.window.show()

    #fahrtende
    def fahrtende(self):
        self.window = QtWidgets.QDialog()
        window = Fahrtende()
        window.setupUi(self.window)
        window.pushButton_3.clicked.connect(self.home)
        window.pushButton_4.clicked.connect(self.home)
        self.close()
        self.window.show()

    #kennzeichen
    def kennzeichen(self):
        self.window = QtWidgets.QDialog()
        window = Kennzeichen()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.adminmenu)
        window.pushButton_2.clicked.connect(self.home)
        self.close()
        self.window.show()

    #mitarbeiter_anlegen
    def mitarbeiter_anlegen(self):
        self.window = QtWidgets.QMainWindow()
        window = Mitarbeiter_anlegen()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.adminmenu)
        window.pushButton_2.clicked.connect(self.adminmenu)#TODO
        self.close()
        self.window.show()

    #mitarbeiter_verwalten
    def mitarbeiter_verwalten(self):
        self.window = QtWidgets.QMainWindow()
        window = Mitarbeiter_verwalten()
        window.setupUi(self.window)
        window.Zuruck.clicked.connect(self.adminmenu)
        window.Neu.clicked.connect(self.mitarbeiter_anlegen)
        window.bearbeiten.clicked.connect(self.mitarbeiter_anlegen)#TODO
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

    #zweck
    def zweck(self):
        self.window = QtWidgets.QDialog()
        window = Zweck()
        window.setupUi(self.window)
        window.pushButton.clicked.connect(self.fahrtbeginn)
        window.pushButton_2.clicked.connect(self.fahrt)
        self.close()
        self.window.show()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gui = Controlling()
    gui.show()
    app.exec_()

    
