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


class MainWindowUI(qtw.QMainWindow):
    def __init__(self, is_opposing, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_opposing = is_opposing
        self.roll_lists: List[TableListUI] = list()

        self.ui: Union[TestMainWindow, OpposingTestMainWindow] = None
        self.menu_ui: MainWindowMenu = None

        if not self.is_opposing:
            self._init_for_grout_test()
        else:
            self._init_for_opposing_test()

        self.fast_many_rolls = FastManyRolls()

        # references
        self.character_creator = None

    def _init_for_grout_test(self):
        self.ui = TestMainWindow()
        self.ui.setupUi(self)

        test_roll_list = TableListUI(
            self.ui.scrollAreaWidgetContents,
            self.ui.test_skill_list,
            self.ui.add_to_list_button,
            self.ui.difficulty_spin_box
        )
        self.roll_lists = [test_roll_list]
        self.menu_ui = MainWindowMenu(self)
        self._connect_buttons()

    def _init_for_opposing_test(self):
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
        self.menu_ui = MainWindowMenu(self)
        self._connect_buttons()

    def switch_mode(self):
        if self.is_opposing:
            self.is_opposing = False
            self._init_for_grout_test()
        else:
            self.is_opposing = True
            self._init_for_opposing_test()
        return self

    def _connect_buttons(self):
        if not self.is_opposing:
            self.ui.pushButton.clicked.connect(self.roll_group_test)
        else:
            self.ui.pushButton.clicked.connect(self.roll_opposing_test)
            self.ui.flip_sides_btn.clicked.connect(self.flip_sides)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.matches(QtGui.QKeySequence.Delete):
            for roll_list in self.roll_lists:
                roll_list.delete_selected()

    def flip_sides(self):
        if not self.is_opposing:
            return
        roll_list_left = self.roll_lists[0]
        roll_list_right = self.roll_lists[1]
        left_characters = [c for c in roll_list_left.character_entries]
        right_characters = [c for c in roll_list_right.character_entries]
        roll_list_left.delete_all()
        roll_list_right.delete_all()
        for table_list, roll_list in [(roll_list_right, left_characters), (roll_list_left, right_characters)]:
            for c in roll_list:
                table_list.insert_widget_at_top(c)
                table_list.character_entries.append(c)
                if table_list.tested_skill is not None:
                    c.set_skill_value(c.character[table_list.tested_skill])

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
        is_ranged = self.ui.is_ranged_checkbox.isChecked()
        combat = self.ui.is_combat_checkbox.isChecked()

        attackers = self.roll_lists[0].character_entries
        defenders = self.roll_lists[1].character_entries
        self.fast_many_rolls.attackers = [entry.character for entry in attackers]
        self.fast_many_rolls.defenders = [entry.character for entry in defenders]
        self.fast_many_rolls.attacking_ability = self.roll_lists[0].tested_skill
        self.fast_many_rolls.defending_ability = self.roll_lists[1].tested_skill

        results = self.fast_many_rolls.resolve_attack(is_ranged, combat)
        pass
