# open a png file, check width, height, image format and file name
import os
# change directory to location where image is saved
os.chdir()
# verify path of the directory is correct
os.getcwd()
from PIL import Image
Test = Image.open ('XYZ.png')
Test
# get the size of the image (height, width)
Test.size
width, height = Test.size
# get the width of the image
width
# get the height of the image
height
# get filename
Test.filename
# get file format
Test.format_description
