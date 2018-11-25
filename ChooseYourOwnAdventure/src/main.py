#!/usr/bin/python

from choice import choice
from story_parser import story_parser

storyParser = story_parser()

theStory = storyParser.parseStoryFile("../Stories/LairOfTheGoblinHoard.md")

next_choice = theStory.prompt()

while True:
	next_choice = next_choice.prompt()
