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

        self.advantage: int = 0
        self.wounds: int = 0
        self.modifiers: Dict[str, int] = {

        }

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        all_skills = {**self.attributes, **self.basic_skills, **self.advanced_skills}
        if item in all_skills:
            return all_skills[item]
        else:
            raise KeyError(f"Not available skill: {item}")

    def __setitem__(self, key, value):
        if key in self.attributes:
            self.attributes[key] = value
        elif key in self.basic_skills:
            self.basic_skills[key] = value
        elif key in self.advanced_skills:
            self.advanced_skills[key] = value
        elif key == 'Advantage':
            self.advantage = value
        elif key == 'Wounds':
            self.wounds = value

    @staticmethod
    def from_dict(data):
        character = Character()
        character.name = data["name"]
        for attr in data['attributes']:
            character[attr] = data['attributes'][attr]

        for basic in data['basic_skills']:
            character[basic] = data['basic_skills'][basic]

        for adv in data['advanced_skills']:
            character[adv] = data['advanced_skills'][adv]

        character.advantage = data['miscellaneous']['Advantage']
        character.wounds = data['miscellaneous']['Wounds']
        return character


