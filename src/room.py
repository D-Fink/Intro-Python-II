# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, name, desc, items=None):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

        if items is None:
            self.items = []
        else:
            self.items = items