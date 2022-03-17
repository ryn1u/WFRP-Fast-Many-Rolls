from table_entry_ui import TableEntryUI
import json
from typing import *
from test_table import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui
from character import Character
from fast_many_rolls import FastManyRolls

from character_creator_ui import CharacterCreatorUI
from select_character_dialog_ui import SelectCharacterDialogUI


class FastManyRollsUI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fast_many_rolls = FastManyRolls()

        self.tested_skill = None
        self.difficulty = 0
        self.character_entries: List[TableEntryUI] = list()

        self._load_skill_lists()

        # references
        self.character_creator = None
        self.character_select = None

        self._connect_buttons()

    def _load_skill_lists(self):
        from utils import ATTRIBUTES, BASIC_SKILLS, ADVANCED_SKILLS
        skills = ["", *ATTRIBUTES, *BASIC_SKILLS, *ADVANCED_SKILLS]
        self.ui.test_skill_list.addItems(skills)

    def open_new_character_creator(self):
        self.character_creator = CharacterCreatorUI()
        self.character_creator.show()

    def edit_character(self):
        filename = self.open_file_name_dialog()
        with open(filename, 'r') as file:
            data = json.load(file)
        self.character_creator = CharacterCreatorUI()
        self.character_creator.load_character(data)
        self.character_creator.show()

    def set_tested_skill(self):
        self.tested_skill = self.ui.test_skill_list.currentText()
        for c in self.character_entries:
            c.set_skill_value(c.character[self.tested_skill])

    def add_character_entry(self, char_data):
        # todo create character object
        table_entry_widget = TableEntryUI()
        table_entry_widget.character = Character.from_dict(char_data)
        table_entry_widget.set_character_name(char_data["name"])
        if self.tested_skill is not None:
            table_entry_widget.set_skill_value(table_entry_widget.character[self.tested_skill])
        self.insert_widget_at_top(table_entry_widget)
        self.character_entries.append(table_entry_widget)

    def insert_widget_at_top(self, widget):
        layout = self.ui.scrollAreaWidgetContents.layout()
        layout_len = len(layout)
        items = [layout.itemAt(layout_len - 2), layout.itemAt(layout_len - 1)]
        for item in items:
            layout.removeItem(item)
        layout.addWidget(widget)
        for item in items:
            layout.addItem(item)

    def _connect_buttons(self):
        self.ui.actionCaracterNew.triggered.connect(lambda: self.open_new_character_creator())
        self.ui.actionCharacterEdit.triggered.connect(lambda: self.edit_character())
        self.ui.test_skill_list.currentTextChanged.connect(self.set_tested_skill)
        self.ui.add_to_list_button.clicked.connect(self.open_select_character_dialog)
        self.ui.pushButton.clicked.connect(self.roll_group_test)
        self.ui.difficulty_spin_box.valueChanged.connect(self.set_difficulty)

    def open_file_name_dialog(self): #todo open characters folder
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        file_name, _ = qtw.QFileDialog.getOpenFileName(self, "Load Character", "", "Json Files (*.json);;All Files (*)", options=options)
        return file_name

    def open_select_character_dialog(self):
        self.character_select = SelectCharacterDialogUI()
        self.character_select.selected_event.connect(lambda: self.add_character_entry(self.character_select.selected_character))
        self.character_select.show()

    def delete_selected_characters(self):
        for character in self.character_entries:
            if character.selected:
                self.character_entries.remove(character)
                self.ui.scrollAreaWidgetContents.layout().removeWidget(character)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.matches(QtGui.QKeySequence.Delete):
            self.delete_selected_characters()

    def set_difficulty(self):
        self.difficulty = self.ui.difficulty_spin_box.value()

    def roll_group_test(self):
        self.fast_many_rolls.attackers = [entry.character for entry in self.character_entries]
        self.fast_many_rolls.attacking_ability = self.tested_skill
        # todo move to fmr
        results = self.fast_many_rolls.resolve_group_test(self.difficulty)
        total = 0
        for idx, result in enumerate(results):
            roll, ps, _ = result
            self.character_entries[idx].set_roll(roll)
            self.character_entries[idx].set_ps(ps)
            if self.ui.only_positive_check.isChecked():
                if ps > 0:
                    total += ps
            else:
                total += ps
        self.ui.result_label.setText(str(total))
