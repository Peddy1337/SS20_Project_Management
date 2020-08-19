# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fahrtbeginn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
"QLineEdit{\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QLabel{\n"
"    color: #FFFFCC;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Zuruck = QtWidgets.QPushButton(self.centralwidget)
        self.Zuruck.setGeometry(QtCore.QRect(10, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Zuruck.setFont(font)
        self.Zuruck.setObjectName("Zuruck")
        self.Bestatigen = QtWidgets.QPushButton(self.centralwidget)
        self.Bestatigen.setGeometry(QtCore.QRect(590, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Bestatigen.setFont(font)
        self.Bestatigen.setObjectName("Bestatigen")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(540, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(690, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 70, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.KM_Stand = QtWidgets.QLineEdit(self.centralwidget)
        self.KM_Stand.setGeometry(QtCore.QRect(540, 120, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.KM_Stand.setFont(font)
        self.KM_Stand.setObjectName("KM_Stand")
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
        self.Zuruck.setText(_translate("MainWindow", "Zuruck"))
        self.Bestatigen.setText(_translate("MainWindow", "Bestatigen"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "Anfangs KM-Stand:"))
        self.lineEdit.setText(_translate("MainWindow", "Art der Fahrt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

