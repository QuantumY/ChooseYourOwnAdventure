from scenario import scenario
from story_parser import story_parser
from character import character

storyParser = story_parser()

[theStory, thePlayer] = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard.md")

theStory.prompt(thePlayer)
