# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fahrten-Liste.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Fahrten_Liste(object):
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
"    border-width: 1px;\n"
"    border-radius: 15px;}"
"QLineEdit, QLabel{\n"
"    color: #FFFFCC;}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 808, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.KFZ_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.KFZ_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.KFZ_label.setFont(font)
        self.KFZ_label.setObjectName("KFZ_label")
        self.horizontalLayout.addWidget(self.KFZ_label)
        self.KFZ_feld = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.KFZ_feld.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.KFZ_feld.setFont(font)
        self.KFZ_feld.setObjectName("KFZ_feld")
        self.horizontalLayout.addWidget(self.KFZ_feld)
        spacerItem = QtWidgets.QSpacerItem(40, 20)
        self.horizontalLayout.addItem(spacerItem)
        self.Zeitraum = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Zeitraum.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Zeitraum.setFont(font)
        self.Zeitraum.setObjectName("Zeitraum")
        self.horizontalLayout.addWidget(self.Zeitraum)
        self.Beginn = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Beginn.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Beginn.setFont(font)
        self.Beginn.setObjectName("Beginn")
        self.horizontalLayout.addWidget(self.Beginn)
        self.Bis = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Bis.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Bis.setFont(font)
        self.Bis.setObjectName("Bis")
        self.horizontalLayout.addWidget(self.Bis)
        self.Ende = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ende.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Ende.setFont(font)
        self.Ende.setObjectName("Ende")
        self.horizontalLayout.addWidget(self.Ende)
        spacerItem2 = QtWidgets.QSpacerItem(40, 30)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonPrivat = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonPrivat.setMinimumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonPrivat.setFont(font)
        self.pushButtonPrivat.setObjectName("pushButtonP")
        self.horizontalLayout.addWidget(self.pushButtonPrivat)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 400, 801, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.AnfangsKMStand_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.AnfangsKMStand_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AnfangsKMStand_label.setFont(font)
        self.AnfangsKMStand_label.setObjectName("AnfangsKMStand_label")
        self.horizontalLayout_2.addWidget(self.AnfangsKMStand_label)
        self.AnfangsKMStand_feld = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.AnfangsKMStand_feld.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AnfangsKMStand_feld.setFont(font)
        self.AnfangsKMStand_feld.setObjectName("AnfangsKMStand_feld")
        self.horizontalLayout_2.addWidget(self.AnfangsKMStand_feld)
        self.EndKMStand_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.EndKMStand_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EndKMStand_label.setFont(font)
        self.EndKMStand_label.setObjectName("EndKMStand_label")
        self.horizontalLayout_2.addWidget(self.EndKMStand_label)
        self.EndKMStand_feld = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.EndKMStand_feld.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EndKMStand_feld.setFont(font)
        self.EndKMStand_feld.setObjectName("EndKMStand_feld")
        self.horizontalLayout_2.addWidget(self.EndKMStand_feld)
        self.table = QtWidgets.QTableWidget(parent = Dialog)
        self.table.setGeometry(QtCore.QRect(10, 60, 781, 341))
        self.table.setObjectName("tableArea")
      
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.KFZ_label.setText(_translate("Dialog", "Kennzeichen:"))
        self.KFZ_feld.setText(_translate("Dialog", "WWKA489"))
        self.Zeitraum.setText(_translate("Dialog", "Zeitraum:"))
        self.Beginn.setText(_translate("Dialog", "01.01.2019"))
        self.Bis.setText(_translate("Dialog", "bis"))
        self.Ende.setText(_translate("Dialog", "31.12.2019"))
        self.pushButtonPrivat.setText(_translate("Dialog", "Private Fahrten"))
        self.pushButton.setText(_translate("Dialog", "Zurück"))
        self.AnfangsKMStand_label.setText(_translate("Dialog", "Anfangskmstand:"))
        self.AnfangsKMStand_feld.setText(_translate("Dialog", "72.531 km"))
        self.EndKMStand_label.setText(_translate("Dialog", "Endkmstand:"))
        self.EndKMStand_feld.setText(_translate("Dialog", "103.475 km"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Fahrten_Liste()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

