# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zweck.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import binding
class Zweck(object):
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
"QListView{\n"
"    color: #FFFFCC;\n"
"    background-color: #999999;\n"
"    border: none;}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(
            lambda: binding.Controlling.zweck_fahrtbeginn(self,Dialog))
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(
            lambda: binding.Controlling.zweck_fahrt(self,Dialog))
        self.pushButton_2.setGeometry(QtCore.QRect(590, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(270, 30, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(270, 80, 256, 211))
        self.listView.setObjectName("listView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Zurück"))
        self.pushButton_2.setText(_translate("Dialog", "Bestätigen"))
        self.lineEdit.setText(_translate("Dialog", "Zweck der Fahrt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Zweck()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

