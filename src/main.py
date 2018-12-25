import sys
import getopt

from scenario import scenario
from story_parser import story_parser
from character import character

fpath = None
options, remainder - getopt.getopt(sys.argv[1:], 'd:a', ['directory=', 'algorithm', 'version'])
for opt, arg in option:
    if opt in ('-f', '--file')
        fpath = arg
    elif opt in ('-h', '--help')
        print "Use -f or --file to specify the path to a story file"
    else
        print "No argument(s) or valid argument(s) passed in, use -h or --help for help"

storyParser = story_parser()

[theStory, thePlayer] = storyParser.parseStoryFile(fpath)

theStory.prompt(thePlayer)
