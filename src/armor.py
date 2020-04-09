from item import Item

class Armor(Item):

    def __init__(self, iname, idesc, rating):
        super().__init__(iname, idesc)
        self.iname = iname
        self.idesc = idesc
        self.rating = rating