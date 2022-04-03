from qt_ui.add_advanced_skill_dialog import Ui_MainWindow as AddAdvancedSkill
from PyQt5 import QtWidgets as qtw
from utils import ADVANCED_SKILLS


class AddAdvancedSkillUI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AddAdvancedSkillUI, self).__init__(*args, **kwargs)
        self.ui = AddAdvancedSkill()
        self.ui.setupUi(self)

        # fill advanced skill list
        self.ui.advnaced_skill_box.addItems(ADVANCED_SKILLS)

        # create OK button function
        #       check if something in specialization
        #       add advnaced skill to table

