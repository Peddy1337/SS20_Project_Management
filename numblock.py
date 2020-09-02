# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numblock.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form, function):
        Form.setObjectName("Form")
        Form.resize(220, 290)
        Form.setStyleSheet("QWidget{background-color: #999999}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #4FC44F;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 10, 60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 10, 60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 80, 60, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 80, 60, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 80, 60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 150, 60, 60))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 150, 60, 60))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 150, 60, 60))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 220, 60, 60))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 220, 60, 60))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton.clicked.connect(lambda: function(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: function(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: function(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: function(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: function(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: function(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: function(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: function(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: function(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: function(self.pushButton_10))
        self.pushButton_11.clicked.connect(lambda: function(self.pushButton_11))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_10.setText(_translate("Form", "0"))
        self.pushButton_11.setText(_translate("Form", "Delete"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
