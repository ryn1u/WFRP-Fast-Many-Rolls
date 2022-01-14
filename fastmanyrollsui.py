from table_entry import Ui_Form
from test_table import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


# TODO: check if character has advanced skill
class FastManyRollsUI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._load_skill_lists()

    def _load_skill_lists(self):
        from utils import ATTRIBUTES, BASIC_SKILLS, ADVANCED_SKILLS
        skills = ["", *ATTRIBUTES, *BASIC_SKILLS, *ADVANCED_SKILLS]
        self.ui.test_skill_list.addItems(skills)

