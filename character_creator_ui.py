from character_creator import Ui_Form as CharacterCreator
from add_advanced_skill_dialog import Ui_MainWindow as AddAdvancedSkill
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from utils import BASIC_SKILLS, ATTRIBUTES, ADVANCED_SKILLS


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

        self.refrence = None
        self.ui.add_advanced_skill_button.clicked.connect(self.add_advanced_skill)

    def _initialize_field(self, name, field_type, num, value=0):
        text = self.ui.__getattribute__(f"{field_type}_label_{num+1}")
        spin_box = self.ui.__getattribute__(f"{field_type}_value_{num+1}")
        text.setText(name)
        spin_box.setValue(value)
        return spin_box

    def add_advanced_skill(self):
        add_advanced_skill_dialog = AddAdvancedSkillUI()
        add_advanced_skill_dialog.show()
    

class AddAdvancedSkillUI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AddAdvancedSkillUI, self).__init__(*args, **kwargs)
        self.ui = AddAdvancedSkill()
        self.ui.setupUi(self)
