from pyio import *
from choice import choice

class scenario:

    def __init__(self):
        self.title = None
        self.desc = None
        self.choices = []

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
        usersChoice = pyget() # Bug. Need to check for only numbers in user selection
        return int(usersChoice)

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


    def prompt(self):
        pyout(self.title)
        pyout(self.desc)
        pyout("\n")

        cc = 1
        for aChoice in self.choices:
            pyout(str(cc)+" : "+aChoice.getUserSelectText())
            cc = cc + 1

        pyout(str(cc)+" : Quit")

        ucc = 0 #user choice counter

        while ucc <= 0 or (ucc > cc):
            ucc = self.collectUserInput()

        if ucc == cc:
            pyout("\nBye!")
        else:
            self.choices[ucc-1].prompt()
