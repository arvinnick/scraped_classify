#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:04:27 2019

@author: Seyedmohammad Mortaji
"""
import cv2, glob
import numpy as np
import pandas as pd

 
path = '/home/mohammad/Documents/bee_image_detector/data/*.jpg'
#find labels:
labels=[]
d = 0
for link in glob.glob(path):
       d = d+1
       link_ = link[len(path)-5:-4]
       label = []
       for i in link_:
              if i.isalpha():
                     label.append(i)
       label = ''.join(label)
       labels.append(label)
#labels_ = {}
#d = 0
#for i in labels:
#       labels_[i] = d
#       d = d+1
#labels = labels_
#del(labels_)
#for i in enumerate(labels.items()):
#       labels[i[1][0]] = i[0]
categories = list(set(labels))
n_categories = len(categories)
categories = np.array(categories)
ohe_encode = np.zeros((len(labels),n_categories))
for i in enumerate(labels):
       j = np.where(categories == i[1])
       ohe_encode[i[0],j] = 1
       

train_data = np.ndarray((1,40001))
train_data = pd.DataFrame(train_data)
train_data.to_csv('train.csv')



d=0
for link in glob.glob(path):
       try:
              d=d+1
              print(d,' from ',len(glob.glob(path)))
              link_ = link[len(path)-5:-4]
              label = []
              for i in link_:
                     if i.isalpha():
                            label.append(i)
              label = ''.join(label)
              matrix = cv2.imread(link,cv2.IMREAD_GRAYSCALE)
              matrix = cv2.resize(matrix,(200,200))
              matrix = np.append(matrix,labels[label])
              matrix = matrix.reshape(1,40001)
              matrix = pd.DataFrame(matrix)
              matrix.to_csv('train.csv',mode='a')
       except Exception as e:
              print(e)
              pass
       

       
#label is done. Load, resize and matrixize the image. Then, attach the lable and save it in hard drive.
#The above comment is done. I have to build the netural network first and then, feed each of the pics individually; not from the hard drive.
       