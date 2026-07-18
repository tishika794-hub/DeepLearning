import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons

x,y = make_moons(n_sample = 500, noise= 0.05, random_state = 0.42)
plt.scatter(x[:,0],y[:,-1],c=y,s=100)
plt.plot()

model = Sequential()
model.add(Dense(10,activation= 'sigmoid',input_dims=2))
model.add(Dense(10,activation= 'sigmoid'))
model.add(Dense(10,activation= 'sigmoid'))
model.add(Dense(1,activation= 'sigmoid'))

model.compile(Loss='absolute_mean_square',optimizer='adam',metrice=['accuracy'])
old_weights = model.get_weights()[0]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=0.42)
model.fit(x_train, y_train, epochs=100)
#fixing vanishinggradient
new_weights = model.get_weights()[0]
gradient = (old_weights - new_weights)/0.001
model = Sequential()
model.add(Dense(10,activation = 'relu',input_dims=2))
model.add(Dense(10,activation = 'relu'))
model.add(Dense(10,activation = 'relu'))
model.add(Dense(10,activation = 'relu'))
model.add(Dense(10,activation = 'relu'))
model.add(Dense(1,activation = 'sigmoid'))
model.compile(loss= 'binary_crossentropy',optimizer='adam',metrics=['accuracy'])
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=0.42)
model.fit(x_train, y_train, epochs = 100)
