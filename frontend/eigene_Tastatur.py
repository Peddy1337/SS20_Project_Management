from PyQt5 import QtCore, QtGui, QtWidgets


class Keyboard(object):
    def setupUi(self, Dialog, keyFunction,delFunction):
        self.isUpper = True
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 290)
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
"    border-width: 1px;\n"
"    border-radius: 15px;}")
        self.lL = []
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setObjectName("1")
        self.b1.move(102.5, 10)
        self.b2 = QtWidgets.QPushButton(Dialog)
        self.b2.setObjectName("2")
        self.b2.move(157.5, 10)
        self.b3 = QtWidgets.QPushButton(Dialog)
        self.b3.setObjectName("3")
        self.b3.move(212.5, 10)
        self.b4 = QtWidgets.QPushButton(Dialog)
        self.b4.setObjectName("4")
        self.b4.move(267.5, 10)
        self.b5 = QtWidgets.QPushButton(Dialog)
        self.b5.setObjectName("5")
        self.b5.move(322.5, 10)
        self.b6 = QtWidgets.QPushButton(Dialog)
        self.b6.setObjectName("6")
        self.b6.move(377.5, 10)
        self.b7 = QtWidgets.QPushButton(Dialog)
        self.b7.setObjectName("7")
        self.b7.move(432.5, 10)
        self.b8 = QtWidgets.QPushButton(Dialog)
        self.b8.setObjectName("8")
        self.b8.move(487.5, 10)
        self.b9 = QtWidgets.QPushButton(Dialog)
        self.b9.setObjectName("9")
        self.b9.move(542.5, 10)
        self.b0 = QtWidgets.QPushButton(Dialog)
        self.b0.setObjectName("0")
        self.b0.move(597.5, 10)
        self.q = QtWidgets.QPushButton(Dialog)
        self.q.setObjectName("q")
        self.q.move(72.5, 65)
        self.lL.append(self.q)
        self.w = QtWidgets.QPushButton(Dialog)
        self.w.setObjectName("w")
        self.w.move(127.5, 65)
        self.lL.append(self.w)
        self.e = QtWidgets.QPushButton(Dialog)
        self.e.setObjectName("e")
        self.e.move(182.5, 65)
        self.lL.append(self.e)
        self.r = QtWidgets.QPushButton(Dialog)
        self.r.setObjectName("r")
        self.r.move(237.5, 65)
        self.lL.append(self.r)
        self.t = QtWidgets.QPushButton(Dialog)
        self.t.setObjectName("t")
        self.t.move(292.5, 65)
        self.lL.append(self.t)
        self.z = QtWidgets.QPushButton(Dialog)
        self.z.setObjectName("z")
        self.z.move(347.5, 65)
        self.lL.append(self.z)
        self.u = QtWidgets.QPushButton(Dialog)
        self.u.setObjectName("u")
        self.u.move(402.5, 65)
        self.lL.append(self.u)
        self.i = QtWidgets.QPushButton(Dialog)
        self.i.setObjectName("i")
        self.i.move(457.5, 65)
        self.lL.append(self.i)
        self.o = QtWidgets.QPushButton(Dialog)
        self.o.setObjectName("o")
        self.o.move(512.5, 65)
        self.lL.append(self.o)
        self.p = QtWidgets.QPushButton(Dialog)
        self.p.setObjectName("p")
        self.p.move(567.5, 65)
        self.lL.append(self.p)
        self.ue = QtWidgets.QPushButton(Dialog)
        self.ue.setObjectName("ü")
        self.ue.move(622.5, 65)
        self.lL.append(self.ue)
        self.sz = QtWidgets.QPushButton(Dialog)
        self.sz.setObjectName("ß")
        self.sz.move(677.5, 65)
        self.a = QtWidgets.QPushButton(Dialog)
        self.a.setObjectName("a")
        self.a.move(97.5, 120)
        self.lL.append(self.a)
        self.s = QtWidgets.QPushButton(Dialog)
        self.s.setObjectName("s")
        self.s.move(152.5, 120)
        self.lL.append(self.s)
        self.d = QtWidgets.QPushButton(Dialog)
        self.d.setObjectName("d")
        self.d.move(207.5, 120)
        self.lL.append(self.d)
        self.f = QtWidgets.QPushButton(Dialog)
        self.f.setObjectName("f")
        self.f.move(262.5, 120)
        self.lL.append(self.f)
        self.g = QtWidgets.QPushButton(Dialog)
        self.g.setObjectName("g")
        self.g.move(317.5, 120)
        self.lL.append(self.g)
        self.h = QtWidgets.QPushButton(Dialog)
        self.h.setObjectName("h")
        self.h.move(372.5, 120)
        self.lL.append(self.h)
        self.j = QtWidgets.QPushButton(Dialog)
        self.j.setObjectName("j")
        self.j.move(427.5, 120)
        self.lL.append(self.j)
        self.k = QtWidgets.QPushButton(Dialog)
        self.k.setObjectName("k")
        self.k.move(482.5, 120)
        self.lL.append(self.k)
        self.l = QtWidgets.QPushButton(Dialog)
        self.l.setObjectName("l")
        self.l.move(537.5, 120)
        self.lL.append(self.l)
        self.oe = QtWidgets.QPushButton(Dialog)
        self.oe.setObjectName("ö")
        self.oe.move(592.5, 120)
        self.lL.append(self.oe)
        self.ae = QtWidgets.QPushButton(Dialog)
        self.ae.setObjectName("ä")
        self.ae.move(647.5, 120)
        self.lL.append(self.ae)
        self.y = QtWidgets.QPushButton(Dialog)
        self.y.setObjectName("y")
        self.y.move(122.5, 175)
        self.lL.append(self.y)
        self.x = QtWidgets.QPushButton(Dialog)
        self.x.setObjectName("x")
        self.x.move(177.5, 175)
        self.lL.append(self.x)
        self.c = QtWidgets.QPushButton(Dialog)
        self.c.setObjectName("c")
        self.c.move(232.5, 175)
        self.lL.append(self.c)
        self.v = QtWidgets.QPushButton(Dialog)
        self.v.setObjectName("v")
        self.v.move(287.5, 175)
        self.lL.append(self.v)
        self.b = QtWidgets.QPushButton(Dialog)
        self.b.setObjectName("b")
        self.b.move(342.5, 175)
        self.lL.append(self.b)
        self.n = QtWidgets.QPushButton(Dialog)
        self.n.setObjectName("n")
        self.n.move(397.5, 175)
        self.lL.append(self.n)
        self.m = QtWidgets.QPushButton(Dialog)
        self.m.setObjectName("m")
        self.m.move(452.5, 175)
        self.lL.append(self.m)
        self.strich = QtWidgets.QPushButton(Dialog)
        self.strich.setObjectName("strich")
        self.strich.move(507.5, 175)
        self.space = QtWidgets.QPushButton(Dialog)
        self.space.setObjectName("space")
        self.space.setGeometry(QtCore.QRect(232.5,230,300,50))
        self.delete = QtWidgets.QPushButton(Dialog)
        self.delete.setObjectName("delete")
        self.delete.setGeometry(QtCore.QRect(627.5,230,100,50))
        self.shift = QtWidgets.QPushButton(Dialog)
        self.shift.setObjectName("shift")
        self.shift.setGeometry(QtCore.QRect(67.5,230,100,50))
        self.shift.clicked.connect(self.changeCase)
        
        self.b1.clicked.connect(lambda: keyFunction(self.b1.text()))
        self.b2.clicked.connect(lambda: keyFunction(self.b2.text()))
        self.b3.clicked.connect(lambda: keyFunction(self.b3.text()))
        self.b4.clicked.connect(lambda: keyFunction(self.b4.text()))
        self.b5.clicked.connect(lambda: keyFunction(self.b5.text()))
        self.b6.clicked.connect(lambda: keyFunction(self.b6.text()))
        self.b7.clicked.connect(lambda: keyFunction(self.b7.text()))
        self.b8.clicked.connect(lambda: keyFunction(self.b8.text()))
        self.b9.clicked.connect(lambda: keyFunction(self.b9.text()))
        self.b0.clicked.connect(lambda: keyFunction(self.b0.text()))
        self.a.clicked.connect(lambda: keyFunction(self.a.text()))
        self.b.clicked.connect(lambda: keyFunction(self.b.text()))
        self.c.clicked.connect(lambda: keyFunction(self.c.text()))
        self.d.clicked.connect(lambda: keyFunction(self.d.text()))
        self.e.clicked.connect(lambda: keyFunction(self.e.text()))
        self.f.clicked.connect(lambda: keyFunction(self.f.text()))
        self.g.clicked.connect(lambda: keyFunction(self.g.text()))
        self.h.clicked.connect(lambda: keyFunction(self.h.text()))
        self.i.clicked.connect(lambda: keyFunction(self.i.text()))
        self.j.clicked.connect(lambda: keyFunction(self.j.text()))
        self.k.clicked.connect(lambda: keyFunction(self.k.text()))
        self.l.clicked.connect(lambda: keyFunction(self.l.text()))
        self.m.clicked.connect(lambda: keyFunction(self.m.text()))
        self.n.clicked.connect(lambda: keyFunction(self.n.text()))
        self.o.clicked.connect(lambda: keyFunction(self.o.text()))
        self.p.clicked.connect(lambda: keyFunction(self.p.text()))
        self.q.clicked.connect(lambda: keyFunction(self.q.text()))
        self.r.clicked.connect(lambda: keyFunction(self.r.text()))
        self.s.clicked.connect(lambda: keyFunction(self.s.text()))
        self.t.clicked.connect(lambda: keyFunction(self.t.text()))
        self.u.clicked.connect(lambda: keyFunction(self.u.text()))
        self.v.clicked.connect(lambda: keyFunction(self.v.text()))
        self.w.clicked.connect(lambda: keyFunction(self.w.text()))
        self.x.clicked.connect(lambda: keyFunction(self.x.text()))
        self.y.clicked.connect(lambda: keyFunction(self.y.text()))
        self.z.clicked.connect(lambda: keyFunction(self.z.text()))
        self.ae.clicked.connect(lambda: keyFunction(self.ae.text()))
        self.oe.clicked.connect(lambda: keyFunction(self.oe.text()))
        self.ue.clicked.connect(lambda: keyFunction(self.ue.text()))
        self.sz.clicked.connect(lambda: keyFunction(self.sz.text()))
        self.strich.clicked.connect(lambda : keyFunction('-'))
        self.space.clicked.connect(lambda : keyFunction(' '))
        self.delete.clicked.connect(delFunction)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.b1.setText(_translate("Dialog", "1"))
        self.b2.setText(_translate("Dialog", "2"))
        self.b3.setText(_translate("Dialog", "3"))
        self.b4.setText(_translate("Dialog", "4"))
        self.b5.setText(_translate("Dialog", "5"))
        self.b6.setText(_translate("Dialog", "6"))
        self.b7.setText(_translate("Dialog", "7"))
        self.b8.setText(_translate("Dialog", "8"))
        self.b9.setText(_translate("Dialog", "9"))
        self.b0.setText(_translate("Dialog", "0"))
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
        self.sz.setText(_translate("Dialog", "ß"))
        self.ae.setText(_translate("Dialog", "Ä"))
        self.oe.setText(_translate("Dialog", "Ö"))
        self.ue.setText(_translate("Dialog", "Ü"))
        self.space.setText(_translate("Dialog", "space"))
        self.delete.setText(_translate("Dialog", "←"))
        self.strich.setText(_translate("Dialog", "-"))
        self.shift.setText(_translate("Dialog", "↑"))

    def createSlot (self,obj , function):
        return function(obj.text())
    
    def changeCase(self) :
        if self.isUpper :
            for l in self.lL :
                l.setText(l.text().lower())
            self.isUpper = False
        else :
            for l in self.lL :
                l.setText(l.text().upper())
            self.isUpper = True

class LineEdit(QtWidgets.QLineEdit):
    
    def mousePressEvent(self,event):
        if(self.text() == 'Name' or self.text() == 'Adresse' or self.text() == 'Zweck der Fahrt') :            
            self.clear()
        
        self.dialog = QtWidgets.QWidget()
        self.dialog.ui = Keyboard()
        self.dialog.ui.setupUi(self.dialog,self.editTextFromSlot, self.deleteCharFromSlot)
        self.dialog.move(0,190)
        self.dialog.show()
        super(LineEdit,self).mousePressEvent(event)
        
    def editTextFromSlot(self,text) :
        self.insert(text)

    def deleteCharFromSlot(self) :
        self.backspace()
