import json
import pickle

from qt_ui.test_table import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from character_creator_ui import CharacterCreatorUI


class MainWindowManu:
    def __init__(self, main_window, ):
        self.main_window = main_window
        self.main_window_qt = main_window.ui

        self.new_character_btn = self.main_window_qt.actionCaracterNew
        self.edit_character_btn = self.main_window_qt.actionCharacterEdit

        self.save_list_btn = self.main_window_qt.actionListSave
        self.load_list_btn = self.main_window_qt.actionListLoad

        self.character_creator: CharacterCreatorUI = None

        self.connect_buttons()

    def connect_buttons(self):
        self.new_character_btn.triggered.connect(self.open_new_character_creator)
        self.edit_character_btn.triggered.connect(self.edit_character)
        self.save_list_btn.triggered.connect(self.save_current_list)
        self.load_list_btn.triggered.connect(self.load_list)

    def open_new_character_creator(self):  # todo move to menu class
        self.character_creator = CharacterCreatorUI()
        self.character_creator.show()

    def edit_character(self):  # todo move to menu class
        filename = self.open_character_file()
        with open(filename, 'r') as file:
            data = json.load(file)
        self.character_creator = CharacterCreatorUI()
        self.character_creator.load_character(data)
        self.character_creator.show()

    def open_character_file(self):
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        file_name, _ = qtw.QFileDialog.getOpenFileName(
            self.main_window,
            "Load Character",
            "characters",
            "Json Files (*.json);;All Files (*)",
            options=options
        )
        return file_name

    def save_current_list(self):  # todo rewrite for opposing throws
        character_entries = self.main_window.table_list_ui.character_entries
        character_list = [c.character.name for c in character_entries]

        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self.main_window,
            "Save list",
            "lists",
            "Characters List (*.clst);; All Files (*)",
            options=options
        )
        if filename:
            if ".clst" not in filename:
                filename += ".clst"
            with open(filename, 'wb') as file:
                pickle.dump(character_list, file)

    def load_list(self):  # todo move to menu class
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        filename, _ = qtw.QFileDialog.getOpenFileName(self.main_window,
                                                      "Load list",
                                                      "lists",
                                                      "Characters List (*.clst);; All Files (*)",
                                                      options=options
                                                      )
        if not filename:
            return

        file = open(filename, 'rb')
        characters_list = pickle.load(file)
        file.close()

        for character_name in characters_list:
            character_file_path = "characters/" + character_name + "_char.json"
            with open(character_file_path, 'r') as file:
                char_dict = json.load(file)
                self.main_window.table_list_ui.add_character_entry(char_dict)
