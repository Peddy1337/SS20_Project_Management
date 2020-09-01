from PyQt5 import QtCore, QtGui, QtWidgets


class Unter25(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 235)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: #404040;}\n"
"QPushButton{\n"
"    color: #FFFFCC; \n"
"    font: bold 30px; \n"
"    height: 50 px;\n"
"    width: 50 px;\n"
"    background-color: #006600;\n"
"    border-style: inset;\n"
"    border-color:black;\n"
"    border-width: 1px;}")
        self.q = QtWidgets.QPushButton(Dialog)
        self.q.setObjectName("q")
        self.q.move(10, 10)
        self.w = QtWidgets.QPushButton(Dialog)
        self.w.setObjectName("w")
        self.w.move(65, 10)
        self.e = QtWidgets.QPushButton(Dialog)
        self.e.setObjectName("e")
        self.e.move(120, 10)
        self.r = QtWidgets.QPushButton(Dialog)
        self.r.setObjectName("r")
        self.r.move(175, 10)
        self.t = QtWidgets.QPushButton(Dialog)
        self.t.setObjectName("t")
        self.t.move(230, 10)
        self.z = QtWidgets.QPushButton(Dialog)
        self.z.setObjectName("z")
        self.z.move(285, 10)
        self.u = QtWidgets.QPushButton(Dialog)
        self.u.setObjectName("u")
        self.u.move(340, 10)
        self.i = QtWidgets.QPushButton(Dialog)
        self.i.setObjectName("i")
        self.i.move(395, 10)
        self.o = QtWidgets.QPushButton(Dialog)
        self.o.setObjectName("o")
        self.o.move(450, 10)
        self.p = QtWidgets.QPushButton(Dialog)
        self.p.setObjectName("p")
        self.p.move(505, 10)
        self.ü = QtWidgets.QPushButton(Dialog)
        self.ü.setObjectName("ü")
        self.ü.move(560, 10)
        self.ß = QtWidgets.QPushButton(Dialog)
        self.ß.setObjectName("ß")
        self.ß.move(615, 10)
        self.a = QtWidgets.QPushButton(Dialog)
        self.a.setObjectName("a")
        self.a.move(35, 65)
        self.s = QtWidgets.QPushButton(Dialog)
        self.s.setObjectName("s")
        self.s.move(90, 65)
        self.d = QtWidgets.QPushButton(Dialog)
        self.d.setObjectName("d")
        self.d.move(145, 65)
        self.f = QtWidgets.QPushButton(Dialog)
        self.f.setObjectName("f")
        self.f.move(200, 65)
        self.g = QtWidgets.QPushButton(Dialog)
        self.g.setObjectName("g")
        self.g.move(255, 65)
        self.h = QtWidgets.QPushButton(Dialog)
        self.h.setObjectName("h")
        self.h.move(310, 65)
        self.j = QtWidgets.QPushButton(Dialog)
        self.j.setObjectName("j")
        self.j.move(365, 65)
        self.k = QtWidgets.QPushButton(Dialog)
        self.k.setObjectName("k")
        self.k.move(420, 65)
        self.l = QtWidgets.QPushButton(Dialog)
        self.l.setObjectName("l")
        self.l.move(475, 65)
        self.ö = QtWidgets.QPushButton(Dialog)
        self.ö.setObjectName("ö")
        self.ö.move(530, 65)
        self.ä = QtWidgets.QPushButton(Dialog)
        self.ä.setObjectName("ä")
        self.ä.move(585, 65)
        self.y = QtWidgets.QPushButton(Dialog)
        self.y.setObjectName("y")
        self.y.move(60, 120)
        self.x = QtWidgets.QPushButton(Dialog)
        self.x.setObjectName("x")
        self.x.move(115, 120)
        self.c = QtWidgets.QPushButton(Dialog)
        self.c.setObjectName("c")
        self.c.move(170, 120)
        self.v = QtWidgets.QPushButton(Dialog)
        self.v.setObjectName("v")
        self.v.move(225, 120)
        self.b = QtWidgets.QPushButton(Dialog)
        self.b.setObjectName("b")
        self.b.move(280, 120)
        self.n = QtWidgets.QPushButton(Dialog)
        self.n.setObjectName("n")
        self.n.move(335, 120)
        self.m = QtWidgets.QPushButton(Dialog)
        self.m.setObjectName("m")
        self.m.move(390, 120)
        self.strich = QtWidgets.QPushButton(Dialog)
        self.strich.setObjectName("strich")
        self.strich.move(445, 120)
        self.space = QtWidgets.QPushButton(Dialog)
        self.space.setObjectName("space")
        self.space.setGeometry(QtCore.QRect(170,175,300,50))
        self.delete = QtWidgets.QPushButton(Dialog)
        self.delete.setObjectName("delete")
        self.delete.setGeometry(QtCore.QRect(565,175,100,50))
        self.shift = QtWidgets.QPushButton(Dialog)
        self.shift.setObjectName("shift")
        self.shift.setGeometry(QtCore.QRect(5,175,100,50))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.a.setText(_translate("Dialog", "A"))
        self.b.setText(_translate("Dialog", "B"))
        self.c.setText(_translate("Dialog", "C"))
        self.d.setText(_translate("Dialog", "D"))
        self.e.setText(_translate("Dialog", "E"))
        self.f.setText(_translate("Dialog", "F"))
        self.g.setText(_translate("Dialog", "G"))
        self.h.setText(_translate("Dialog", "H"))
        self.i.setText(_translate("Dialog", "I"))
        self.j.setText(_translate("Dialog", "J"))
        self.k.setText(_translate("Dialog", "K"))
        self.l.setText(_translate("Dialog", "L"))
        self.m.setText(_translate("Dialog", "M"))
        self.n.setText(_translate("Dialog", "N"))
        self.o.setText(_translate("Dialog", "O"))
        self.p.setText(_translate("Dialog", "P"))
        self.q.setText(_translate("Dialog", "Q"))
        self.r.setText(_translate("Dialog", "R"))
        self.s.setText(_translate("Dialog", "S"))
        self.t.setText(_translate("Dialog", "T"))
        self.u.setText(_translate("Dialog", "U"))
        self.v.setText(_translate("Dialog", "V"))
        self.w.setText(_translate("Dialog", "W"))
        self.x.setText(_translate("Dialog", "X"))
        self.y.setText(_translate("Dialog", "Y"))
        self.z.setText(_translate("Dialog", "Z"))
        self.ß.setText(_translate("Dialog", "ß"))
        self.ä.setText(_translate("Dialog", "Ä"))
        self.ö.setText(_translate("Dialog", "Ö"))
        self.ü.setText(_translate("Dialog", "Ü"))
        self.space.setText(_translate("Dialog", "space"))
        self.delete.setText(_translate("Dialog", "←"))
        self.strich.setText(_translate("Dialog", "-"))
        self.shift.setText(_translate("Dialog", "↑"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Unter25()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
