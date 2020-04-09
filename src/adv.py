from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Coins", "A sack of gold [Coins]"), Item("Sword", "A Rusted Iron [Sword]")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Coins", "A sack of gold [Coins]"), Item("Shield", "A rusty iron [Shield].")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Coins", "A sack of gold [Coins]"), Item("Chestplate", "A rusty iron [Chestplate]")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Coins", "A sack of gold [Coins]"), Item("Helm", "A rusty iron [Helm]et")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Coins", "A sack of gold [Coins]"), Item("Boots", "A pair of moldy [Boots]")]),
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
    direction = input("\nPlease enter direction ([n]orth [s]outh [e]ast [w]est [search] [i]nventory [q]uit):\n")

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
                    #if x[0] != 'all' or x[0] != 'none':
                    #    print("\n***Please choose from available commands***\n")
                    if x[0] == 'all':
                        for i in player.current_room.items:
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

            print(f"\nInventory:")
            for i in player.inv:
                print(f'[{i}]')

            x = [str(x) for x in input("\n([drop] [item] or [c]lose)\n").split()]

            if len(x) == 2:

                if x[0] != 'drop':
                    print("\n***Please choose from available commands***\n")
                else:
                    player.drop(x[1])
                    

            elif len(x) == 1:

                if x[0] != 'c':
                    print("\n***Please choose from available commands***\n")
                else:
                    inventory = False

            else:
                print("\n***Please choose from available commands***\n")

    elif direction == 'q':
        game = False

    else:
        print("\n***Please choose from available commands***\n")