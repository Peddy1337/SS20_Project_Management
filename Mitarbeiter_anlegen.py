# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mitarbeiter_anlegen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from numblock import Ui_Form as Form
from eigene_Tastatur import Keyboard

class Mitarbeiter_anlegen(object):
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
"    border-width: 1px;}\n"
"QLineEdit,QTextEdit{\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QLabel{\n"
"    color: #FFFFCC;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(17.5, 10, 150, 150))
        self.label.setObjectName("label")
        self.PIC = QtWidgets.QLineEdit(self.centralwidget)
        self.PIC.setGeometry(QtCore.QRect(10, 170, 165, 50))
        self.PIC.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.PIC.setFont(font)
        self.PIC.setObjectName("Name")
        self.dir_button = QtWidgets.QPushButton(self.centralwidget)
        self.dir_button.setGeometry(QtCore.QRect(10, 230, 165, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dir_button.setFont(font)
        self.dir_button.setObjectName("dir_button")
        self.Name = LineEditK(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(190, 0, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.PIN_label = QtWidgets.QLabel(self.centralwidget)
        self.PIN_label.setGeometry(QtCore.QRect(590, 10, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.PIN_label.setFont(font)
        self.PIN_label.setObjectName("PIN_label")
        self.PIN_feld = LineEditN(self.centralwidget)
        self.PIN_feld.setGeometry(QtCore.QRect(590, 50, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.PIN_feld.setFont(font)
        self.PIN_feld.setObjectName("PIN_feld")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Adresse = LineEditK(self.centralwidget)
        self.Adresse.setGeometry(QtCore.QRect(190, 40, 361, 120))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Adresse.setFont(font)
        self.Adresse.setObjectName("Adresse")
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
        self.label.setText(_translate("MainWindow", "Platzhalter\n"
"Profilbild"))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.PIN_label.setText(_translate("MainWindow", "PIN:"))
        self.dir_button.setText(_translate("MainWindow", "Durchsuchen"))
        self.pushButton.setText(_translate("MainWindow", "Zurück"))
        self.pushButton_2.setText(_translate("MainWindow", "speichern"))
        self.Adresse.setText(_translate("MainWindow", "Adresse"))

class LineEditK(QtWidgets.QLineEdit):
    
    def mousePressEvent(self,event):
        if(self.text() == 'Name' or self.text() == 'Adresse') :            
            self.clear()
        
        self.dialog = QtWidgets.QWidget()
        self.dialog.ui = Keyboard()
        self.dialog.ui.setupUi(self.dialog,self.editTextFromSlot, self.deleteCharFromSlot)
        self.dialog.move(self.pos().x(),self.pos().y()+80)
        self.dialog.show()
        super(LineEditK,self).mousePressEvent(event)
        
    def editTextFromSlot(self,text) :
        self.insert(text)

    def deleteCharFromSlot(self) :
        self.backspace()

class LineEditN(QtWidgets.QLineEdit):
    
    def mousePressEvent(self,event):
        if(self.text() == 'Pin') :            
            self.clear()
        
        self.dialog = QtWidgets.QWidget()
        self.dialog.ui = Form()
        self.dialog.ui.setupUi(self.dialog,self.editTextFromSlot,self.deleteCharFromSlot)
        self.dialog.move(self.pos().x(),self.pos().y()+80)
        self.dialog.show()
        super(LineEditN,self).mousePressEvent(event)
        
    def editTextFromSlot(self,button) :
        self.insert(button.text())

    def deleteCharFromSlot(self) :
        self.backspace()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mitarbeiter_anlegen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

