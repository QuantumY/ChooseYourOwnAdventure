import sys
from scenario import scenario
from story_parser import story_parser
from character import character


storyParser = story_parser()

[theStory, thePlayer] = storyParser.parseStoryFile(sys.argv[1])

theStory.prompt(thePlayer)
