
class item:

    def __init__(self, name, itemType, description):
        self.name = name
        self.type = itemType
        self.description = description

    def show(self):

        print "Name: " + self.name + "\n"
        print "Type: " + self.type + "\n"
        print "Description: " + self.description + "\n"


class armor(item):

    def __init__(self, name, itemType, description, adjustment=0):
        item.__init__(self, name, itemType, description)

        self.adjustment = adjustment
        

    def show(self):

        super().show()
        print "Adjustment: " + self.adjustment + "\n"


class weapon(item):

    def __init__(self, name, itemType, description, damage, adjustment=0):
        item.__init__(self, name, itemType, description)

        self.adjustment = adjustment
        self.damage = damage

    def show(self):

        super().show()
        print "Adjustment: " + self.adjustment + "\n"
        print "Damage: " + self.damage + "\n"


class money(item):

    def __init__(self, name, itemType, description, value):
        item.__init__(self, name, itemType, description)

        self.value = value

class gem(items):

    def __init__(self, name, itemType, description, value):
        item.__init__(self, name, itemType, description)

        self.value = value

class inventory:

    def __init__(self, items=None):

        if items == None:
            self.items = []
        else:
            self.items = items

        self.weapons = {}
        self.money = None
        self.gems = None

        self.items[0] = { name: "Leather Armor", acAdjust: 2}


    def show(self):
        for item in self.items:
            print "Items\n"
            item.show()
