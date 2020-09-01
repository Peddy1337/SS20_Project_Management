# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homedirty.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #404040;\n"
"    color: #FFFFCC}\n"
"QPushButton,QComboBox{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QLabel{\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QComboBox QAbstractItemView{\n"
"    min-width: 200px; }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Neue_Fahrt = QtWidgets.QPushButton(self.centralwidget)
        self.Neue_Fahrt.setGeometry(QtCore.QRect(280, 170, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Neue_Fahrt.setFont(font)
        self.Neue_Fahrt.setObjectName("Neue_Fahrt")
        self.Angehoriger = QtWidgets.QPushButton(self.centralwidget)
        self.Angehoriger.setGeometry(QtCore.QRect(280, 280, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Angehoriger.setFont(font)
        self.Angehoriger.setObjectName("Angehoriger")
        self.Profilbild = QtWidgets.QLabel(self.centralwidget)
        self.Profilbild.setGeometry(QtCore.QRect(20, 10, 100, 100))
        self.Profilbild.setWordWrap(True)
        self.Profilbild.setObjectName("Profilbild")
        self.Daten_Mitarbeiter = QtWidgets.QLabel(self.centralwidget)
        self.Daten_Mitarbeiter.setGeometry(QtCore.QRect(130, 10, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Daten_Mitarbeiter.setFont(font)
        self.Daten_Mitarbeiter.setObjectName("Daten_Mitarbeiter")
        self.Buch = QtWidgets.QPushButton(self.centralwidget)
        self.Buch.setGeometry(QtCore.QRect(730, 10, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Buch.setFont(font)
        self.Buch.setObjectName("Buch")
        self.Buch.setIcon(QtGui.QIcon('Buch.png'))
        self.Buch.setIconSize(QtCore.QSize(60,60))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 10, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("0")
        self.comboBox.addItem("1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 11, 60, 59))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Zahnrad.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.Neue_Fahrt.setText(_translate("MainWindow", "Neue Fahrt"))
        self.Angehoriger.setText(_translate("MainWindow", "Angehöriger"))
        self.Profilbild.setText(_translate("MainWindow", "Platzhalter Profilbild"))
        self.Daten_Mitarbeiter.setText(_translate("MainWindow", "Name\n"
"Adresse"))
        #self.Buch.setText(_translate("MainWindow", "Buch"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Abmelden"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Admin"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

