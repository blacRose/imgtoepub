import argparse

def thedir():
    print "meow"

def noimg():
    #run when they flag that the dir isn't images
    print "moo"
def doimg():
    #run when they don't flag that the dir isn't images
    print "mao!"


parser = argparse.ArgumentParser(description='Program to convert folder of images to epub.')
parser.add_argument('thedir', help='The directory of files to take and turn into an epub', type=int)
parser.add_argument('--not', '-n', action='store_true', help='If included, the directory is not images')


args = parser.parse_args()

print args.thedir