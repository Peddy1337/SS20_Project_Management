# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fahrtbeginn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Fahrtbeginn(object):

    def setupUi(self, MainWindow, modus=0):
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
"QLabel{\n"
"    color: #FFFFCC;}"
"QLineEdit, QComboBox{\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QComboBox QAbstractItemView{\n"
"    min-width: 200px; }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Zuruck = QtWidgets.QPushButton(self.centralwidget)
        self.Zuruck.setGeometry(QtCore.QRect(10, 370, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Zuruck.setFont(font)
        self.Zuruck.setObjectName("Zuruck")
        self.Bestatigen = QtWidgets.QPushButton(self.centralwidget)
        self.Bestatigen.setGeometry(QtCore.QRect(590, 370, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Bestatigen.setFont(font)
        self.Bestatigen.setObjectName("Bestatigen")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 120, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.Zuruck.setText(_translate("MainWindow", "Zurück"))
        self.Bestatigen.setText(_translate("MainWindow", "Bestätigen"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Art der Fahrt"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Dienstlich"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Privat"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Von aktuellem Standort"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Nach Hause"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Fahrtbeginn()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

