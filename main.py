from frontend.binding import Controlling
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gui = Controlling()
    gui.showFullScreen()
    app.exec_()
