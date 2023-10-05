# mogrt.py
# v1.0
# Builds Adobe Stock Mogrt Batches based on my personal file structure
# workbench.tv

import os
import argparse
import textwrap
import glob
import pathlib
import shutil
import zipfile


parser = argparse.ArgumentParser(
    formatter_class = argparse.RawTextHelpFormatter,
    description = 'Builds Adobe Stock Mogrt Batches based on my personal file structure')
parser.add_argument('src_dir', help = 'source directory')
args = parser.parse_args()

src_dir = args.src_dir

name = os.path.basename(src_dir)

mogrt = src_dir + '/' + name + '.mogrt'
thumb = src_dir + '/Renders/Thumbnail.jpg'
preview = src_dir + '/Renders/Preview.mp4'

root = "/Volumes/Dropbox/Dropbox/Work/Clients/Adobe Stock/_MOGRTS/Batch Delivery"
dst = root + '/' + name
tmp = "/Volumes/Dropbox/Dropbox/Work/Clients/Adobe Stock/_MOGRTS/Batch Delivery Temp"

# Build Main folder
os.mkdir(dst)

# Build stock deliverable
shutil.copyfile(mogrt, dst + '/' + name + '.mogrt')
shutil.copyfile(preview, dst + '/' + name + '.mp4')
shutil.copyfile(thumb, dst + '/Thumbnail.jpg')

deliverable = pathlib.Path(dst)
deliverable_zip = root + '/' + name + '.zip'

with zipfile.ZipFile(deliverable_zip, 'w') as zip:
    for file in deliverable.rglob('*'):
        file_path = str(file)
        zip.write(file, file_path[len(dst):len(file_path)])

print('--> Zipped Deliverable')

# Clean Up
shutil.rmtree(dst)

print('--> Cleaned up')
