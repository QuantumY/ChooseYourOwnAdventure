from scenario import scenario
from story_parser import story_parser

storyParser = story_parser()

theStory = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard.md")

theStory.prompt()
