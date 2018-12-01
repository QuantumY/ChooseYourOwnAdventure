import re
from choice import choice
import sys as sys

class story_parser:

    def __init__(self):
        self.IS_CHOICE = "#"
        self.IS_CHOICE_DESC = "##"
        self.IS_NEXT_CHOICE = "###"
        self.IS_NEXT_CHOICE_LINK = "####"
        self.IS_NOT_CHOICE_FIELD = ""
        self.sFile = None
        self.storyGraphEntry = None
        self.pos = 0
        self.parentChoice = None
        self.firstChoiceName = None
        self.choiceDict = {}


    def lineType(self, line):
        if line.find(self.IS_NEXT_CHOICE_LINK) != -1:
            return self.IS_NEXT_CHOICE_LINK
        elif line.find(self.IS_NEXT_CHOICE) != -1:
            return self.IS_NEXT_CHOICE
        elif line.find(self.IS_CHOICE_DESC) != -1:
            return self.IS_CHOICE_DESC
        elif line.find(self.IS_CHOICE) != -1:
            return self.IS_CHOICE
        else:
            return self.IS_NOT_CHOICE_FIELD

    def addToDict(self, thisTitle):
        if thisTitle == None:
            print "ERROR: No Choice title text"
            sys.exit()
        if thisTitle not in self.choiceDict:
            self.choiceDict[thisTitle] = choice()
            self.choiceDict[thisTitle].setTitle(thisTitle)
            #print "Adding new " + thisTitle + " to dict"
            if self.firstChoiceName == None:
                self.firstChoiceName = thisTitle
                self.storyGraphEntry = self.choiceDict[thisTitle]


    def createAllChoices(self):

        for line in self.sFile:
            if self.lineType(line) == self.IS_CHOICE:
                thisTitle = line.split(self.IS_CHOICE, 1)[1].strip()
                self.addToDict(thisTitle)
            if self.lineType(line) == self.IS_NEXT_CHOICE_LINK:
                thisTitle = line.split(self.IS_NEXT_CHOICE_LINK, 1)[1].strip()
                self.addToDict(thisTitle)


    def getAllChoiceDescriptions(self):
        self.sFile.seek(0)
        thisTitle = None
        description = None

        for line in self.sFile:
            if self.lineType(line) == self.IS_CHOICE:
                if description != None:
                    self.choiceDict[thisTitle].setText(description)
                    #print thisTitle + "'s description: " + self.choiceDict[thisTitle].getText()
                    description = None
                    thisTitle = None
                thisTitle = line.split(self.IS_CHOICE, 1)[1].strip()
                #print "Looking for " + thisTitle + "'s description"
            elif self.lineType(line) == self.IS_CHOICE_DESC:
                if thisTitle == None:
                    print "Descption without Title"
                    sys.exit()
                description = line.split(self.IS_CHOICE_DESC, 1)[1].strip()
                #print thisTitle + "'s description started"
                if description == None:
                    description = " "
            elif self.lineType(line) == self.IS_NOT_CHOICE_FIELD and description != None:
                description = description + line.strip()
            elif self.lineType(line) == self.IS_NEXT_CHOICE_LINK and description == None and thisTitle != None:
                #print "ERROR: No Choice description found"
                sys.exit()

        # EOF before next tag
        if description != None:
            self.choiceDict[thisTitle].setText(description)
            #print thisTitle + "'s description: " + self.choiceDict[thisTitle].getText()


    def linkChildren(self):
        self.sFile.seek(0)
        thisTitle = None
        nextChoiceText =  None

        for line in self.sFile:
            if self.lineType(line) == self.IS_CHOICE:
                thisTitle = line.split(self.IS_CHOICE, 1)[1].strip()
            elif self.lineType(line) == self.IS_NEXT_CHOICE:
                nextChoiceText = line.split(self.IS_NEXT_CHOICE, 1)[1].strip()
            elif self.lineType(line) == self.IS_NEXT_CHOICE_LINK:
                #if self.storyGraphEntry.getTitle() == thisTitle:
                #    newChoice = choice()
                #    newChoice.setTitle(thisTitle)
                #    newChoice.setText(self.choiceDict[thisTitle].getText())
                #    self.storyGraphEntry.addChoice()
                #else:
                #print "Adding " + line.split(self.IS_NEXT_CHOICE_LINK, 1)[1].strip() + " as child of " + thisTitle
                self.choiceDict[thisTitle].addChoice(self.choiceDict[line.split(self.IS_NEXT_CHOICE_LINK, 1)[1].strip()])

    def printDict(self):
        for k,v in self.choiceDict.items():
            #print " >>>> " + k
            print v.echo()


    #### Parse A Story File
    # Returns a choice object that is the top level of the story

    def parseStoryFile(self, pathToStoryFile):
        # Open file, assume Markdown format
        self.sFile = open(pathToStoryFile, "r")

        self.createAllChoices()
        self.getAllChoiceDescriptions()
        self.linkChildren()

        #self.printDict()

        self.sFile.close()

        return self.storyGraphEntry

