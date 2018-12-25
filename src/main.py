from scenario import scenario
from story_parser import story_parser
import sys
from character import character

if sys.argc < 2:
	print "Only one argument is allowed: the story file!"
  exit()

storyParser = story_parser()

[theStory, thePlayer] = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard.md")

theStory.prompt(thePlayer)
