
from choice import choice
from story_parser import story_parser

storyParser = story_parser()

theStory = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard_test.md")

#theStory.echo()

while True:
	next_choice = next_choice.prompt()
