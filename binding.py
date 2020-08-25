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

class Controlling():

    def bind(self,MainWindow,to):
        self.window = QtWidgets.QMainWindow()
        self.ui = to()
        self.ui.setupUi(self.window)
        MainWindow.close()#hide()
        self.window.show()

    def bind_dialog(self,Dialog,to):
        self.window = QtWidgets.QDialog()
        self.ui = to()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def bindfahrtbeginn(self,MainWindow,to):
        self.window = QtWidgets.QMainWindow()
        self.ui = to()
        self.ui.setupUi(self.window,1)
        MainWindow.close()#hide()
        self.window.show()
        
    def start_auswahl(self,MainWindow):
        Controlling.bind(self,MainWindow,Profilauswahl)

    def anmelden_start(self,MainWindow):
        Controlling.bind(self,MainWindow,Start)

    def anmelden_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def home_fahrtbeginn(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrtbeginn)

    def home_altersabfrage(self,MainWindow):
        Controlling.bind(self,MainWindow,Altersabfrage)

    def home_fahrtenliste(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrten_Liste)

    def fahrtbeginn_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def fahrtbeginn_fahrt(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrt)

    def fahrtbeginn_zweck(self,MainWindow):
        Controlling.bind(self,MainWindow,Zweck)

    def altersabfrage_unter25(self,MainWindow):
        Controlling.bind_dialog(self,MainWindow,Unter25)

    def altersabfrage_fahrtbeginn(self,MainWindow):
        Controlling.bindfahrtbeginn(self,MainWindow,Fahrtbeginn)

    def altersabfrage_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def unter25_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def fahrtenliste_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def zweck_fahrtbeginn(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrtbeginn)

    def zweck_fahrt(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrt)

    def fahrt_fahrtbeginn(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrtbeginn)

    def fahrt_fahrtende(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrtende)

    def fahrtende_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def fahrtende_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def home_start(self,MainWindow):
        Controlling.bind(self,MainWindow,Start)

    def home_adminanmelden(self,MainWindow):
        Controlling.bind(self,MainWindow,Admin_Anmelden)

    def home_fahrtenliste(self,MainWindow):
        Controlling.bind(self,MainWindow,Fahrten_Liste)

    def adminanm_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def adminanm_adminmenu(self,MainWindow):
        Controlling.bind(self,MainWindow,adminmenu)

    def adminmenu_mitverwalten(self,MainWindow):
        Controlling.bind(self,MainWindow,Mitarbeiter_verwalten)

    def adminmenu_datenauslesen(self,MainWindow):
        Controlling.bind(self,MainWindow,adminmenu)#Daten

    def adminmenu_kennzeichen(self,MainWindow):
        Controlling.bind(self,MainWindow,Kennzeichen)

    def adminmenu_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

    def mitverw_neu(self,MainWindow):
        Controlling.bind(self,MainWindow,Mitarbeiter_anlegen)

    def mitverw_adminmenu(self,MainWindow):
        Controlling.bind(self,MainWindow,adminmenu)

    def auswahl_adminanmelden(self,MainWindow):
        Controlling.bind(self,MainWindow,Admin_Anmelden)

    def auswahl_anmelden(self,MainWindow):
        Controlling.bind(self,MainWindow,anmelden)

    def kennzeichen_adminmenu(self,MainWindow):
        Controlling.bind(self,MainWindow,adminmenu)

    def kennzeichen_home(self,MainWindow):
        Controlling.bind(self,MainWindow,Home)

        
