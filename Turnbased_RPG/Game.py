# This holds the logic for the game and characters
import sys
import time
from pyfiglet import Figlet
from Engine import *
from random import randint
import os


# Prompts the user to create a character from the 3 different class types: Warrior, Mage and Bard
def create_character():
    song_choice = ["Enchanted Ballad", "Orchestra of Battle", "Soothing Rhythm"]
    while True:
        print("Welcome to The Arena!\n")
        class_choice = input("Choose your class: A) Mage. B) Warrior. C) Bard. \n\n[A/B/C]? ")
        if class_choice in ["A", "B", "C"]:
            break
        else:
            print("That was an invalid choice, try again please")

    if class_choice == "A":
        print("You have chosen the Mage class!\n")
        name = input("Enter your characters name: ")
        int_roll = randint(1, 12) * 5 + 10
        player = Mage(name, 75, 75, int_roll)
        print(f"Welcome to the fight {player.name}")
        print(
            f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Intelligence: {player.int}\n "
            f"\t-XP: {player.xp}\n \t-Level: {player.level}\n")

    elif class_choice == "B":
        print("You have chosen the Warrior class!")
        name = input("Enter your characters name: ")
        resolve_roll = randint(1, 12) * 7
        player = Warrior(name, 150, 150, resolve_roll)
        print(f"Welcome to the fight {player.name}")
        print(
            f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Resolve: {player.resolve}\n "
            f"\t-XP: {player.xp}\n \t-Level: {player.level}\n")

    else:
        print("You have chosen the Bard class!")
        name = input("Enter your characters name: ")
        song = input("Choose a song: \n\t A) Enchanted Ballad: Raises int of Mages in party, \n\t B) Orchestra of "
                     "Battle: Raises enrage of Warriors in your party. \n\t C) Soothing Rhythm: Removes de-buffs from "
                     "a party member. \n\n[A/B/C]? ")

        if song == "A":
            player = Bard(name, 110, 110, song_choice[0])
            print(f"Welcome to the fight {player.name}")
            print(
                f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Song {player.song}\n "
                f"\t-XP: {player.xp}\n \t-Level: {player.level}\n")

        elif song == "B":
            player = Bard(name, 120, 120, song_choice[1])
            print(f"Welcome to the fight {player.name}")
            print(
                f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Song: {player.song}\n "
                f"\t-XP: {player.xp}\n \t-Level: {player.level}\n")

        else:
            player = Bard(name, 120, 120, song_choice[2])
            print(f"Welcome to the fight {player.name}")
            print(
                f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Song: {player.song}\n "
                f"\t-XP: {player.xp}\n \t-Level: {player.level}\n")

    return player


# Saves the users character, run after character creation
def save_character(player_class, player_weapon):
    if not os.path.exists(os.path.expanduser("~/Documents/Turnbased_RPG_save/")):
        os.makedirs(os.path.expanduser("~/Documents/Turnbased_RPG_save/"))
    else:
        save_file = open(os.path.expanduser("~/Documents/Turnbased_RPG_save/save.ini"), "w+")
        save_file.truncate()

        if type(player_class) == Mage:
            save_file.write("Class=Mage\n")
            save_file.write(f"Name={player_class.name}\n")
            save_file.write(f"HP={player_class.hp}\n")
            save_file.write(f"Max_HP={player_class.max_hp}\n")
            save_file.write(f"Intelligence={player_class.int}\n")
            save_file.write(f"XP={player_class.xp}\n")
            save_file.write(f"XP={player_class.level}\n")
            save_file.write(f"\n")
            save_file.write(f"Weapon=Runic Wand\n")
            save_file.write(f"Name={player_weapon.name}\n")
            save_file.write(f"Name={player_weapon.damage_type}\n")
            save_file.write(f"Name={player_weapon.damage_stat}\n")

            save_file.close()
            print("CHARACTER SAVED SUCCESSFULLY\n")

        elif type(player_class) == Warrior:
            save_file.write("Class=Warrior\n")
            save_file.write(f"Name={player_class.name}\n")
            save_file.write(f"HP={player_class.hp}\n")
            save_file.write(f"Max_HP={player_class.max_hp}\n")
            save_file.write(f"Enrage={player_class.resolve}\n")
            save_file.write(f"XP={player_class.xp}\n")
            save_file.write(f"XP={player_class.level}\n")
            save_file.write(f"\n")
            save_file.write(f"Weapon=Great Axe\n")
            save_file.write(f"Name={player_weapon.name}\n")
            save_file.write(f"Name={player_weapon.damage_type}\n")
            save_file.write(f"Name={player_weapon.damage_stat}\n")

            save_file.close()
            print("CHARACTER SAVED SUCCESSFULLY\n")

        elif player_class == type(Bard):
            save_file.write("Class=Bard\n")
            save_file.write(f"Name={player_class.name}\n")
            save_file.write(f"HP={player_class.hp}\n")
            save_file.write(f"Max_HP={player_class.max_hp}\n")
            save_file.write(f"Song={player_class.song}\n")
            save_file.write(f"XP={player_class.xp}\n")
            save_file.write(f"XP={player_class.level}\n")
            save_file.write(f"\n")
            save_file.write(f"Weapon=Sharpshooter\n")
            save_file.write(f"Name={player_weapon.name}\n")
            save_file.write(f"Name={player_weapon.damage_type}\n")
            save_file.write(f"Name={player_weapon.damage_stat}\n")
            save_file.close()
            print("CHARACTER SAVED SUCCESSFULLY\n")


def create_weapon(player):
    if type(player) == Mage:
        player_weapon = Wand("Magik Stik", "magic", 12)
        print(
            f"Here are your weapon stats:\n \tName: {player_weapon.name}\n \tDamage Type: {player_weapon.damage_type}\n "
            f"\tDamage Stats: {player_weapon.damage_stat}\n")
        return player_weapon

    elif type(player) == Warrior:
        player_weapon = Axe("Great Axe", "physical", 15)
        print(
            f"Here are your weapon stats:\n \tName: {player_weapon.name}\n \tDamage Type: {player_weapon.damage_type}\n "
            f"\tDamage Stats: {player_weapon.damage_stat}\n")
        return player_weapon

    elif type(player) == Bard:
        player_weapon = Bow("Sharpshooter", "physical", 10)
        print(
            f"Here are your weapon stats:\n \tName: {player_weapon.name}\n \tDamage Type: {player_weapon.damage_type}\n "
            f"\tDamage Stat: {player_weapon.damage_stat}\n")
        return player_weapon


# Prints text to console at a slower speed to give the feeling of a game
# Possibly increase text speed?
def slow_print(title):
    for letter in title:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


# Prints game start title
def create_title(text):
    banner = Figlet(font="epic")
    print(banner.renderText(text))


# Opens a text file explaining the mechanics of the game to the user
def open_help():
    os.startfile("help.txt")


# Generate a random enemy
def create_mob_hp():
    hp = []
    for i in range(1, 7):
        hp.insert(i, (i * 30) + 20)
    return hp


def create_mob_armour():
    armour = []
    for i in range(1, 7):
        armour.insert(i, (i * 25) + 50)
    return armour


def create_mob_enrage():
    enrage = []
    for i in range(1, 7):
        enrage.append(i)
    return enrage


def create_mob():
    name = ['Goblin', 'Troll']
    hp = create_mob_hp()
    armour = create_mob_armour()
    enrage = create_mob_enrage()

    created_mob = []

    for i in range(0, 6):
        class_choice = randint(0, 1)
        if class_choice == 0:
            mob = Goblin(name[0], hp[0], hp[0], enrage[0])
            hp.pop(0)
            enrage.pop(0)
            created_mob.insert(i, mob)
        else:
            mob = Troll(name[1], hp[0], hp[0], armour[0])
            hp.pop(0)
            armour.pop()
            created_mob.insert(i, mob)

    return created_mob


def player_attack(player, enemy, weapon):
    # Calculate damage
    damage_calc = player.damage + weapon.damage_stat
    round(damage_calc, 0)

    # Calculate hit chance: 1 - 6. 1 is the least amount of damage 6 is max
    hit_multiplier = randint(1, 6)
    damage_calc = (damage_calc / 6) * hit_multiplier
    round(damage_calc, 0)

    # Update update enemy hp
    enemy.hp = enemy.hp - damage_calc
    print(f"You roll {hit_multiplier}, you hit {enemy.name} for {damage_calc}! It has {enemy.hp} left")

