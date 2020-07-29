from room import Room
from item import Item
from character import  Enemy, Hero
from rpginfo import RPGInfo
import time


###########################################################################
####                    Helper Functions                               ####
###########################################################################

def set_rooms_attributes(gate_way, chapel, library, drawing_room, court_yard, dining_hall, bed_room, ball_room,
                         kitchen):
    """Setting the attributes of each room"""
    # Making the rooms

    gate_way.name = "Gate Way"
    chapel.name = "Chapel"
    library.name = "Library"
    drawing_room.name = "Drawing Room"
    court_yard.name = "Court Yard"
    dining_hall.name = "Dining Hall"
    bed_room.name = "Bed Room"
    ball_room.name = "Ballroom"
    kitchen.name = "Kitchen"

    # Giving each room a description
    gate_way.description = "A heavily fortified gateway of a castle"
    chapel.description = "A Haunted Chapel, filled with dark energy, everything is.\nThe only thing left here is a cross hanging in the center of the chapel"
    library.description = "Old Library. A musty room, filled with tomes old and new. \nThe pungent aroma of book mold fills the air."
    drawing_room.description = "A room filled with a lot of paintings."
    court_yard.description = "A yard filled with tombstones everywhere"
    dining_hall.description = "A large room with ornate golden decorations on each wall"
    bed_room.description = "A dirty room with the smell of blood everywhere"
    ball_room.description = "A vast room with a shiny wooden floor; huge candlesticks guard the entrance"
    kitchen.description = "A dank and dirty room buzzing with flies"

    # Linking the rooms together
    gate_way.link_room(chapel, "east")
    gate_way.link_room(drawing_room, "south")

    chapel.link_room(gate_way, "west")
    chapel.link_room(library, "east")
    chapel.link_room(court_yard, "south")

    library.link_room(chapel, "west")
    library.link_room(dining_hall, "south")

    drawing_room.link_room(gate_way, "north")
    drawing_room.link_room(court_yard, "east")
    drawing_room.link_room(bed_room, "south")

    court_yard.link_room(chapel, "north")
    court_yard.link_room(dining_hall, "east")
    court_yard.link_room(ball_room, "south")
    court_yard.link_room(drawing_room, "west")

    dining_hall.link_room(library, "north")
    dining_hall.link_room(court_yard, "west")
    dining_hall.link_room(kitchen, "south")

    bed_room.link_room(drawing_room, "north")
    bed_room.link_room(ball_room, "east")

    ball_room.link_room(court_yard, "north")
    ball_room.link_room(kitchen, "east")
    ball_room.link_room(bed_room, "west")

    kitchen.link_room(dining_hall, "north")
    kitchen.link_room(ball_room, "west")


def main_character_creation():
    """ Create a Character"""
    char_name = input("Please enter the name of your character: ")
    character = Hero(char_name)
    return character


def enemies_creation():
    zombie1 = Enemy("Zombie1", "A smelly zombie")
    zombie2 = Enemy("Zombie2", "A smelly zombie")

    skeleton1 = Enemy("Skeleton1", "A skeleton")
    skeleton2 = Enemy("Skeleton2", "A skeleton")
    skeleton3 = Enemy("Skeleton3", "A skeleton")
    skeleton4 = Enemy("Skeleton4", "A skeleton")
    skeleton5 = Enemy("Skeleton5", "A skeleton")

    bats1 = Enemy("Bats1", "Bats")
    bats2 = Enemy("Bats1", "Bats")
    bats3 = Enemy("Bats1", "Bats")

    vampire1 = Enemy("Vampire1", "A Vampire")
    vampire2 = Enemy("Vampire2", "A Vampire")
    vampire3 = Enemy("Vampire3", "A Vampire")
    vampire4 = Enemy("Vampire4", "A Vampire")
    vampire5 = Enemy("Vampire5", "A Vampire")
    vampire6 = Enemy("Vampire6", "A Vampire")

    final_boss = Enemy("Giant Spider", "Final Boss")

    zombie1.health = 50
    zombie2.health = 50

    skeleton1.health = 25
    skeleton2.health = 25
    skeleton3.health = 25
    skeleton4.health = 25
    skeleton5.health = 25

    bats1.health = 35
    bats2.health = 35
    bats3.health = 35

    vampire1.health = 75
    vampire2.health = 75
    vampire3.health = 75
    vampire4.health = 75
    vampire5.health = 75
    vampire6.health = 75

    final_boss.health = 100

    court_yard.character.append(skeleton1)
    court_yard.character.append(skeleton2)
    court_yard.character.append(skeleton3)

    ball_room.character.append(bats1)
    ball_room.character.append(bats2)
    ball_room.character.append(skeleton4)

    kitchen.character.append(skeleton1)
    kitchen.character.append(vampire1)

    dining_hall.character.append(vampire2)
    dining_hall.character.append(vampire3)
    dining_hall.character.append(vampire4)

    library.character.append(zombie1)
    library.character.append(zombie2)

    ball_room.character.append(vampire5)
    ball_room.character.append(vampire6)

    drawing_room.character.append(skeleton5)

    chapel.character.append(bats3)

    bed_room.character.append(final_boss)


def items_creation():

    holy_sword = Item("Holy Sword", 75)
    shotgun = Item("Shotgun", 50)
    katana = Item("Katana", 50)
    lighting_spell = Item("Lighting Spell", 100)

    chapel.item = holy_sword
    kitchen.item = shotgun
    dining_hall.item = katana
    library.item = lighting_spell


    holy_sword.description = "A sword forged by God to fight against the Darkness\n"
    shotgun.description = "A gun with powerful damage\n"
    katana.description = "A Japanese sword that can cut down almost anything\n"
    lighting_spell.description = "An ancient spell that can cast power lighting from the sky\n"

def game_over(character):
    if character.health <= 0:
        print("You died\nGame OVer.")
        RPGInfo.credits()
        exit(0)

def win_check():
    if not bed_room.character:
        print("Congratulation you win")
        RPGInfo.credits()
        quit()
 



###########################################################################
####                     Functions For Game Interaction                ####
###########################################################################


def welcome_msg(hero):
    '''
    A msg to welcome to user to the game and displaying the game info
    :return: none
    '''
    spooky_castle = RPGInfo("The Spooky Castle")
    spooky_castle.char = hero
    spooky_castle.welcome()
    RPGInfo.info()


def help_command():
    print("\nPlease type in what command do you need help with")
    print("Commands: north, south ,east ,west, pick up, backpack, fight")
    print("To exit type: 'exit'\n")
    commands = ["north", "south", "east", "est", "pick up","backpack", "fight"]
    valid = False
    while not valid:
        command = input("help> ").lower().strip()
        if command in commands:
            print("\n____________________________________________")
            if command == "north":
                print("\nUse this command to move: 'North'")
            elif command == "south":
                print("\nUse this command to move: 'South'")
            elif command == "east":
                print("\nUse this command to move: 'East'")
            elif command == "west":
                print("\nUse this command to move: 'West'")
            elif command == "pick up":
                print("\nUse this command to: 'Pick up an item'")
            elif command == "backpack":
                print("\nDisplay all the items in your backpack")
            elif command == "fight":
                print("\nUse this command to: Fight the Enemy")
            elif command == "hp":
                print("\nYou this command to see current health")
            print("____________________________________________")
            valid = True
        elif command == 'exit':
            break
        else:
            print("Invalid command, try again\n")

def item_fight_with():
    """
    Let the payer pick a weapon from their backpack or use their fists if backpack is empty
    :return: weapon to use
    """
    fists = Item("Fists", 10)
    fists.description = "Your powerful fists\n"

    if hero.backpack:
        valid = False
        while not valid:
            print("\n\nHere are the items available in your backpack")
            hero.backpack_listing()
            item = input("Choose your weapon> ")
            my_item = hero.backpack_item(item)
            if my_item:
                return my_item
            else:
                print("\nInvalid item name try again\n")
    else:
        print("Backpack is empty")
        return fists

def player_fight_turn(room):
    """
    Do all the fighting for the player
    :param room: current room the player is in
    :return:
    """
    valid = False
    while not valid:
        print("\nWhich character do you want to fight")
        char_to_fight = input("> ")
        item = item_fight_with()
        for inhabitant in room.character:
            if char_to_fight == inhabitant.name:
                valid = True
                print("-------------------------------------------")
                time.sleep(0.5)
                hero.fight(inhabitant, item.damage)
                time.sleep(1)
                if inhabitant.health <= 0:
                    time.sleep(1)
                    print(f"\n{hero.name.upper()} have killed {inhabitant.name.upper()} ")
                    time.sleep(1)
                    room.character.remove(inhabitant)
                break
        else:
            print("\nThere no character with that name. Try again\n")

def comp_fight_turn(room):
    """
    AI turn to fight
    :param room: current room
    :return: none
    """
    for inhabitant in room.character:
        time.sleep(1)
        print(f"\n{inhabitant.name.upper()} turn to attack\n")
        inhabitant.fight(hero, inhabitant.damage)
        game_over(hero)

def fight(room):
    '''char = input("Which enemy do you want to fight ")
    ene = room.get_specific_character(char)
    ene.describe()'''
    while room.has_enemy():
        room.character_listing()
        player_fight_turn(room)
        comp_fight_turn(room)
        if room.character is None:
            break
        print("-------------------------------------------")
        time.sleep(0.5)


if __name__ == "__main__":
    # Creating instances of Room class
    gate_way = Room()
    chapel = Room()
    library = Room()
    drawing_room = Room()
    court_yard = Room()
    dining_hall = Room()
    bed_room = Room()
    ball_room = Room()
    kitchen = Room()

    set_rooms_attributes(gate_way, chapel, library, drawing_room, court_yard, dining_hall, bed_room, ball_room, kitchen)

    # The rooms
    rooms = [gate_way, chapel, library, drawing_room, court_yard, dining_hall, bed_room, ball_room, kitchen]

    # Main Character
    hero = main_character_creation()

    # Create enemies for the game
    enemies_creation()

    # Create items for the game
    items_creation()

    # Setting the current room
    #current_room = gate_way
    current_room = gate_way

    # Start Game
    welcome_msg(hero)

    while hero.health > 0:
        win_check()
        print("\n-------------------------")
        print("You are Here:", end=" ")
        current_room.get_details()

        # Display the current room item
        if current_room.item is not None:
            current_room.item.describe()

        # Display the current room enemies
        current_room.character_listing()

        print("Commands to use: north, south ,east ,west, pick up,help, backpack, fight, hp")

        valid = False
        while not valid:
            command = input("> ").lower().strip()
            print("\n\n")
            if command == "help":
                help_command()
                valid = True
            elif command == "north" or command == "south" or command == "east" or command == "west":
                current_room = current_room.move(command)
                valid = True
            elif command == "pick up" and current_room.item is not None:
                print(f"\nYou have picked up: {current_room.item}")
                hero.backpack_insert(current_room.item)
                current_room.remove_item()
                valid = True
            elif command == "backpack":
                hero.backpack_listing()
                valid = True
            elif command == "fight":
                if current_room.character:
                    print("Fight")
                    fight(current_room)
                    valid = True
                else:
                    print("There's no one to fight with")
                    break
            elif command == "hp":
                print(f"\nYour hp is: {hero.health}\n")
                valid = True
            else:
                print("Invalid command try again")
