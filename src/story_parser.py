import re
import json
from choice import choice
from scenario import scenario
from character import character
import sys as sys

class story_parser:

    def __init__(self):
        self.IS_PLAYER_START = "{"
        self.IS_PLAYER_END = "}"
        self.IS_SCENARIO = "#"
        self.IS_SCENARIO_DESC = "##"
        self.IS_NEXT_CHOICE = "###"
        self.IS_NEXT_CHOICE_LINK = "####"
        self.IS_NOT_SCENARIO_FIELD = ""
        self.sFile = None
        self.storyGraphEntry = None
        self.pos = 0
        self.firstChoiceName = None
        self.scenarioDict = {}


    def lineType(self, line):
        if line.find(self.IS_NEXT_CHOICE_LINK) != -1:
            return self.IS_NEXT_CHOICE_LINK
        elif line.find(self.IS_NEXT_CHOICE) != -1:
            return self.IS_NEXT_CHOICE
        elif line.find(self.IS_SCENARIO_DESC) != -1:
            return self.IS_SCENARIO_DESC
        elif line.find(self.IS_SCENARIO) != -1:
            return self.IS_SCENARIO
        elif line.find(self.IS_PLAYER_START) != -1:
            return self.IS_PLAYER_START
        elif line.find(self.IS_PLAYER_END) != -1:
            return self.IS_PLAYER_END
        else:
            return self.IS_NOT_SCENARIO_FIELD


    def checkKey(self, thisTitle):

        return re.sub(r'[^\x00-\x7F]+',r'', thisTitle)


    def addToDict(self, thisTitle):
        if thisTitle == None:
            print "ERROR: No Scenario title text"
            sys.exit()

        dictKey = self.checkKey(thisTitle)

        if dictKey not in self.scenarioDict:
            self.scenarioDict[dictKey] = scenario()
            self.scenarioDict[dictKey].setTitle(dictKey)
            #print "Adding new " + dictKey + " to dict"
            if self.firstChoiceName == None:
                self.firstChoiceName = dictKey


    def createAllScenarios(self):

        for line in self.sFile:
            if self.lineType(line) == self.IS_SCENARIO:
                thisTitle = line.split(self.IS_SCENARIO, 1)[1].strip()
                self.addToDict(thisTitle)


    def getAllChoiceDescriptions(self):
        self.sFile.seek(0)
        thisTitle = None
        description = None

        for line in self.sFile:
            if self.lineType(line) == self.IS_SCENARIO:
                if description != None:
                    self.scenarioDict[self.checkKey(thisTitle)].setDesc(description)
                    #print thisTitle + "'s description: " + self.scenarioDict[self.checkKey(thisTitle)].getDesc()
                    description = None
                    thisTitle = None
                thisTitle = line.split(self.IS_SCENARIO, 1)[1].strip()
                #print "Looking for " + thisTitle + "'s description"
            elif self.lineType(line) == self.IS_SCENARIO_DESC:
                if thisTitle == None:
                    print "Descption without Title"
                    sys.exit()
                description = line.split(self.IS_SCENARIO_DESC, 1)[1]
                #print thisTitle + "'s description started"
                if description == None:
                    description = " "
            elif self.lineType(line) == self.IS_NOT_SCENARIO_FIELD and description != None:
                description = description + line
            elif self.lineType(line) == self.IS_NEXT_CHOICE_LINK and description == None and thisTitle != None:
                #print "ERROR: No Choice description found"
                sys.exit()

        # EOF before next tag
        if description != None:
            self.scenarioDict[self.checkKey(thisTitle)].setDesc(description)
            #print thisTitle + "'s description: " + self.scenarioDict[self.checkKey(thisTitle)].getDesc()


    def addChoices(self):
        self.sFile.seek(0)
        thisTitle = None
        currentChoice = None

        for line in self.sFile:
            if self.lineType(line) == self.IS_SCENARIO:
                thisTitle = line.split(self.IS_SCENARIO, 1)[1].strip()
            elif self.lineType(line) == self.IS_NEXT_CHOICE:
                currentChoice = choice()
                currentChoice.setUserSelectText(line.split(self.IS_NEXT_CHOICE, 1)[1].strip())
            elif self.lineType(line) == self.IS_NEXT_CHOICE_LINK:
                currentChoice.setScenario(self.scenarioDict[self.checkKey(line.split(self.IS_NEXT_CHOICE_LINK, 1)[1].strip())])
                print "Adding " + line.split(self.IS_NEXT_CHOICE_LINK, 1)[1].strip() + " as child of " + thisTitle + " with user select text: " + currentChoice.getUserSelectText()
                self.scenarioDict[self.checkKey(thisTitle)].addChoice(currentChoice)


    def getPlayer(self):
        self.sFile.seek(0)
        inPlayer = ""

        for line in self.sFile:
            if self.lineType(line) == self.IS_PLAYER_START and inPlayer == "":
                inPlayer = inPlayer + self.IS_PLAYER_START
            elif inPlayer != "" and self.lineType(line) != self.IS_SCENARIO:
                inPlayer = inPlayer + line
            elif self.lineType(line) == self.IS_SCENARIO:
                break

        print inPlayer

        jsonPlayer = json.loads(inPlayer)

        thePlayer = character(jsonPlayer["name"], jsonPlayer["type"], jsonPlayer["race"], jsonPlayer["hp"], jsonPlayer["inventory"] )

        return thePlayer


    def printDict(self):
        for k,v in self.scenarioDict.items():
            #print " >>>> " + k
            print v.getTitle()

    #### Parse A Story File
    # Returns a choice object that is the top level of the story

    def parseStoryFile(self, pathToStoryFile):
        # Open file, assume Markdown format
        self.sFile = open(pathToStoryFile, "r")

        self.createAllScenarios()
        self.getAllChoiceDescriptions()
        self.addChoices()

        #self.printDict()

        #self.sFile.close()

        return [self.scenarioDict[self.firstChoiceName], self.getPlayer()]
