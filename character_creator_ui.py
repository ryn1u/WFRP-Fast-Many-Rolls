from qt_ui.character_creator import Ui_Form as CharacterCreator
from add_advanced_skill_dialog_ui import AddAdvancedSkillUI
from qt_ui.advanced_skill_entry import Ui_advanced_skill_entry as AdvancedSkillEntry
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui

from utils import BASIC_SKILLS, ATTRIBUTES
from typing import Union

import json


# todo add specialization handling
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

        self.advanced_skills = {}

        self.add_advanced_skill_dialog: Union[None, AddAdvancedSkillUI] = None
        self.ui.add_advanced_skill_button.clicked.connect(self.show_advanced_skill_dialog)
        self.ui.pushButton.clicked.connect(self.save_character)

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

    def add_advanced_skill_entry(self, skill, specialization, value=0):
        entry: AdvancedSkillEntryUI = AdvancedSkillEntryUI()
        entry.set_text(skill, specialization)
        entry.ui.advanced_skill_value.setValue(value)
        if skill in self.advanced_skills:
            if specialization in self.advanced_skills[skill]:
                return
            else:
                self.advanced_skills[skill][specialization] = entry.ui.advanced_skill_value
        else:
            self.advanced_skills[skill] = {specialization: entry.ui.advanced_skill_value}

        layout = self.ui.scrollAreaWidgetContents.layout()
        button_item = layout.itemAt(len(layout) - 2)
        spacer_item = layout.itemAt(len(layout) - 1)
        layout.removeItem(button_item)
        layout.removeItem(spacer_item)
        layout.addWidget(entry)
        layout.addItem(button_item)
        layout.addItem(spacer_item)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.matches(QtGui.QKeySequence.Delete):
            self.delete_selected_skills()

    def delete_selected_skills(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        advanced_skills = [layout.itemAt(i).widget() for i in range(len(layout))
                           if type(layout.itemAt(i).widget()) == AdvancedSkillEntryUI]
        for skill in advanced_skills:
            if skill.selected:
                layout.removeWidget(skill)
                skill_name = skill.ui.advanced_skill_label.text()
                specialization = skill.ui.specialization_label.text()
                del self.advanced_skills[skill_name][specialization]

    def save_character(self):
        attributes = {attribute: spin_box.value() for attribute, spin_box in self.attributes.items()}
        basic_skills = {skill: spin_box.value() for skill, spin_box in self.basic_skills.items()}
        advanced_skills = {}
        for advanced_skill in self.advanced_skills:
            advanced_skills[advanced_skill] = {spec: spin_box.value() for spec, spin_box
                                               in self.advanced_skills[advanced_skill].items()}
        misc = {skill: spin_box.value() for skill, spin_box in self.misc.items()}

        name = self.ui.lineEdit_2.text()
        character_data = {"name": name, "attributes": attributes, "basic_skills": basic_skills,
                          "advanced_skills": advanced_skills, "miscellaneous": misc}
        with open(f"characters/{name}_char.json", "w") as file:
            json.dump(character_data, file, indent=4)

    def load_character(self, data):
        self.ui.lineEdit_2.setText(data["name"])
        attributes = data["attributes"]
        basic_skills = data["basic_skills"]
        misc = data["miscellaneous"]
        for attribute, spin_box in self.attributes.items():
            spin_box.setValue(attributes[attribute])
        for basic, spin_box in self.basic_skills.items():
            spin_box.setValue(basic_skills[basic])
        for m, spin_box in self.misc.items():
            spin_box.setValue(misc[m])

        advanced_skills = data["advanced_skills"]
        for advanced_skill, skill_dict in advanced_skills.items():
            for specialization, value in skill_dict.items():
                self.add_advanced_skill_entry(advanced_skill, specialization, value)


class AdvancedSkillEntryUI(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = AdvancedSkillEntry()
        self.ui.setupUi(self)
        self.selected = False

    def set_text(self, skill, specialization):
        self.ui.advanced_skill_label.setText(skill)
        self.ui.specialization_label.setText(specialization)

    def toggle_selection(self):
        self.selected = not self.selected
        if self.selected:
            self.ui.frame.setFrameStyle(qtw.QFrame.Panel)
        else:
            self.ui.frame.setFrameStyle(qtw.QFrame.StyledPanel)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == 2:
            self.toggle_selection()
