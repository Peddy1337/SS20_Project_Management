# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mitarbeiter_verwalten.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Mitarbeiter_verwalten(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #404040;\n"
"    color: #00CC00}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QLineEdit,QLabel{\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Zuruck = QtWidgets.QPushButton(self.centralwidget)
        self.Zuruck.setGeometry(QtCore.QRect(10, 490, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Zuruck.setFont(font)
        self.Zuruck.setObjectName("Zuruck")
        self.bearbeiten = QtWidgets.QPushButton(self.centralwidget)
        #window für bearbeiten
        self.bearbeiten.setGeometry(QtCore.QRect(290, 10, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.bearbeiten.setFont(font)
        self.bearbeiten.setObjectName("bearbeiten")
        self.Neu = QtWidgets.QPushButton(self.centralwidget)
        self.Neu.setGeometry(QtCore.QRect(10, 10, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Neu.setFont(font)
        self.Neu.setObjectName("Neu")
        self.suche = QtWidgets.QLineEdit(self.centralwidget)
        self.suche.setGeometry(QtCore.QRect(590, 10, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.suche.setFont(font)
        self.suche.setObjectName("suche")
        self.loschen = QtWidgets.QPushButton(self.centralwidget)
        #function für löschen
        self.loschen.setGeometry(QtCore.QRect(520, 10, 41, 50))
        self.loschen.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Mulltonne.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.loschen.setIcon(icon)
        self.loschen.setIconSize(QtCore.QSize(50, 50))
        self.loschen.setObjectName("loschen")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 70, 781, 401))
        self.list.setObjectName("listArea")
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
        self.Zuruck.setText(_translate("MainWindow", "Zurück"))
        self.bearbeiten.setText(_translate("MainWindow", "Bearbeiten"))
        self.Neu.setText(_translate("MainWindow", "Neu"))
        self.suche.setText(_translate("MainWindow", "Suche"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mitarbeiter_verwalten()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

