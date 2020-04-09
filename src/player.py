# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, inv=[]):
        self.name = "Player"
        self.current_room = current_room
        self.inv = inv

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
            item_num = 0
            for i in self.current_room.items:
                item_num += 1
                print(f'{i.idesc}')
        else:
            print("\nThere is nothing of importance")
            

    def take(self, item):
        for i in self.current_room.items:
            if i.iname != item:
                print("\n***You do not see that here***\n")
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