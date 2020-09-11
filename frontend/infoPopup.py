# Form implementation generated from reading ui file 'infoPopup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Popup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 180)
        Form.setStyleSheet("QWidget{background-color: #999999}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint| QtCore.Qt.Popup)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(105, 110, 90, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Form.close)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10,10, 280, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.label.setText(_translate("Form", "Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Popup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
