import tensorflow as tf
import numpy as np
import pandas as pd
import time
df = pd.read_csv('/content/Social_Network_Ads.csv')
df.head() 
df = df[['Age','EstimatedSalary','Purchased']]
df.head()
x = df.iloc[:,0:2]
y = df.iloc[:,-1]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler
x_scaled = scaler.fit_transform(x)

import keras
from keras.models import Sequential
from keras.layers import Dense
model = Sequential
model.add(Dense(10, activation = 'relu',input_dim=2))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.compile(loss = 'binary_crossentropy', metrics=['accuracy'])
history = model.fit(x_scaled,y,epochs = 500, batch_size =1, validation_split = 0.2)

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
model = Sequential()

model.add(Dense(10,activation='relu',input_dim=2))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',metrics=['accuracy'])
#start = time.time()
history = model.fit(X_scaled,y,epochs=10,batch_size=250,validation_split=0.2)
#print(time.time() - start)
plt.plot(history.history['loss'])