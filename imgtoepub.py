import argparse
import shutil
import tempfile
import os
import zipfile
import errno
from time import gmtime, strftime

# From Randy
# f = NamedTemporaryFile(delete=False)
# f.close()
# fn = f.name + '.gz'
# os.rename(f.name, fn)
# fz = gzip.open(fn, 'wt')
# writer = csv.writer(fz, delimiter='\t', lineterminator=lt)
# for row in table:
#     writer.writerow(row)
# fz.close()

parser = argparse.ArgumentParser(description='Program to convert folder of images to epub.')
parser.add_argument('thedir', help='The directory of files to take and turn into an epub')
parser.add_argument('--output', '-o', help='Filename to create') #output name, including epub or not
parser.add_argument('--not', '-n', dest='uhno', action='store_true', help='If included, the directory is not images')

# cp -r for python
def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
        print(src)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

args = parser.parse_args()
thedir = os.path.abspath(args.thedir)
if args.output != None:
    if args.output.endswith(".epub"):
        outfile = args.output[:-5]
    else:
        outfile = args.output

if args.uhno==True:
    #if it's not images
    print("moo")
else:
    #if it is images
    dirtoputin = tempfile.gettempdir()
    dirtoputin += "/img2epub" + strftime("%Y-%m-%d[%H:%M:%S]", gmtime())
    copyanything(thedir, dirtoputin)
    
    shutil.rmtree(dirtoputin)
    