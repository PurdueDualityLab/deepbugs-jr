# -*- coding: utf-8 -*-
"""Deep bugs.ipynb

Automatically generated by Colaboratory.

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
from keras.utils import np_utils

def basemodel():
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

model = basemodel()

#Compile the model using binary_cross loss function and rmsprop optim
model.compile(loss='binary_crossentropy',optimizer='rmsprop', metrics=['accuracy'])

model_mdata = model.fit(data_train, labels_train, validation_data=(data_test, labels_test), epochs=10, batch_size=100, shuffle=True)

#FILL THIS IN
scores = model.evaluate(data_test, labels_test)
print("Accuracy: %.2f%%"%(scores[1]*100))

#Plot accuracy vs epoch
plt.plot(model_mdata.history['accuracy'])
plt.plot(model_mdata.history['val_accuracy'])
plt.title('Model Accuracy vs. Epoch')
plt.ylabel('Model Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#Plot accuracy vs epoch
plt.plot(model_mdata.history['loss'])
plt.plot(model_mdata.history['val_loss'])
plt.title('Model loss vs. Epoch')
plt.ylabel('Model loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

