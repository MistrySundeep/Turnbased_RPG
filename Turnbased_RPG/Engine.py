

class Character:
    """ Defines a basic character object"""
    def __init__(self, name: str, hp: int, max_hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp


class Warrior(Character):
    """ Defines a Warrior object, which is a type of character. Special triat is enrage """
    def __init__(self, name: str, hp: int, max_hp: int, enrage: int):
        Character.__init__(self, name, hp, max_hp)
        self.enrage = enrage


class Mage(Character):
    """ Defines a Mage object, which is a type of character. Special trait is intelligence """
    def __init__(self, name: str, hp: int, max_hp: int, intelligence: int):
        Character.__init__(self, name, hp, max_hp)
        self.int = intelligence


class Bard(Character):
    """ Defines a Mage object, which is a type of character. Special trait is song """
    def __init__(self, name: str, hp: int, max_hp: int, song: str):
        Character.__init__(self, name, hp, max_hp)
        self.song = song


class Goblin(Character):
    def __init__(self, name: str, hp: int, max_hp: int, size: float):
        Character.__init__(self, name, hp, max_hp)
        self.size = size


class Troll(Character):
    def __init__(self, name: str, hp: int, max_hp: int, armour: float):
        Character.__init__(self, name, hp, max_hp)
        self.armour = armour


class Boss(Character):
    def __init__(self, name: str, hp: int, max_hp: int, corruption: int):
        Character.__init__(self, name, hp, max_hp)
        self.corruption = corruption

