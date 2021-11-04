from Game import *


enemy_turn_choice = ["attack", "block"]
# First Intro Game Title (ASCII)
# Ask user to start new or load game
# Add help option/command that gives the user info on the different stats and how they work
create_title("The Arena")

slow_print("Hello Adventurer! Welcome to The Arena\n\n")
slow_print("What would you like to do: \n\t*Start*\n\t*Help*\n\t*Quit*\n\n")
slow_print("Type the option you want\n")

while True:
    menu_choice = input("Your choice: ")
    if menu_choice == "quit":
        quit(0)

    if menu_choice == "start":
        # create new character function
        player = create_character()
        player_weapon = create_weapon(player)
        save_character(player, player_weapon)
        break

    elif menu_choice == "help":
        # EDIT THIS TEXT FILE WITH GAME MECHANIC INFO
        open_help()
        print("\n")

# Start combat with first enemy
enemy_list = create_mob()


slow_print("The Arena is a 1v1 challenge where you fight progressively stronger opponents until you reach the final "
           "boss.\n")
slow_print("As you progress you will get stronger and wiser, with the addition of new equipment can you make it out "
           "alive?\n")
slow_print("As you enter The Arena, steel yourself adventurer for there is no turning back...\n\n")
create_title("Round 1")

mob1 = enemy_list.pop(0)
slow_print(f"Your first opponent enters The Arena, prepare yourself {player.name}\n")


while mob1.hp != 0 or player.hp != 0:
    if mob1.hp <= 0:
        print(f"\nYou have slain the {mob1.name}! Well done adventurer")
        player.xp += mob1.xp
        check_xp(player)
        break
    else:
        combat_choice = input("What do you want to do: \n \t*attack* \n \t*block* \n \t*s-attack*\n")
        if combat_choice == "attack":
            player_turn = player_attack(player, mob1, player_weapon)
            print(player_turn)

    if player.hp <= 0:
        print("You have been slain, your adventure ends here...")
        break
    else:
        enemy_choice = enemy_turn_choice[randint(0, 1)]
        if combat_choice == "attack":
            enemy_turn = enemy_attack(player, mob1)
            print(enemy_turn)
