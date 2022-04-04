from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from main_window import MainWindowUI


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = MainWindowUI(True)
    widget.show()

    app.exec()

# todo:
#   add attacking test difficulty
