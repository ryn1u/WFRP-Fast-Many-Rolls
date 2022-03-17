from table_entry import Ui_table_entry_frame as TableEntry
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui


class TableEntryUI(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = TableEntry()
        self.ui.setupUi(self)

        self.character = None
        self.selected = False

    def get_character_name(self):
        return self.ui.character_name.text()

    def set_character_name(self, name):
        self.ui.character_name.setText(name)

    def set_skill_value(self, skill):
        self.ui.skill_value_label.setText(str(skill))

    def get_skill_value(self):
        return int(self.ui.skill_value_label.text())

    def set_roll(self, roll):
        self.ui.roll_label.setText(str(roll))

    def get_roll(self):
        return int(self.ui.roll_label.text())

    def set_ps(self, ps):
        self.ui.ps_label.setText(str(ps))

    def get_ps(self):
        return int(self.ui.ps_label.text())

    def toggle_selection(self):
        self.selected = not self.selected
        if self.selected:
            self.ui.frame.setFrameStyle(qtw.QFrame.Panel)
        else:
            self.ui.frame.setFrameStyle(qtw.QFrame.StyledPanel)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == 2:
            self.toggle_selection()
