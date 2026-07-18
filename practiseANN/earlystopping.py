import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from pylab import rcParams
import warnings
from mlxtend.plotting import plot_decision_regions
from matplotlib.colors import ListedColormap
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
import seaborn as sns

x,y = make_circles(n_samples=100, noise=0.1, random_state=1)
sns.scatterplot(x[:,0],x[:,1],hue = y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= 0.42)

model = Sequential()
model.add(Dense(256, activation= 'relu', input_dim=2))
model.add(Dense(1,activation= 'sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs= 3500, validation_data=(x_test, y_test))

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label= 'test')
plt.legend()
plt.show()

#early stopping

model= Sequential()

model.add(Dense(256, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
callback = EarlyStopping(monitor='val_loss',min_delta=0.00001,patience=20,verbose=1,mode='auto',baseline=None, restore_best_weights=False)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3500, callbacks=callback)

lt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()