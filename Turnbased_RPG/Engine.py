# Classes for player characters and enemy characters
class Character:
    """ Defines a basic character object"""

    def __init__(self, name: str, hp: int, max_hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.xp = 0
        self.level = 1


class Warrior(Character):
    """ Defines a Warrior object, which is a type of character. Special trait is resolve """

    def __init__(self, name: str, hp: int, max_hp: int, resolve: int):
        Character.__init__(self, name, hp, max_hp)
        self.resolve = resolve
        # Max base damage 11 @ lvl 1
        self.damage = (self.level * 5) + 6
        self.shield = 5


class Mage(Character):
    """ Defines a Mage object, which is a type of character. Special trait is intelligence """

    def __init__(self, name: str, hp: int, max_hp: int, intelligence: int):
        Character.__init__(self, name, hp, max_hp)
        self.int = intelligence
        # Max base damage 11 @ lvl 1
        self.damage = (self.level * 5) + 10


class Bard(Character):
    """ Defines a Mage object, which is a type of character. Special trait is song """

    def __init__(self, name: str, hp: int, max_hp: int, song: str):
        Character.__init__(self, name, hp, max_hp)
        self.song = song
        self.damage = (self.level * 5) + 7


class Goblin(Character):
    """ Defines a Goblin Character, which is a type of character. Special trait is enrage """

    def __init__(self, name: str, hp: int, max_hp: int, enrage: int):
        Character.__init__(self, name, hp, max_hp)
        self.enrage = enrage
        self.damage = 10


class Troll(Character):
    """  Defines a Troll Character, which is a type of character. Special trait is armour"""

    def __init__(self, name: str, hp: int, max_hp: int, armour: float):
        Character.__init__(self, name, hp, max_hp)
        self.armour = armour
        self.damage = 10
        self.xp = 10


class Boss(Character):
    """ Defines a Boss character, which is a type of character. Special trait is corruption """

    def __init__(self, name: str, hp: int, max_hp: int, corruption: int):
        Character.__init__(self, name, hp, max_hp)
        self.corruption = corruption
        self.damage = 0.0
        self.xp = 20


class Weapon:
    def __init__(self, name: str, damage_type: str):
        self.name = name
        self.damage_type = damage_type


class Axe(Weapon):
    def __init__(self, name: str, damage_type: str, damage_stat: int):
        Weapon.__init__(self, name, damage_type)
        self.damage_stat = damage_stat


class Bow(Weapon):
    def __init__(self, name: str, damage_type: str, damage_stat: int):
        Weapon.__init__(self, name, damage_type)
        self.damage_stat = damage_stat


class Wand(Weapon):
    def __init__(self, name: str, damage_type: str, damage_stat: int):
        Weapon.__init__(self, name, damage_type)
        self.damage_stat = damage_stat
