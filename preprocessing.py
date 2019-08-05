#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 01:02:26 2019

@author: mohammad
"""

import numpy as np
import pandas as pd
from PIL import Image
from glob import glob
data = pd.DataFrame()
data.to_csv('data.csv')
file_names = [i for i in glob('/home/mohammad/Documents/projects/scraped_classify/data/*.jpg')]
counter = 0
for i in glob('/home/mohammad/Documents/projects/scraped_classify/data/*.jpg'):
       label = i[56:-4]
       temp_list = []
       for j in label:
              if j.isalpha:
                     temp_list.append(j)
              else:
                     pass
       label = ''.join(temp_list)
       image_data = Image.open(i)
       image_data = image_data.resize((300,300))
       image_data = np.asarray(image_data)
       if len(image_data.shape)>2:
              image_data = image_data[:,:,0]
       else:
              pass
       temp_data = pd.DataFrame({label:image_data.flatten()})
       temp_data.to_csv('data.csv',mode='a')
       print(counter,'  done from:   ',len(file_names))
       counter = counter+1

                     
                    
