import json
from typing import *
from qt_ui.test_table import Ui_MainWindow as TestMainWindow
from qt_ui.test_table_opposing import Ui_MainWindow as OpposingTestMainWindow
from PyQt5 import QtWidgets as qtw
import pickle
from PyQt5 import QtGui
from fast_many_rolls import FastManyRolls
from main_window_menu import MainWindowMenu
from table_list_ui import TableListUI


# todo make classes for: table header, table bottom
class MainWindowUI(qtw.QMainWindow):
    def __init__(self, is_opposing, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_opposing = is_opposing
        self.roll_lists: List[TableListUI] = list()

        if not self.is_opposing:
            self.ui = TestMainWindow()
            self.ui.setupUi(self)

            test_roll_list = TableListUI(
                self.ui.scrollAreaWidgetContents,
                self.ui.test_skill_list,
                self.ui.add_to_list_button,
                self.ui.difficulty_spin_box
            )
            self.roll_lists.append(test_roll_list)
        else:
            self.ui: OpposingTestMainWindow = OpposingTestMainWindow()
            self.ui.setupUi(self)

            left_roll_list = TableListUI(
                self.ui.scrollAreaWidgetLeft,
                self.ui.test_skill_list_left,
                self.ui.add_to_list_button_left,
                self.ui.difficulty_spin_box_left
            )
            right_roll_list = TableListUI(
                self.ui.scrollAreaWidgetRight,
                self.ui.test_skill_list_right,
                self.ui.add_to_list_button_right,
                self.ui.difficulty_spin_box_right
            )
            self.roll_lists = [left_roll_list, right_roll_list]

        self.fast_many_rolls = FastManyRolls()
        self.menu_ui = MainWindowMenu(self)

        # references
        self.character_creator = None

        self._connect_buttons()

    def _connect_buttons(self):
        if not self.is_opposing:
            self.ui.pushButton.clicked.connect(self.roll_group_test)
        else:
            self.ui.pushButton.clicked.connect(self.roll_opposing_test)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.matches(QtGui.QKeySequence.Delete):
            for roll_list in self.roll_lists:
                roll_list.delete_selected()

    def roll_group_test(self):
        character_entries = self.roll_lists[0].character_entries
        self.fast_many_rolls.attackers = [entry.character for entry in character_entries]
        self.fast_many_rolls.attacking_ability = self.roll_lists[0].tested_skill
        # todo move to fmr
        results = self.fast_many_rolls.resolve_group_test(self.roll_lists[0].difficulty)
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

    def roll_opposing_test(self):
        attackers = self.roll_lists[0].character_entries
        defenders = self.roll_lists[1].character_entries
        self.fast_many_rolls.attackers = [entry.character for entry in attackers]
        self.fast_many_rolls.defenders = [entry.character for entry in defenders]
        self.fast_many_rolls.attacking_ability = self.roll_lists[0].tested_skill
        self.fast_many_rolls.defending_ability = self.roll_lists[1].tested_skill

        results = self.fast_many_rolls.resolve_attack(False)
        pass
