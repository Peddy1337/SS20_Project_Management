# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import binding
class adminmenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #404040;\n"
"    color: #00CC00}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Mitarbeiter_verwalten = QtWidgets.QPushButton(self.centralwidget)
        self.Mitarbeiter_verwalten.clicked.connect(
            lambda: binding.Controlling.adminmenu_mitverwalten(self,MainWindow))
        self.Mitarbeiter_verwalten.setGeometry(QtCore.QRect(180, 90, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Mitarbeiter_verwalten.setFont(font)
        self.Mitarbeiter_verwalten.setObjectName("Mitarbeiter_verwalten")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(
            lambda: binding.Controlling.adminmenu_kennzeichen(self,MainWindow))
        self.pushButton_2.setGeometry(QtCore.QRect(430, 90, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Daten_auslesen = QtWidgets.QPushButton(self.centralwidget)
        self.Daten_auslesen.clicked.connect(
            lambda: binding.Controlling.adminmenu_datenauslesen(self,MainWindow))
        self.Daten_auslesen.setGeometry(QtCore.QRect(300, 210, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Daten_auslesen.setFont(font)
        self.Daten_auslesen.setObjectName("Daten_auslesen")
        self.zuruck = QtWidgets.QPushButton(self.centralwidget)
        self.zuruck.clicked.connect(
            lambda: binding.Controlling.adminmenu_home(self,MainWindow))
        self.zuruck.setGeometry(QtCore.QRect(10, 370, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zuruck.setFont(font)
        self.zuruck.setObjectName("zuruck")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Mitarbeiter_verwalten.setText(_translate("MainWindow", "Mitarbeiter \n"
"verwalten"))
        self.pushButton_2.setText(_translate("MainWindow", "Kennzeichen \n"
"ändern"))
        self.Daten_auslesen.setText(_translate("MainWindow", "Daten \n"
"auslesen"))
        self.zuruck.setText(_translate("MainWindow", "Zurück"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = adminmenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

