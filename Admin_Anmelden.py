# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Anmelden.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Admin_Anmelden(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: #404040;}\n"
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
"    border-width: 1px;}\n"
"QLabel{\n"
"    color: #FFFFCC;}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(310, 60, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PIN:"))
        self.pushButton.setText(_translate("Dialog", "Zurück"))
        self.pushButton_2.setText(_translate("Dialog", "Bestätigen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Admin_Anmelden()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

