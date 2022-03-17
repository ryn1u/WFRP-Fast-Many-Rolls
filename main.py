from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from fastmanyrollsui import FastManyRollsUI


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = FastManyRollsUI()
    widget.show()

    app.exec()
