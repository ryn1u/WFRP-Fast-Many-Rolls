import random
from typing import *
from character import Character

"""
I want to be able to choose create one (for normal) or two (for opposing) lists of characters, and choose what stats
are these lists rolling for. Then random number generator automatically rolls dice for all of them and calculates
PS. 

Additional options:
- Create, save, modify, copy specific characters with names.
- modifiers (for talents or status)
- advantage. Give advantage to group
- Mark crits and auto win/loss
- Create scenes (premade sets of lists that can be sotored, edited and saved, these could represent different fronts
of battle)
- character creator
- calc dmg option
"""


class FastManyRolls:
    def __init__(self):
        self.attackers: List[Character] = []
        self.defenders: List[Character] = []
        self.attacking_ability: str = ""
        self.defending_ability: str = ""

    @staticmethod
    def get_tens(x):
        return int(x / 10)

    @staticmethod
    def calculate_opposing_throw(
            attacker: Character, attacking_ability: str, defender: Character, defending_ability: str,
            block_opposing: bool = False
    ) -> Tuple[int, int, int]:
        attacking_roll = random.randint(1, 100)
        attacking_skill = attacker[attacking_ability]
        attacker_ps = FastManyRolls.get_tens(attacking_skill - attacking_roll)
        if block_opposing:
            return attacking_roll, attacker_ps, 0

        defending_roll = random.randint(1, 100)
        defending_skill = defender[defending_ability]
        defender_ps = FastManyRolls.get_tens(defending_skill - defending_roll)

        return attacking_roll, attacker_ps - defender_ps, defending_roll

    @staticmethod
    def calculate_test(character: Character, ability: str, difficulty: int) -> Tuple[int, int, int]:
        roll = random.randint(1, 100)
        skill = character[ability]
        result = skill - difficulty
        ps = FastManyRolls.get_tens(result) - FastManyRolls.get_tens(roll)
        return roll, ps, result

    def resolve_attack(self, is_ranged: bool):
        pairs = self.create_pairs()
        for pair in pairs:
            atk_roll, ps, def_roll = FastManyRolls.calculate_opposing_throw(
                pair[0], self.attacking_ability, pair[1], self.defending_ability, is_ranged
            )
            #TODO: add advantage, deal dmg, flag crits and killed
            print(f"{str(pair[0])}:\t{atk_roll}\t\t{ps}\t\t{def_roll}:\t{str(pair[1])}")

    def resolve_group_test(self, difficulty):
        results = []
        for attacker in self.attackers:
            roll, ps, result = FastManyRolls.calculate_test(attacker, self.attacking_ability, difficulty)
            test_result = "PASS" if result >= 0 else "FAIL"
            print(f"{str(attacker)}:\t{roll}\t\t{ps}\t\t{test_result}")
            results.append((roll, ps, result))
        return results

    def create_pairs(self) -> List[Tuple[Character, Character]]:
        # give each attacker a random opponent. Remove that oponent from avaible list. If you run out of defenders refill
        defenders_pool: List[int] = list(range(len(self.defenders)))
        pairs: List[Tuple[Character, Character]] = []
        for attacker in self.attackers:
            if len(defenders_pool) == 0:
                defenders_pool = list(range(len(self.defenders)))
            choice: int = random.choice(defenders_pool)
            defenders_pool.remove(choice)
            pairs.append((attacker, self.defenders[choice]))
        return pairs