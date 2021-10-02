from Game import *

# First Intro Game Title (ASCII)
# Ask user to start new or load game
# Add help option/command that gives the user info on the different stats and how they work
create_title()
slow_print("Hello Adventurer! Welcome to The Arena\n\n")
slow_print("What would you like to do: \n\t*New Game*\n\t*Load Game*\n\t*Help*\n\n")
slow_print("Press 1, 2 or 3 for your choice\n")
menu_choice = int(input("Your choice: "))

if menu_choice == 1:
    # create new character function
    create_character()
elif menu_choice == 2:
    # load character function
    load_character()
else:
    # Open a txt file that explains the mechanics of the game TODO
    pass