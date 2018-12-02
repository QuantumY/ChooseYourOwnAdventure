from choice import choice
from story_parser import story_parser

storyParser = story_parser()

theStory = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard_test.md")

# Test the parser
#theStory.echo()

theStory.prompt()
