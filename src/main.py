from scenario import scenario
from story_parser import story_parser
from character import character


storyParser = story_parser()

[theStory, thePlayer] = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard_Future.md")

theStory.prompt(thePlayer)
