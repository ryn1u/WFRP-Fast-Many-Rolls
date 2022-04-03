import json
from qt_ui.test_table import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
import pickle
from PyQt5 import QtGui
from fast_many_rolls import FastManyRolls
from main_window_menu import MainWindowManu
from table_list_ui import TableListUI


# todo make classes for: table header, table bottom
class MainWindowUI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fast_many_rolls = FastManyRolls()
        self.menu_ui = MainWindowManu(self)
        self.table_list_ui = TableListUI(self.ui, self.ui.test_skill_list)

        self.difficulty = 0

        # references
        self.character_creator = None

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.test_skill_list.currentTextChanged.connect(self.table_list_ui.set_tested_skill)
        self.ui.pushButton.clicked.connect(self.roll_group_test)
        self.ui.difficulty_spin_box.valueChanged.connect(self.set_difficulty)

    def delete_selected_characters(self):
        # todo delegate to new subclass
        for i in range(len(self.table_list_ui.character_entries) - 1, -1, -1):
            character = self.table_list_ui.character_entries[i]
            if character.selected:
                self.table_list_ui.character_entries.remove(character)
                character.remove()

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.matches(QtGui.QKeySequence.Delete):
            self.delete_selected_characters()

    def set_difficulty(self):
        self.difficulty = self.ui.difficulty_spin_box.value()

    def roll_group_test(self):
        character_entries = self.table_list_ui.character_entries
        self.fast_many_rolls.attackers = [entry.character for entry in character_entries]
        self.fast_many_rolls.attacking_ability = self.table_list_ui.tested_skill
        # todo move to fmr
        results = self.fast_many_rolls.resolve_group_test(self.difficulty)
        total = 0
        for idx, result in enumerate(results):
            roll, ps, _ = result
            character_entries[idx].set_roll(roll)
            character_entries[idx].set_ps(ps)
            if self.ui.only_positive_check.isChecked():
                if ps > 0:
                    total += ps
            else:
                total += ps
        self.ui.result_label.setText(str(total))


