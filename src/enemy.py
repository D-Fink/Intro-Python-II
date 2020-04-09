from attributes import Attributes

class Enemy(Attributes):

    def __init__(self, name, att, hp):
        super().__init__(att, hp)
        self.name = name
        self.att = att
        self.hp = hp