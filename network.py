#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:47:05 2019

@author: mohammad
"""
import numpy as np
import keras
network = keras.models.Sequential()
d_layer = keras.layers.Dense
network.add(d_layer(700,
                    activation='relu',
                    input_dim=train_data.shape[1]-1))
network.add(d_layer(2000,
                    activation='relu'))
network.add(keras.layers.Dropout(0.2))
network.add(d_layer(4000,
                    activation='relu'))
network.add(keras.layers.Dropout(0.2))
network.add(d_layer(4000,
                    activation='relu'))
network.add(keras.layers.Dropout(0.2))
network.add(d_layer(4000,
                    activation='relu'))
network.add(d_layer(6,
                    activation='relu'))
network.compile(optimizer='adam',
                loss='categorical_crossentropy')
