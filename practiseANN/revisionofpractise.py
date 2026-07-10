import numpy as np
import pandas as pd
import sklearn.pyplot 
df = pd.read_csv()
df.head()
df.info()
df.duplicated.sum()
df.drop(['rownumber','customerid','surname'],inplace=True)
x = df.drop('exited',axis=1)
y = df['exited']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(3,activation='sigmoid',input_dim=x_train_scaled.shape[1]))
model.add(Dense(1,activation='sigmoid'))
model.fit(x_train_scaled,y_train,epochs=100)
model.predict(x_test_scaled)

#mnist dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
import matplotlib.pyplot as plt
plt.imshow(x_train[0])
x_train = x_train/255
x_test = x_test/255

#graduate admission prediction
df = pd.read_csv('graduate_admission_data.csv')
df.info()
df.duplicated().sum()
