import scipy.ndimage as sc
import pandas as pd
import  cv2
import numpy as np
import glob
from PIL import Image 
import math
import os
import matplotlib
from scipy import ndimage as a

from os import listdir
from os.path import isfile, join
import numpy
import cv2

x_train_pos = np.zeros((6000,324), dtype=np.float32)
x_cv_pos = np.zeros((2000,324), dtype=np.float32)
x_test_pos = np.zeros((2524,324), dtype=np.float32)

mypath='/home/abhishek/Desktop/project/Grey_Photos_32X32'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    
    images[n] = a.imread( join(mypath,onlyfiles[n]) )
  #images[n]=cv2.resize(images[n],(32,32),interpolation = cv2.INTER_AREA)
    hog=cv2.HOGDescriptor((32,32),(16,16),(8,8),(8,8),9)
    if(n<6000):
        
        x_train_pos[n,:]=numpy.transpose(hog.compute(images[n]))
        #print('train')
        #print(n)

    if(n>=6000 and n<8000):
        x_cv_pos[n-6000,:]=numpy.transpose(hog.compute(images[n]))
        #print('cv')
        #print(n)
    if(n>=8000):
        x_test_pos[n-8000,:]=numpy.transpose(hog.compute(images[n]))
        #print('test')
        #print(n)
#print(n)  
#print(histogram[n,:])
#cv2.imwrite('/home/abhishek/Desktop/project/resized_neg/image'+str(n)+'.jpg',images[n])
x_train_neg = np.zeros((4800,324), dtype=np.float32)
x_cv_neg = np.zeros((1600,324), dtype=np.float32)
x_test_neg = np.zeros((1560,324), dtype=np.float32)

mypath='/home/abhishek/Desktop/project/resized_neg'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    images[n] = a.imread( join(mypath,onlyfiles[n]) )
    hog=cv2.HOGDescriptor((32,32),(16,16),(8,8),(8,8),9)
    if(n<4800):
        
        x_train_neg[n,:]=numpy.transpose(hog.compute(images[n]))
        #print('train')
        #print(n)

    if(n>=4800 and n<6400):
        x_cv_neg[n-4800,:]=numpy.transpose(hog.compute(images[n]))
        #print('cv')
        #print(n)
    if(n>=6400):
        x_test_neg[n-6400,:]=numpy.transpose(hog.compute(images[n]))
        #print('test')
        #print(n)

x_train=np.vstack((x_train_pos,x_train_neg))
x_cv=np.vstack((x_cv_pos,x_cv_neg))
x_test=np.vstack((x_test_pos,x_test_neg))
y_train = np.vstack(((np.ones((6000,1), dtype=np.uint8)),(np.zeros((4800,1), dtype=np.uint8))))
y_cv = np.vstack(((np.ones((2000,1), dtype=np.uint8)),(np.zeros((1600,1), dtype=np.uint8))))
y_test = np.vstack(((np.ones((2524,1), dtype=np.uint8)),(np.zeros((1560,1), dtype=np.uint8))))


print(x_train.shape)
print(x_cv.shape)
print(x_test.shape)
print(y_train.shape)
print(y_cv.shape)
print(y_test.shape)


from sklearn.svm import SVC
clf = SVC(probability=True,kernel='linear')
clf.fit(x_train, y_train) 

histogram = np.zeros((324,1), dtype=np.float32)
gray=a.imread('/home/abhishek/Desktop/project/Caltech_WebFaces/pic00033.jpg', 0)

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
i=0
while((150+i*8<np.size(gray,0))):
    j=0
    while((120+j*8<np.size(gray,1))):
        cell_32x32=gray[0+j*8:150+j*8,0+i*8:150+i*8]
        cell_32x32=cv2.resize(cell_32x32,(32,32),interpolation = cv2.INTER_CUBIC)
        hog=cv2.HOGDescriptor((32,32),(16,16),(8,8),(8,8),9)
        histoVector=np.transpose(hog.compute(cell_32x32))
        #histoVector=histoVector.reshape(1,-1)
        #histoVector=[histoVector]
        #y_pred = model.predict(histoVector)
        y_pred = clf.predict_proba(histoVector)
        #print(histoVector)
        #y_pred=y_pred.reshape(1,-1)
        #print(y_pred,i,j)
        if(y_pred[0][1]>.990):
            gray=cv2.rectangle(gray,(0+j*8,0+i*8),(150+j*8,150+i*8),(0,255,0),3)
            print(i,j)
            cv2.imshow('detectedFaceInGreenBoundry',gray)
            cv2.waitKey(1000)
        j=j+1
        
    i=i+1
    

cv2.imshow('detectedFaceInGreenBoundry',gray)       
