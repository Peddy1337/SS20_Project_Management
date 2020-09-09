# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newlicence.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from numblock import LineEdit as LineEditN
from eigene_Tastatur import LineEdit as LineEditK

class Kennzeichen(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: #404040;\n"
"    color: #FFFFCC}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QLineEdit{\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.neuesKennzeichen = QtWidgets.QLabel(Dialog)
        self.neuesKennzeichen.setGeometry(QtCore.QRect(170, 80, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.neuesKennzeichen.setFont(font)
        self.neuesKennzeichen.setObjectName("neuesKennzeichen")
        self.lineEdit = LineEditK(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(400, 80, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.startkilometerstand = QtWidgets.QLabel(Dialog)
        self.startkilometerstand.setGeometry(QtCore.QRect(170, 130, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.startkilometerstand.setFont(font)
        self.startkilometerstand.setObjectName("startkilometerstand")
        self.lineEdit_2 = LineEditN(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 130, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Zurück"))
        self.pushButton_2.setText(_translate("Dialog", "Bestätigen"))
        self.neuesKennzeichen.setText(_translate("Dialog", "Neues Kennzeichen"))
        self.startkilometerstand.setText(_translate("Dialog", "Startkilometerstand"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Kennzeichen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

