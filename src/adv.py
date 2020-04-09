from room import Room
from player import Player
from money import Money
from weapon import Weapon
from armor import Armor
import random

# Declare all the rooms

gold_outside = random.randint(1, 50)
gold_foyer = random.randint(1, 50)
gold_overlook = random.randint(1, 50)
gold_narrow = random.randint(1, 50)
gold_treasure = random.randint(100, 500)

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Money("Coins", f"A sack of {gold_outside} [Coins]", gold_outside), Weapon("Sword", "A Rusted Iron [Sword]", 5)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Money("Coins", f"A sack of {gold_foyer}[Coins]", gold_foyer), Armor("Shield", "A rusty iron [Shield].", 5)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Money("Coins", f"A sack of {gold_overlook}[Coins]", gold_overlook), Armor("Chestplate", "A rusty iron [Chestplate]", 10)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Money("Coins", f"A sack of {gold_narrow}[Coins]", gold_narrow), Armor("Helm", "A rusty iron [Helm]et", 3)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Money("Coins", f"A sack of {gold_treasure}[Coins]", gold_treasure), Armor("Boots", "A pair of moldy [Boots]", 2)]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
game = True
print(f'\n\nYou are in the {player.current_room.name}. \n {player.current_room.desc}\n')

while game == True:
    direction = input("\nPlease enter direction ([n]orth [s]outh [e]ast [w]est [search] [i]nventory [eq]uipment [st]atus [q]uit):\n")

    if direction == 'n':
        player.move(direction)

    elif direction == 'e':
        player.move(direction)

    elif direction == 's':
        player.move(direction)

    elif direction == 'w':
        player.move(direction)

    elif direction == 'search':
        interact = True
        while interact == True:
            if len(player.current_room.items) == 0:
                print("\nThere is nothing of importance")
                interact = False

            else:
                player.look()
                x = [str(x) for x in input("\nWhich loot would you like to take? ([take] [item] or [all] [none]): \n").split()]

                if len(x) == 2:
                    if x[0] != 'take':
                        print("\n***Please choose from available commands***\n")
                    else:
                        player.take(x[1])
                
                elif len(x) == 1:
                    if x[0] == 'all':
                        print("\nYou put all the items in your inventory")
                        for i in player.current_room.items:
                            if i.__class__.__name__ == "Money":
                                player.gold += i.amount
                                del player.current_room.items[0:0]
                            if i.__class__.__name__ == "Weapon":
                                player.inv.append(i)
                            if i.__class__.__name__ == "Armor":
                                player.inv.append(i)
                        del player.current_room.items[:]

                        interact = False

                    elif x[0] == 'none':
                        interact = False
                
                else:
                    print("\n***Please choose from available commands***\n")

    elif direction == 'i':

        inventory = True

        while inventory == True:

            print(f"\nGold: {player.gold}")

            print(f"Inventory:")
            for i in player.inv:
                print(f'[{i}]')

            x = [str(x) for x in input("\n([drop/equip] [item] or [c]lose)\n").split()]

            if len(x) == 2:

                if x[0] == 'equip':
                    player.equip(x[1])

                elif x[0] == 'drop':
                    player.drop(x[1])

                else:
                    print("\n***Please choose from available commands***\n")

            elif len(x) == 1:

                if x[0] != 'c':
                    print("\n***Please choose from available commands***\n")
                else:
                    inventory = False

            else:
                print("\n***Please choose from available commands***\n")

    elif direction == 'eq':
        equipment = True
        while equipment == True:
            if len(player.equipment) == 0:
                print("You have nothing equipped")
                equipment = False
            else:
                for i in player.equipment:
                    if i.__class__.__name__ == "Weapon":
                        print(f"{i.iname}: attack({i.rating})")
                    elif i.__class__.__name__ == "Armor":
                        print(f"{i.iname}: armor({i.rating}")

    elif direction == 'st':
        print(f"Name: {player.name}\nHealth: {player.hp}\nAttack: {player.att}\nDefense: {player.defense}")


    elif direction == 'q':
        game = False

    else:
        print("\n***Please choose from available commands***\n")