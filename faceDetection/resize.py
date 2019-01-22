import scipy.ndimage as sc
import pandas as pd
import  cv2
import numpy as np
import glob
from PIL import Image 
import math
import os
import matplotlib

from os import listdir
from os.path import isfile, join
import numpy
import cv2

mypath='/home/abhishek/Desktop/project/neg'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
  cv2.imread('/home/abhishek/Desktop/project/resized_neg/image'+str(i)+'.jpg',images[n])

