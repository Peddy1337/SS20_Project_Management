# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fahrt.ui'
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
        self.Fahrart_andern = QtWidgets.QPushButton(self.centralwidget)
        self.Fahrart_andern.setGeometry(QtCore.QRect(540, 270, 250, 70))
        self.Fahrart_andern.setObjectName("Fahrart_andern")
        self.Fahrt_beenden = QtWidgets.QPushButton(self.centralwidget)
        self.Fahrt_beenden.setGeometry(QtCore.QRect(540, 350, 250, 70))
        self.Fahrt_beenden.setObjectName("Fahrt_beenden")
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(30, 60, 481, 360))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.Name.setObjectName("Name")
        self.Art_der_Fahrt = QtWidgets.QLineEdit(self.centralwidget)
        self.Art_der_Fahrt.setGeometry(QtCore.QRect(220, 10, 200, 40))
        self.Art_der_Fahrt.setObjectName("Art_der_Fahrt")
        self.Uhrzeit_feld = QtWidgets.QLineEdit(self.centralwidget)
        self.Uhrzeit_feld.setGeometry(QtCore.QRect(540, 40, 115, 32))
        self.Uhrzeit_feld.setObjectName("Uhrzeit_feld")
        self.Datum_feld = QtWidgets.QLineEdit(self.centralwidget)
        self.Datum_feld.setGeometry(QtCore.QRect(675, 40, 115, 32))
        self.Datum_feld.setObjectName("Datum_feld")
        self.Gefahrende_KM_feld = QtWidgets.QLineEdit(self.centralwidget)
        self.Gefahrende_KM_feld.setGeometry(QtCore.QRect(540, 122, 250, 32))
        self.Gefahrende_KM_feld.setObjectName("Gefahrende_KM_feld")
        self.Fahrzeit_feld = QtWidgets.QLineEdit(self.centralwidget)
        self.Fahrzeit_feld.setGeometry(QtCore.QRect(540, 204, 250, 32))
        self.Fahrzeit_feld.setObjectName("Fahrzeit_feld")
        self.Uhrzeit_label = QtWidgets.QLabel(self.centralwidget)
        self.Uhrzeit_label.setGeometry(QtCore.QRect(540, 10, 120, 30))
        self.Uhrzeit_label.setObjectName("Uhrzeit_label")
        self.Datum_label = QtWidgets.QLabel(self.centralwidget)
        self.Datum_label.setGeometry(QtCore.QRect(670, 10, 120, 30))
        self.Datum_label.setObjectName("Datum_label")
        self.Gefahrende_KM_label = QtWidgets.QLabel(self.centralwidget)
        self.Gefahrende_KM_label.setGeometry(QtCore.QRect(540, 92, 250, 30))
        self.Gefahrende_KM_label.setObjectName("Gefahrende_KM_label")
        self.Fahrzeit_label = QtWidgets.QLabel(self.centralwidget)
        self.Fahrzeit_label.setGeometry(QtCore.QRect(540, 174, 250, 30))
        self.Fahrzeit_label.setObjectName("Fahrzeit_label")
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
        self.Fahrart_andern.setText(_translate("MainWindow", "Art der Fahrt andern"))
        self.Fahrt_beenden.setText(_translate("MainWindow", "Fahrt beenden"))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.Art_der_Fahrt.setText(_translate("MainWindow", "Art der Fahrt"))
        self.Uhrzeit_label.setText(_translate("MainWindow", "Uhrzeit:"))
        self.Datum_label.setText(_translate("MainWindow", "Datum:"))
        self.Gefahrende_KM_label.setText(_translate("MainWindow", "Gefahrende KM:"))
        self.Fahrzeit_label.setText(_translate("MainWindow", "Fahrzeit:"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
