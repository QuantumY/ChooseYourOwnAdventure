from inventory import inventory


class character:

    def __init__(self, name, type, race=None, hp=None, inventory=None):
        self.inventory = None
        self.name = None
        self.hp = None
        self.ac = None
        self.type = None
        self.race = None

