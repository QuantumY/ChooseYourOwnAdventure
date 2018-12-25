from inventory import *


class character:

    def __init__(self, name, cType="Fighter", race="Human", hp=1, rawInventory=None):
        self.inventory = inventory()
        self.name = name
        self.hp = hp
        self.ac = 10
        self.xp = 0
        self.type = cType
        self.race = race

        if rawInventory != None:
            for item in rawInventory:
                self.inventory.addItem(itemFactory(item))

    def show(self):
        print(chr(27) + "[2J")
        print "Name: "+self.name
        print "Hit Points: "+self.hp
        print "Armor Class: "+str(self.ac)
        print "Experience Points: "+str(self.xp)
        print "Type: "+self.type
        print "Race: "+self.race
        print ""

        self.inventory.show()
