from Game import *


# First Intro Game Title (ASCII)
# Ask user to start new or load game
# Add help option/command that gives the user info on the different stats and how they work
create_title("The Arena")

slow_print("Hello Adventurer! Welcome to The Arena\n\n")
slow_print("What would you like to do: \n\t*New Game*\n\t*Help*\n\t*Quit*\n\n")
slow_print("Type start to create a character or  quit to close the game\n")

choice = True
while choice:
    menu_choice = input("Your choice: ")
    if menu_choice == "quit":
        quit(0)

    if menu_choice == "start":
        # create new character function
        player = create_character()
        player_weapon = create_weapon(player)
        save_character(player, player_weapon)
        choice = False

    elif menu_choice == "help":
        # EDIT THIS TEXT FILE WITH GAME MECHANIC INFO
        open_help()
        print("\n")

# Start combat with first enemy
slow_print("GENERATING ENEMIES\n\n")
enemy = create_mob()

slow_print("The Arena is a 1v1 challenge where you fight progressively stronger opponents until you reach the final "
           "boss.\n")
slow_print("As you progress you will get stronger and wiser, with the addition of new equipment can you make it out "
           "alive?\n")
slow_print("As you enter The Arena, steel yourself adventurer for there is no turning back...\n\n")

create_title("Round 1")



