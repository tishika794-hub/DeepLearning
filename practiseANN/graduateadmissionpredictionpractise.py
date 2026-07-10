#this is a dataset of people who apply for graduation abroad ismai 7column hai of documents required for admission and 1 column is target column which is admit or not admit
import pandas as pd
import numpy as np
import os
for dirname, _, filename in os.walk('/kaggle/input'):
    for filename in filename:
        print(os.path.join(dirname, filename))
df = pd.read_csv()
df.head()
df.shape()
df.info() #to see if there are any null values
df.duplicated().sum() #to see any duplicate values 
df.drop(columns=['serialno'],inplace=True) #to drop these column which are of no use)
df.head()#data after removing serialno column
x = df.iloc[:,0:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=42)
from sklearn.preprocessing import MinMaxScaler #to scale the data between 0-1
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)#isse pura x_train tranform hogya hai similar value mai
import tensorflow
from tensorflow import keras
from tensorflow.keras import sequential
from keras.layers import Dense
model = sequential()
model.add(Dense(7,activation='relu',input_dim=7)) #input layer 
model.add(Dense(1,activation='linear')) #output layer ka activation funtion linear hota hai in case of regression
model.summary() #isse hame model ka summary milta hai ki kitne parameters hai aur kis layer mai kitne neurons hai 
model.compile(loss='mean_squared_error',optimizer = 'Adam') #compile mai loss funtion and optimizer define karte hai 
history = model.fit(x_train_scaled,y_train,epochs=10,validation_split=0.2) #isse model train hota hai aur validation mai 20% data use hota hai 
y_pred = model.predict(x_test_scaled) #isse model test data mai predict karta hai

df = pd.read_csv('/kaggle/input/graduate-admission-prediction/Graduate Admission Predictions.csv')
df.head()
df.info()
df.duplicated().sum()
df.drop(columns=['serialno'],inplace=True)
x = df.drop('admit',axis=1)
y = df['admit']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=42,test_size=0.2)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)
model = Sequential()
model.add(Dense(7,activation='relu',input_dim=7))
model.add(Dense(1,activation='linear'))