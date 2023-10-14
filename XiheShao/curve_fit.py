# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 08:15:09 2023

@author: Ivan
"""

import pathlib
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from keras.layers import LSTM, Dense, Activation

print(tf.__version__)

csidata0 = pd.read_csv(r'C:\Users\Ivan\Desktop\srtp\csidata.txt', header=None)
csidata1=csidata0.T
csidata1.insert(loc=0,column='time',value=range(1,1+len(csidata1)))
csidata1.columns=['time','csi']
#print(csidata1)
csidata1.plot(x='time',y='csi')
time_array=csidata1['time'].tolist()
time_array=np.array(time_array).reshape((len(time_array),1))
csi_array=csidata1['csi'].tolist()
csi_array=np.array(csi_array).reshape((len(csi_array),1))
print(time_array)

#setup model
model=keras.Sequential()
model.add(Dense(100,  input_dim=1))
model.add(Activation('relu'))
model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('tanh'))
model.summary()

#optimizer=keras.optimizers.experimental.RMSprop()

model.compile(optimizer='rmsprop',
              loss='mse')#compile model
model.fit(time_array,csi_array,epochs=100,batch_size=10)

y_pred=model.predict(time_array)
plt.plot(time_array,y_pred)
plt.show()