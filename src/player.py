# Write a class to hold player information, e.g. what room they are in
# currently.
from attributes import Attributes
from weapon import Weapon
from armor import Armor
from money import Money

class Player(Attributes):
    def __init__(self, current_room, inv=None, equipment=None, gold=0, att=1, hp=20, defense=0):
        super().__init__(att, hp, defense)
        self.name = "Player"
        self.current_room = current_room
        if inv is None:
            self.inv = []
        else:
            self.inv = inv
        if equipment is None:
            self.equipment = []
        else:
            self.equipment = equipment
        self.gold = gold
        self.att = att
        self.hp = hp
        self.defense = defense

    def move(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to')
        if next_room == None:
            print("\n***You cannot go in that direction***\n")
        elif next_room is not None:
            self.current_room = next_room
            print(f'\nYou enter the {self.current_room.name}. \n {self.current_room.desc}\n')
            
    def look(self):
        if len(self.current_room.items) > 0:
            print("\nYou look around and see: ")
            for i in self.current_room.items:
                print(f'{i.idesc}')
        else:
            print("\nThere is nothing of importance")


    def take(self, item):
        for i in self.current_room.items:
            if i.iname != item:
                print("\n***You do not see that here***\n")
            elif i.__class__.__name__ == "Money":
                self.gold = self.gold + i.amount
                self.current_room.items.remove(i)
            else:
                print(f"You put the {i.iname} in your inventory")
                self.inv.append(i)
                self.current_room.items.remove(i)

    def drop(self, item):
        for i in self.inv:
            if i.iname != item:
                print("You do not have that item in your inventory")
            else:
                print(f"You drop your {i.iname}")
                self.inv.remove(i)
                self.current_room.items.append(i)

    def equip(self, item):
        for i in self.inv:
            if i.iname != item:
                print(f"You do not have a {item}")
            elif i.__class__.__name__ == "Weapon":
                print(f"You equip the {i.iname}")
                self.equipment.append(i)
                self.inv.remove(i)
                self.att += i.rating
            elif i.__class__.__name__ == "Armor":
                print(f"You equip the {i.iname}")
                self.equipment.append(i)
                self.inv.remove(i)
                self.defense += i.rating
            else:
                print("You cannot equip that")