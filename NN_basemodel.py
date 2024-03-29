# -*- coding: utf-8 -*-
"""Deep bugs.ipynb

semi-Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MuhEb5-ow0aPoZEarISCivB2pfxxVcC_
"""

# NETWORK ARCHITECTURE
# INPUT (Dropout 20%)
# HIDDEN (Dense 200 + ReLU + Dropout 20%)
# OUTPUT (Dense 1 + Sigmoid)

# Compile w binary_crossentropy loss and the rmsprop optimizer.
# Train for 10 epochs. Batch size 100

#Libraries to create the multiclass model
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
#from keras.utils import np_utils

import numpy as np

def basemodel_deepbugs():
  model = Sequential()

  #Adding 20% dropout
  model.add(Dropout(0.20))

  #Add 1 layer with output 200 and relu function
  model.add(Dense(200,activation='relu'))

  #Adding 20% dropout here
  model.add(Dropout(0.20))

  #Add 1 layer with output 1 and sigmoid function
  model.add(Dense(1,activation='sigmoid'))

  return model

model = basemodel_deepbugs()

