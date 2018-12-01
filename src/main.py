from choice import choice
from story_parser import story_parser

storyParser = story_parser()

theStory = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard_test.md")

# Test the parsing
theStory.echo()

next_choice = theStory.prompt()

while True:
	next_choice = next_choice.prompt()
