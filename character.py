import pickle
import json
from typing import *


class Character:
    def __init__(self) -> None:
        self.name = ""

        self.attributes = {
            'Weapon Skill': 0,
            'Ballistic Skill': 0,
            'Strength': 0,
            'Toughness': 0,
            'Initiative': 0,
            'Agility': 0,
            'Dexterity': 0,
            'Intelligence': 0,
            'Willpower': 0,
            'Fellowship': 0
        }

        self.basic_skills = {
            'Art': 0,
            'Athletics': 0,
            'Bribery': 0,
            'Charm': 0,
            'Animal': 0,
            'Climb': 0,
            'Cool': 0,
            'Consume': 0,
            'Alcohol': 0,
            'Dodge': 0,
            'Drive': 0,
            'Endurance': 0,
            'Entertain': 0,
            'Gamble': 0,
            'Gossip': 0,
            'Haggle': 0,
            'Intimidate': 0,
            'Intuition': 0,
            'Leadership': 0,
            'Melee': 0,
            'Navigation': 0,
            'Outdoor Survival': 0,
            'Perception': 0,
            'Ride': 0,
            'Row': 0,
            'Stealth': 0,
        }

        self.advanced_skills = {

        }

        self.advantage: int = 0
        self.health: int = 0
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


