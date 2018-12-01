import choice

class story_paser:

    def __init__(self, sFile):  #file with story
        self.IS_CHOICE = "#"
        self.IS_CHOICE_DESC = "##"
        self.IS_NEXT_CHOICE = "###"
        self.IS_NEXT_CHOICE_LINK = "####"
        self.story_path = sFile
        self.story = None
        self.counter = None #story counter (charcter in story)

    def detectLineType(self):
        endDetect = False
        out = None
        while (self.story)[self.counter] == ' ' or  '\t' or '\n':
            self.counter += 1
        while len(out) < 5:
            self.counter += 1
            if (self.story)[self.counter] == '#':
                out += "#"
            else:
                break
        return out

    def getData(self):
        out = None
        while (self.counter < len(self.story)) and detectLineType() == None:
            out += (self.story)[self.counter]
            self.counter += 1
        return out

    def getChoice(self, pChoice):   #parent choice
        out = choice()
        while self.counter < len(self.story):
            if detectLineType() == self.IS_CHOICE:
                out.title = getData()
                if (detectLineType() == self.IS_CHOICE_DESC):
                    out.text = getData()

    def parseStory(self):
        self.story = open(story_path, "r")
        self.story = self.story.read()
        self.counter = 0
        while True:
            c = self.story[self.counter]
            getChoice()
