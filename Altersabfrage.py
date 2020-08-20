# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Altersabfrage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import binding
class Altersabfrage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: #404040;\n"
"    color: #FFFFFF}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        self.Frage = QtWidgets.QLabel(Dialog)
        self.Frage.setGeometry(QtCore.QRect(0, 70, 800, 130))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.Frage.setFont(font)
        self.Frage.setAlignment(QtCore.Qt.AlignCenter)
        self.Frage.setWordWrap(True)
        self.Frage.setObjectName("Frage")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(
            lambda: binding.Controlling.altersabfrage_fahrtbeginn(self,Dialog))
        self.pushButton.setGeometry(QtCore.QRect(175, 230, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(
            lambda: binding.Controlling.altersabfrage_unter25(self,Dialog))
        self.pushButton_2.setGeometry(QtCore.QRect(425, 230, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(
            lambda: binding.Controlling.altersabfrage_home(self,Dialog))
        self.pushButton_3.setGeometry(QtCore.QRect(300, 360, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Frage.setText(_translate("Dialog", "Sind Sie mindestens 25 Jahre alt?"))
        self.pushButton.setText(_translate("Dialog", "Ja"))
        self.pushButton_2.setText(_translate("Dialog", "Nein"))
        self.pushButton_3.setText(_translate("Dialog", "Zurück"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Altersabfrage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

