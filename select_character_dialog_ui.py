from qt_ui.select_character_dialog import Ui_Form
from PyQt5 import QtWidgets as qtw
import os
import json


class SelectCharacterDialogUI(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super(SelectCharacterDialogUI, self).__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.selected_event = self.ui.pushButton.clicked
        self.selected_character = None

        self.characters = self.get_characters_list()
        self.ui.comboBox.addItems([c['name'] for c in self.characters])
        self.ui.comboBox.currentTextChanged.connect(self.set_selected_character)
        self.set_selected_character()

    def set_selected_character(self):
        for c in self.characters:
            if c['name'] == self.ui.comboBox.currentText():
                self.selected_character = c

    def get_characters_list(self):
        files = os.listdir("characters/")
        characters = list()
        for file in files:
            if 'char.json' in file:
                path = os.path.join("characters", file)
                with open(path, 'r') as json_file:
                    characters.append(json.load(json_file))
        return characters
