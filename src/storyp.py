import choice

class story_paser:

    def __init__(self, sFile):  #file with story
        self.IS_CHOICE = "#"
        self.IS_CHOICE_DESC = "##"
        self.IS_NEXT_CHOICE = "###"
        self.IS_NEXT_CHOICE_LINK = "####"
        self.sf = open(sFile, "r")
        self.story = self.sf.read()
        self.counter = 0    #story counter (charcter in story)

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
        cc = choice()   #current choice to work on
        nc = []         # next choice (array names)
        while self.counter < len(self.story):
            if detectLineType() == self.IS_CHOICE:
                cc.title = getData()
                if detectLineType() == self.IS_CHOICE_DESC:
                    cc.text = getData()
                elif detectLineType() == self.IS_NEXT_CHOICE:
                    nc.append(getData())
                elif detectLineType() == self.IS_NEXT_CHOICE_LINK:
                    nc.append(getData())
                else:
                    pChoice.addChoice(cc)
                    break
            else:
                break
        return nc

    def parseStory(self):
        while True:
            getChoice()
