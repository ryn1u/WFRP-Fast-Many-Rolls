from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from main_window import MainWindowUI


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = MainWindowUI()
    widget.show()

    app.exec()

# todo:
#   move table list widgets to separate qt ui files
#   split main window functionality into multiple classes
#   make main fmr ui class generic for test and opposing throws
