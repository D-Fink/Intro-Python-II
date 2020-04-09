from item import Item
import random

class Money(Item):

    def __init__(self, iname, idesc, amount):
        super().__init__(iname, idesc)
        self.iname = iname
        self.idesc = idesc
        self.amount = amount