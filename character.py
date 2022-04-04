import pickle
import json
from typing import *


class Character:
    def __init__(self) -> None:
        from utils import BASIC_SKILLS, ATTRIBUTES, MISCELLANEOUS

        self.name = ""

        self.attributes = {attribute: 0 for attribute in ATTRIBUTES}

        self.basic_skills = {basic: 0 for basic in BASIC_SKILLS}

        self.advanced_skills = {

        }

        self.miscellaneous = {misc: 0 for misc in MISCELLANEOUS}

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        all_skills = {**self.attributes, **self.basic_skills, **self.advanced_skills}
        if item in all_skills:
            return all_skills[item]
        else:
            raise KeyError(f"Not available skill: {item}")

    def __setitem__(self, key, value):
        if key == "name":
            self.name = value
        elif key in self.attributes:
            self.attributes[key] = value
        elif key in self.basic_skills:
            self.basic_skills[key] = value
        elif key in self.advanced_skills:
            self.advanced_skills[key] = value
        elif key in self.miscellaneous:
            self.miscellaneous[key] = value

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
        for misc in data['miscellaneous']:
            character[misc] = data['miscellaneous'][misc]
        return character

    def to_dict(self):
        return {
            "name": self.name,
            "attributes": self.attributes,
            "basic_skills": self.basic_skills,
            "advanced_skills": self.advanced_skills,
            "miscellaneous": self.miscellaneous
        }

    def __iter__(self):
        yield "name", self.name
        for attr in self.attributes:
            yield tuple(attr)
        for basic in self.basic_skills:
            yield tuple(basic)
        for adv in self.advanced_skills:
            yield tuple(adv)
        for misc in self.miscellaneous:
            yield  tuple(misc)
