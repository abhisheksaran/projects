#import opencv as cv
#import opencv as cv 
import scipy.ndimage as sc
import pandas as pd
import  cv2
import numpy as np
import glob
from PIL import Image 
import math
import os
import matplotlib

#filelist = glob.glob('Grey_Scale/*.jpg')
#print(filelist[0][11:])

df6 = pd.read_csv("csv_modified_distance.txt")
pic_index = df6.iloc[:,0]
pic_name = df6.iloc[:,1]
left_x = df6.iloc[:,5]
left_y = df6.iloc[:,6]
right_x = df6.iloc[:,7]
right_y = df6.iloc[:,8]
nose_x = df6.iloc[:,2]
nose_y = df6.iloc[:,3]
dis = df6.iloc[:,4]
#j=0

for i in range(10524):
	#c = str("{}".format(filelist[i][11:]))
	c = str("{}".format(pic_name[i]))
	d = str("{}.jpg".format(pic_index[i]))
	#print(i)
	#a = cv2.imread('Grey_Scale/%s'%c)
	a = sc.imread('Grey_Scale/%s'%c)
	#print(c)
	#print(a)
	#if(len(a.shape) == 3):
	#	grey_scale  = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
	#else:
	#	grey_scale = a
	#s = np.array([np.array(Image.open(grey_scale))])
	#print(s.shape)
	#cv2.imshow('albuan', grey_scale)
	#cv2.imwrite("Grey_Scale/%s"%c, grey_scale)
	#print(i)
	#cv2.waitKey(1)
	if(int(nose_x[i])> int(1.5*dis[i]) and int(nose_y[i])>int(1.5*dis[i]) and (int(nose_x[i])+int(1.5*dis[i])<a.shape[1]) and (int(nose_y[i])+int(1.5*dis[i])<a.shape[0])):
		crop_img = a[int(left_y[i]):int(right_y[i]),int(left_x[i]):int(right_x[i])]
		cv2.imwrite("modified_Crop_Images/%s"%d,crop_img) 
	else:
		cv2.imwrite("modified_Crop_Images/%s"%d,a) 
#print(grey_scale.shape)   
