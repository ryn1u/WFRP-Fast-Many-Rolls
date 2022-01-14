import pickle
import json
from typing import *


class Character:
    def __init__(self) -> None:
        from utils import BASIC_SKILLS, ATTRIBUTES

        self.name = ""

        self.attributes = {attribute: 0 for attribute in ATTRIBUTES}

        self.basic_skills = {basic: 0 for basic in BASIC_SKILLS}

        self.advanced_skills = {

        }
        self._all_skills = {**self.attributes, **self.basic_skills, **self.advanced_skills}

        self.advantage: int = 0
        self.health: int = 0
        self.modifiers: Dict[str, int] = {

        }

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        if item in self._all_skills:
            return self._all_skills[item]
        else:
            raise KeyError(f"Not available skill: {item}")

    def __iter__(self):
        yield "name", self.name
        yield "attributes", self.attributes
        yield "basic skills", self.basic_skills
        yield "advanced skills", self.advanced_skills
        yield "advantage", self.advantage
        yield "health", self.health
        yield "modifiers", self.modifiers

    def to_json(self):
        return json.dumps(dict(self), indent=4)

    @staticmethod
    def from_json(json_string):
        char = Character()
        char.name = json_string['name']
        char.attributes = json_string['attributes']
        char.basic_skills = json_string['basic_skills']
        char.advanced_skills = json_string['advanced_skills']
        char.advantage = json_string['advantage']
        char.health = json_string['health']
        char.modifiers = json_string['modifiers']
        return char

    def save_character(self):
        with open(f"characters/{self.name}.py", 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_character(name):
        with open(f"characters/{name}.py", 'rb') as file:
            return pickle.load(file)


