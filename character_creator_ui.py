from character_creator import Ui_Form as CharacterCreator
from add_advanced_skill_dialog_ui import AddAdvancedSkillUI
from advanced_skill_entry import Ui_advanced_skill_entry as AdvancedSkillEntry
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from utils import BASIC_SKILLS, ATTRIBUTES
from typing import Union


class CharacterCreatorUI(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = CharacterCreator()
        self.ui.setupUi(self)
        self.setWindowTitle("Character editor")

        self.attributes = {
            attribute: self._initialize_field(attribute, "attribute", num)
            for num, attribute in enumerate(ATTRIBUTES)
        }
        self.basic_skills = {
            basic_skill: self._initialize_field(basic_skill, "basic_skill", num)
            for num, basic_skill in enumerate(BASIC_SKILLS)
        }

        self.misc = {
            misc: self._initialize_field(misc, "misc", num)
            for num, misc in enumerate(["Advantage", "Wounds"])
        }

        self.add_advanced_skill_dialog: Union[None, AddAdvancedSkillUI] = None
        self.ui.add_advanced_skill_button.clicked.connect(self.show_advanced_skill_dialog)

    def _initialize_field(self, name, field_type, num, value=0):
        text = self.ui.__getattribute__(f"{field_type}_label_{num+1}")
        spin_box = self.ui.__getattribute__(f"{field_type}_value_{num+1}")
        text.setText(name)
        spin_box.setValue(value)
        return spin_box

    def show_advanced_skill_dialog(self):
        if self.add_advanced_skill_dialog is not None:
            return
        add_advanced_skill_dialog = AddAdvancedSkillUI()
        add_advanced_skill_dialog.show()
        self.add_advanced_skill_dialog = add_advanced_skill_dialog
        self.add_advanced_skill_dialog.ui.add_button.clicked.connect(self.add_advanced_skill_callback)

    def add_advanced_skill_callback(self):
        skill = self.add_advanced_skill_dialog.ui.advnaced_skill_box.currentText()
        specialization = self.add_advanced_skill_dialog.ui.specialization_value.text()
        self.add_advanced_skill_dialog.close()
        self.add_advanced_skill_dialog = None

        self.add_advanced_skill_entry(skill, specialization)

    def add_advanced_skill_entry(self, skill, specialization):
        print(skill)
        print(specialization)
        entry: AdvancedSkillEntryUI = AdvancedSkillEntryUI()
        entry.set_text(skill, specialization)

        layout = self.ui.scrollAreaWidgetContents.layout()
        button_item = layout.itemAt(len(layout) - 2)
        spacer_item = layout.itemAt(len(layout) - 1)
        layout.removeItem(button_item)
        layout.removeItem(spacer_item)
        layout.addWidget(entry)
        layout.addItem(button_item)
        layout.addItem(spacer_item)


class AdvancedSkillEntryUI(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = AdvancedSkillEntry()
        self.ui.setupUi(self)

    def set_text(self, skill, specialization):
        self.ui.advanced_skill_label.setText(skill)
        self.ui.specialization_label.setText(specialization)
