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

train_path = '../swarg_training_data.npz'
test_path = '../swarg_eval_data.npz'

# load up data
with np.load(train_path) as data:
      x_data = data['data_x']
      y_data = data['labels_y']


# break up data
# paper says 100k files train and 50k test, but all we got are json
train_p = 2/3 
#rng = np.random.default_rng()
#rng.shuffle(x_data, axis = 0)
#rng.shuffle(y_data, axis = 0) 
from math import ceil
train_data_x = x_data[:ceil(len(x_data)*train_p)]
train_data_y = y_data[:ceil(len(y_data)*train_p)]
val_data_x = x_data[ceil(len(x_data)*train_p):]
val_data_y = y_data[ceil(len(y_data)*train_p):]

#print(len(x_data) == len(train_data_x) + len(val_data_x))

with np.load(test_path) as data:
      data_test = data['data_x']
      labels_test = data['labels_y']

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

#Compile the model using binary_cross loss function and rmsprop optim
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop', 
              metrics=['accuracy'])

model_mdata = model.fit(train_data_x, train_data_y, 
       validation_data=(val_data_x, val_data_y), 
       epochs=10, batch_size=100, shuffle=True)

# it smol
model.save('deepbug_model.keras')

#model = keras.models.load_model("deepbug_model.keras")
#
#model_mdata = model.evaluate(data_test, labels_test)
#print(model_mdata)
## This stuff prints models. But the code is deprecated
#
#import matplotlib.pyplot as plt
## Plot accuracy vs epoch
#plt.plot(model_mdata['accuracy'])
#plt.plot(model_mdata['val_accuracy'])
#plt.title('Model Accuracy vs. Epoch')
#plt.ylabel('Model Accuracy')
#plt.xlabel('Epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()
#
## Plot accuracy vs epoch
#plt.plot(model_mdata.history['loss'])
#plt.plot(model_mdata.history['val_loss'])
#plt.title('Model loss vs. Epoch')
#plt.ylabel('Model loss')
#plt.xlabel('Epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()
#