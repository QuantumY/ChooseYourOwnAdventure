from scenario import scenario
from story_parser import story_parser
import sys

storyParser = story_parser()

if sys.argc < 2:
	print "Only one argument is allowed: the story file!"

else:
	theStory = storyParser.parseStoryFile(sys.argv) #"../Stories/LairOfTheGoblinHoard.md"
	theStory.prompt()
