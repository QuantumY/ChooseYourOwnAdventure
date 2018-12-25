
def itemFactory(itemJson):
    if itemJson["itemType"] == "Weapon":
        return weapon(itemJson["name"], itemJson["itemType"], itemJson["itemSubType"], itemJson["description"], itemJson["damage"], itemJson["adjustment"])

    if itemJson["itemType"] == "Money":
        return weapon(itemJson["name"], itemJson["itemType"], itemJson["itemSubType"], itemJson["description"], itemJson["value"])


class item(object):

    def __init__(self, name, itemType, itemSubType, description):
        self.name = name
        self.type = itemType
        self.itemSubType = itemSubType
        self.description = description

    def show(self):

        print "Name: " + self.name
        print "Type: " + self.type
        print "SubType: " + self.itemSubType
        print "Description: " + self.description


class armor(item):

    def __init__(self, name, itemType, itemSubType, description, adjustment=0):
        super(armor, self).__init__(name, itemType, itemSubType, description)

        self.adjustment = adjustment
        

    def show(self):

        super(armor,self).show()
        print "Adjustment: " + self.adjustment


class weapon(item):

    def __init__(self, name, itemType, itemSubType, description, damage, adjustment=0):
        super(weapon,self).__init__(name, itemType, itemSubType, description)

        self.adjustment = adjustment
        self.damage = damage

    def show(self):

        super(weapon,self).show()
        print "Adjustment: " + str(self.adjustment)
        print "Max Damage: " + str(self.damage)


class money(item):

    def __init__(self, name, itemType, itemSubType, description, value):
        super(money,self).__init__(name, itemType, itemSubType, description)

        self.value = value

class gem(item):

    def __init__(self, name, itemType, itemSubType, description, value):
        super(gem,self).__init__(name, itemType, itemSubType, description)

        self.value = value



class inventory:

    def __init__(self, items=None):

        if items == None:
            self.items = []
        else:
            self.items = items

    def addItem(self, newItem):
        self.items.append(newItem)

    def show(self):
        print "Inventory Items"
        for item in self.items:
            print ""
            item.show()

        print ""
