from table_entry_ui import TableEntryUI
from typing import *
from qt_ui.test_table import Ui_MainWindow as TestTable
from select_character_dialog_ui import SelectCharacterDialogUI
from PyQt5 import QtWidgets as qtw
from character import Character


class TableListUI:
    def __init__(self, test_list_frame: TestTable, test_skill_combo: qtw.QComboBox):
        self.tested_skill = None
        self.test_skill_combo: qtw.QComboBox = test_skill_combo
        self.layout: qtw.QWidget = test_list_frame.scrollAreaWidgetContents.layout()
        self.character_entries: List[TableEntryUI] = list()

        self._load_skill_lists()

        self.character_select = None
        test_list_frame.add_to_list_button.clicked.connect(self.open_select_character_dialog)

    def insert_widget_at_top(self, widget):
        layout_len = len(self.layout)
        items = [self.layout.itemAt(layout_len - 2), self.layout.itemAt(layout_len - 1)]
        for item in items:
            self.layout.removeItem(item)
        self.layout.addWidget(widget)
        for item in items:
            self.layout.addItem(item)

    def set_tested_skill(self):
        self.tested_skill = self.test_skill_combo.currentText()
        for c in self.character_entries:
            c.set_skill_value(c.character[self.tested_skill])

    def add_character_entry(self, char_data):
        table_entry_widget = TableEntryUI()
        table_entry_widget.character = Character.from_dict(char_data)
        table_entry_widget.set_character_name(char_data["name"])
        if self.tested_skill is not None:
            table_entry_widget.set_skill_value(table_entry_widget.character[self.tested_skill])
        self.insert_widget_at_top(table_entry_widget)
        self.character_entries.append(table_entry_widget)

    def open_select_character_dialog(self):
        self.character_select = SelectCharacterDialogUI()
        self.character_select.selected_event.connect(
            lambda: self.add_character_entry(self.character_select.selected_character))
        self.character_select.show()

    def _load_skill_lists(self):
        from utils import ATTRIBUTES, BASIC_SKILLS, ADVANCED_SKILLS
        skills = ["", *ATTRIBUTES, *BASIC_SKILLS, *ADVANCED_SKILLS]
        self.test_skill_combo.addItems(skills)
