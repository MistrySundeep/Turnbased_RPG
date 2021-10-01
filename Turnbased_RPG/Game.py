# This holds the logic for the game and characters
import sys
import time
from Engine import *
from random import randint
import os
import pygame


def create_character():
    song_choice = ["Enchanted Ballad", "Orchestra of Battle", "Soothing Rhythm"]
    while True:
        print("Welcome to the Arena!\n")
        class_choice = input("Choose your class: A) Mage. B) Warrior. C) Bard. [A/B/C]? ")
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
            f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Intelligence: {player.int}\n ")

    elif class_choice == "B":
        print("You have chosen the Warrior class!")
        name = input("Enter your characters name: ")
        enrage_roll = randint(1, 12) * 7
        player = Warrior(name, 150, 150, enrage_roll)
        print(f"Welcome to the fight {player.name}")
        print(
            f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Intelligence: {player.enrage}\n ")

    else:
        print("You have chosen the Bard class!")
        name = input("Enter your characters name: ")
        song = input("Choose a song: \n\t A) Enchanted Ballad: Raises int of Mages in party, \n\t B) Orchestra of "
                     "Battle: Raises enrage of Warriors in your party. \n\t C) Soothing Rhythm: Removes de-buffs from "
                     "a party member. \n\n[A/B/C]? ")
        if song == "A":
            player = Bard(name, 120, 120, song_choice[0])
            print(f"Welcome to the fight {player.name}")
            print(
                f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Intelligence: {player.song}\n ")

        elif song == "B":
            player = Bard(name, 120, 120, song_choice[1])
            print(f"Welcome to the fight {player.name}")
            print(
                f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Intelligence: {player.song}\n ")

        else:
            player = Bard(name, 120, 120, song_choice[2])
            print(f"Welcome to the fight {player.name}")
            print(
                f"Here are your stats: \n \t-name: {player.name}\n \t-HP: {player.max_hp}\n \t-Intelligence: {player.song}\n ")

    return player


def load_character():
    if not os.path.exists(os.path.expanduser("~/Documents/Turnbased_RPG_save/save.ini")):
        print("FILE DOES NOT EXIST")
    else:
        save_file = open(os.path.expanduser("~/Documents/Turnbased_RPG_save/save.ini"), "r")
        load_properties = set()
        lines = save_file.readlines()
        for line in lines:
            parts = line.split("=")
            for _ in parts:
                load_properties.add(parts[1].strip())
        load_list = list(load_properties)
        load_list.sort()

        if load_list.__contains__("Mage"):
            load_list.pop(3)
            loaded_class = Mage(load_list[2], int(load_list[0]), int(load_list[0]), int(load_list[1]))
            print("CHARACTER LOADED SUCCESSFULLY\n")
            load_list.clear()
            if load_list.__len__() == 0:
                print("LIST CLEAR\n")

        elif load_list.__contains__("Warrior"):
            load_list.pop(3)
            loaded_class = Warrior(load_list[2], int(load_list[0]), int(load_list[0]), int(load_list[1]))
            print("CHARACTER LOADED SUCCESSFULLY\n")
            load_list.clear()
            if load_list.__len__() == 0:
                print("LIST CLEAR\n")

        else:
            load_list.pop(3)
            loaded_class = Bard(load_list[2], int(load_list[0]), int(load_list[0]), (load_list[1]))
            print("CHARACTER LOADED SUCCESSFULLY\n")
            load_list.clear()
            if load_list.__len__() == 0:
                print("LIST CLEAR\n")

    return loaded_class


def save_character(player_class):
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
            save_file.close()
            print("CHARACTER SAVED SUCCESSFULLY\n")

        elif type(player_class) == Warrior:
            save_file.write("Class=Warrior\n")
            save_file.write(f"Name={player_class.name}\n")
            save_file.write(f"HP={player_class.hp}\n")
            save_file.write(f"Max_HP={player_class.max_hp}\n")
            save_file.write(f"Enrage={player_class.enrage}\n")
            save_file.close()
            print("CHARACTER SAVED SUCCESSFULLY\n")

        else:
            save_file.write("Class=Bard\n")
            save_file.write(f"Name={player_class.name}\n")
            save_file.write(f"HP={player_class.hp}\n")
            save_file.write(f"Max_HP={player_class.max_hp}\n")
            save_file.write(f"Song={player_class.song}\n")
            save_file.close()
            print("CHARACTER SAVED SUCCESSFULLY\n")


def slow_print(title):
    for letter in title:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


