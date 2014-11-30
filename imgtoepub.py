import argparse
import shutil


parser = argparse.ArgumentParser(description='Program to convert folder of images to epub.')
parser.add_argument('thedir', help='The directory of files to take and turn into an epub')
parser.add_argument('--output', '-o', help='Filename to create') #output name, including epub or not
parser.add_argument('--not', '-n', dest='uhno', action='store_true', help='If included, the directory is not images')

args = parser.parse_args()
if args.output.endswith(".epub"):
    outfile = args.output[:-5]
else:
    outfile = args.output


if args.uhno==True:
    #if it's not images
    print outfile
else:
    #if it is images
    print "tree"