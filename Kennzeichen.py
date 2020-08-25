# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newlicence.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
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
        self.kennzeichen = QtWidgets.QLabel(Dialog)
        self.kennzeichen.setGeometry(QtCore.QRect(170, 30, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.kennzeichen.setFont(font)
        self.kennzeichen.setObjectName("kennzeichen")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(380, 30, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.startkilometerstand = QtWidgets.QLabel(Dialog)
        self.startkilometerstand.setGeometry(QtCore.QRect(170, 80, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.startkilometerstand.setFont(font)
        self.startkilometerstand.setObjectName("startkilometerstand")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 80, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Zuruck"))
        self.pushButton_2.setText(_translate("Dialog", "Bestatigen"))
        self.kennzeichen.setText(_translate("Dialog", "Neues Kennzeichen"))
        self.startkilometerstand.setText(_translate("Dialog", "Startkilometerstand"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

