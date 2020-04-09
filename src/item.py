class Item:

    def __init__(self, iname, idesc):
        self.iname = iname
        self.idesc = idesc

    def __str__(self):
        return "{}".format(self.iname)