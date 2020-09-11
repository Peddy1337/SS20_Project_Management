# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fahrtende.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Fahrtende(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: #404040;\n"
"    color: #00CC00}\n"
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
        self.End_KMStand_label = QtWidgets.QLabel(Dialog)
        self.End_KMStand_label.setGeometry(QtCore.QRect(150, 160, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.End_KMStand_label.setFont(font)
        self.End_KMStand_label.setObjectName("End_KMStand_label")
        self.End_KMStand_feld = QtWidgets.QLineEdit(Dialog)
        self.End_KMStand_feld.setGeometry(QtCore.QRect(150, 210, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.End_KMStand_feld.setFont(font)
        self.End_KMStand_feld.setObjectName("End_KMStand_feld")
        self.plus = QtWidgets.QPushButton(Dialog)
        self.plus.setGeometry(QtCore.QRect(150, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(Dialog)
        self.minus.setGeometry(QtCore.QRect(300, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 10, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 370, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.End_KMStand_label.setText(_translate("Dialog", "End KM-Stand:"))
        self.plus.setText(_translate("Dialog", "+"))
        self.minus.setText(_translate("Dialog", "-"))
        self.pushButton_3.setText(_translate("Dialog", "später\n"
"Bestatigen"))
        self.pushButton_4.setText(_translate("Dialog", "Bestätigen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Fahrtende()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

