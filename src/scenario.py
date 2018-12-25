from pyio import *
from choice import choice
from time import sleep

class scenario:

    def __init__(self, characters=None, inventory=None):
        self.title = None
        self.desc = None
        self.choices = []
        self.characters = characters

        if inventory == None:
            self.inventory = inventory()
        else:
            self.inventory = inventory

    def addChoice(self, the_choice):
        self.choices.append(the_choice)

    def setTitle(self, newval):
        self.title = newval

    def getTitle(self):
        return self.title

    def setDesc(self, newval):
        self.desc = newval

    def getDesc(self):
        return self.desc

    def collectUserInput(self):
        pyout("Please Choose: ")
        usersChoice = pyget()

        ucInt = -1

        try:
            ucInt = int(usersChoice)
        except:
            ucInt = -1

        return ucInt

    def echo(self, n = 0):
        print n
        print "-------------------"
        print "Title: " + self.title
        print "Description: " + self.desc

        n = n + 1

        print "Children ---------->>>>>>>>>>>>>>"
        for choice in self.choices:
            choice.echo(n)

        print "-------------------"


    def prompt(self, player):
        print(chr(27) + "[2J")
        pyout(self.title)
        pyout(self.desc)
        pyout("\n")

        cc = 1
        for aChoice in self.choices:
            pyout(str(cc)+" : "+aChoice.getUserSelectText())
            cc = cc + 1

        pyout(str(cc)+" : Look Around")
        cc = cc + 1
        pyout(str(cc)+" : Me")
        cc = cc + 1
        pyout(str(cc)+" : Quit")

        ucc = 0 #user choice counter

        while ucc <= 0 or (ucc > cc):
            ucc = self.collectUserInput()

        if ucc == cc - 2:
            if self.inventory == None:
                print(chr(27) + "[2J")
                print "Nothing else here."
                sleep(3)
                self.prompt(player)
            else:
                self.inventory.show()
                self.prompt(player)
        elif ucc == cc - 1:
            player.show()
            sleep(7)
            self.prompt(player)
        elif ucc == cc:
            print(chr(27) + "[2J")
            pyout("\nBye!")
        else:
            self.choices[ucc-1].prompt(player)

