import pickle


class Character:
    def __init__(self) -> None:
        self.name = ""

        self.attributes = {
            "Walka wręcz": 50,
            "Umiejętności strzeleckie": 50,
            "Siła": 0,
            "Wytrzymałość": 0,
            "Inicjatywa": 0,
            "Zwinność": 0,
            "Zręcznośc": 0,
            "Inteligencja": 0,
            "Siła woli": 0,
            "Ogłada": 0
        }

        self.basic_skills = {
            'Atletyka': 0,
            'Broń Biała': 0,
            'Charyzma': 0,
            'Dowodzenie': 0,
            'Hazard': 0,
            'Intuicja': 0,
            'Jeździectwo': 0,
            'Mocna Głowa': 0,
            'Nawigacja': 0,
            'Odporność': 0,
            'Opanowanie': 0,
            'Oswajanie': 0,
            'Percepcja': 0,
            'Plotkowanie': 0,
            'Powożenie': 0,
            'Przekupstwo': 0,
            'Skradanie': 0,
            'Sztuka Przetrwania': 0,
            'Targowanie': 0,
            'Unik': 0,
            'Wioślarstwo': 0,
            'Wspinaczka': 0,
            'Występy': 0,
            'Zastraszanie': 0
        }

        self.advanced_skills = {

        }

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        all_skills = {**self.attributes, **self.basic_skills, **self.advanced_skills}
        if item in all_skills:
            return all_skills[item]
        else:
            raise KeyError(f"Not available skill: {item}")


    def save_character(self):
        with open(f"characters/{self.name}.py", 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_character(name):
        with open(f"characters/{name}.py", 'rb') as file:
            return pickle.load(file)


