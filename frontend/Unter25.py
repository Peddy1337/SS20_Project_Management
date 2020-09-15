# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Unter25.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Unter25(object):
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
"    border-width: 1px;\n"
"    border-radius: 15px;}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 70, 800, 140))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.zuruck = QtWidgets.QPushButton(Dialog)
        self.zuruck.setGeometry(QtCore.QRect(10, 370, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zuruck.setFont(font)
        self.zuruck.setObjectName("zuruck")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Fur Fahrer unter 25 gilt kein Versicherungsschutz!!!"))
        self.zuruck.setText(_translate("Dialog", "Zurück"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Unter25()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

