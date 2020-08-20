# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anmeldenfinal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from numblock import Ui_Form as Form
import binding
class anmelden(object):     
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("QWidget{background-color: #404040;}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QLineEdit {\n"
"    color: #FFFFCC;\n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}\n"
"QCheckBox, QLabel{\n"
"    color: #FFFFCC;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:
                        binding.Controlling.anmelden_start(self,MainWindow))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 320, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:
                        binding.Controlling.anmelden_home(self,MainWindow))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 20, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = LineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 70, 200, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(200, 120, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(30, 30))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 161))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
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
        self.pushButton.setText(_translate("MainWindow", "Zurück"))
        self.pushButton_2.setText(_translate("MainWindow", "Bestätigen"))
        self.lineEdit.setText(_translate("MainWindow", "Name"))
        self.lineEdit_2.setText(_translate("MainWindow", "Pin"))
        self.checkBox.setText(_translate("MainWindow", "Angemeldet bleiben"))
        self.label.setText(_translate("MainWindow", "Dies ist ein Platzhalter für das Bild "))

class LineEdit(QtWidgets.QLineEdit):
    
    def mousePressEvent(self,event):
        if(self.text() == 'Pin') :            
            self.clear()
        
        self.dialog = QtWidgets.QWidget()
        self.dialog.ui = Form()
        self.dialog.ui.setupUi(self.dialog,self.editTextFromSlot)
        self.dialog.move(self.pos().x(),self.pos().y()+80)
        self.dialog.show()
        super(LineEdit,self).mousePressEvent(event)
        
    def editTextFromSlot(self,button) :
        self.insert(button.text())

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = anmelden()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
