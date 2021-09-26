from random import randint
import pygame


class Window:
    def __init__(self, width, height, caption, fullscreen):
        self.window = pygame.display.set_mode((width, height), fullscreen)
        pygame.display.set_caption(caption)

    def show_frame(self):
        pygame.display.flip()

    def clear(self):
        self.window.fill((0, 0, 0))


class Character:
    """ Defines a basic character object"""

    def __init__(self, name: str, hp: int, max_hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp


class Warrior(Character):
    """ Defines a Warrior object, which is a type of character. Special trait is enrage """

    def __init__(self, name: str, hp: int, max_hp: int, enrage: int):
        Character.__init__(self, name, hp, max_hp)
        self.enrage = enrage
        self.weapon_damage = randint(1, 12) * 2.5
        self.damage = 0.0

    def attack(self, warrior) -> float:
        self.damage = float(warrior.enrage + warrior.weapon_damage)
        return self.damage


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
    """ Defines a Goblin Character, which is a type of character. Special trait is size """

    def __init__(self, name: str, hp: int, max_hp: int, size: float):
        Character.__init__(self, name, hp, max_hp)
        self.size = size


class Troll(Character):
    """  Defines a Troll Character, which is a type of character. Special trait is armour"""

    def __init__(self, name: str, hp: int, max_hp: int, armour: float):
        Character.__init__(self, name, hp, max_hp)
        self.armour = armour


class Boss(Character):
    """ Defines a Boss character, which is a type of character. Special trait is corruption """

    def __init__(self, name: str, hp: int, max_hp: int, corruption: int):
        Character.__init__(self, name, hp, max_hp)
        self.corruption = corruption
