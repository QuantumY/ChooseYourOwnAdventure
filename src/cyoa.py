from scenario import scenario
from story_parser import story_parser
from character import character
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',
    action="store", dest="fpath",
    help="Path to a story file.", default="")

args = vars(parser.parse_args())

if args["fpath"] == "":
    print "No file path argument(s) passed in, use -h or --help for help"
    exit()

storyParser = story_parser()

[theStory, thePlayer] = storyParser.parseStoryFile(args["fpath"])

theStory.prompt(thePlayer)
