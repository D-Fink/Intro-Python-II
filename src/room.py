# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def get_room(self, name, desc):
        return self.name and self.desc

    def __str__(self):
        return "{}. {}".format(self.name, self.desc)