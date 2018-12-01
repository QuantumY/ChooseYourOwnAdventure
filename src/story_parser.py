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
        self.choiceDict = None


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


    def readChoiceDescription(self):
        choiceText = ""

        for line in self.sFile:
            if self.lineType(line) == self.IS_NOT_CHOICE_FIELD:
                choiceText = choiceText + line
            else:
                break
        return choiceText


    def seekAndProcessNewChoice(self, startPos, parentChoice):
        self.sFile.seek(startPos)
        childChoice = None
        currSeek = self.IS_CHOICE
        choiceText = None

        for line in self.sFile:
            line.strip()
            if currSeek == self.IS_CHOICE and self.lineType(line) == self.IS_CHOICE:
                if parentChoice.getTitle() == None:
                    parentChoice.setTitle(line.split(self.IS_CHOICE, 1)[1].strip())
                    currSeek = self.IS_CHOICE_DESC
                elif parentChoice.getTitle() == line.split(self.IS_CHOICE, 1)[1].strip():
                    currSeek = self.IS_CHOICE_DESC
            elif currSeek == self.IS_CHOICE_DESC and self.lineType(line) == self.IS_CHOICE_DESC:
                choiceText = self.readChoiceDescription()
                if choiceText != None:
                    parentChoice.setText(choiceText)
                    currSeek = self.IS_NEXT_CHOICE
                else:
                    print "ERROR: No Choice description found"
                    sys.exit()
            elif currSeek == self.IS_NEXT_CHOICE and self.lineType(line) == self.IS_NEXT_CHOICE:
                childChoice = choice()
                childChoice.setTitle(line.split(self.IS_NEXT_CHOICE, 1)[1].strip())
                currSeek = self.IS_NEXT_CHOICE_LINK
            elif currSeek == self.IS_NEXT_CHOICE_LINK and self.lineType(line) == self.IS_NEXT_CHOICE_LINK:
                thisPos = self.sFile.tell()
                childChoice = self.seekAndProcessNewChoice(thisPos,childChoice)
                self.sFile.seek(thisPos)
                if childChoice == None:
                    print "Done with child choices"
                else:
                    parentChoice.addChoice(childChoice)
            elif currSeek == self.IS_NEXT_CHOICE and self.lineType(line) == self.IS_CHOICE:
                childChoice.echo()
                return childChoice

        return None


    #### Parse A Story File
    # Returns a choice object that is the top level of the story

    def parseStoryFile(self, pathToStoryFile):
        # Open file, assume Markdown format
        self.sFile = open(pathToStoryFile, "r")

        self.storyGraphEntry = choice()

        self.seekAndProcessNewChoice(0,self.storyGraphEntry)

        self.sFile.close()

        return self.storyGraphEntry
