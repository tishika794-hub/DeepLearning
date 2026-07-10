import pandas as pd
import numpy as np
import os
for dirname, _, filename in os.walk('/kaggle/input'):
    for filename in filename:
        print(os.path.join(dirname, filename))
df = pd.read_csv()
df.head()
df.info() #to  see if there are any null values
df.duplicated().sum() #to see any duplicate values
df['exited'].value_counts() #to see distribution of number of output in that column
df.drop(['rownumber','customerid','surname'],inplace=True) #to drop these column which are of no use 
pd.get_dummies(df,columns=['geography','gender'],drop_first=True)
x = df.drop('exited',axis=1)
y = df['exited']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=42)
from sklearn.preprocessing import standardScaler
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)
import tensorflow 
from ternsorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(3,activation='sigmoid',input_dim=x_train_scaled.shape[1]))
model.add(Dense(1,activation='sigmoid'))
model.summary()

df = pd.read_csv()
df.head()
df.info()
df.duplicated().sum()
df.drop(['rownumber','customerid',],inplace=True)
df = df.get_dummies(columns=['geography'],drop_first=True)
x = df.drop('excited',axis=1)
y = df['excited']
from skelarn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
scaled_x_train = sc.fit_transform(x_train)
scaled_x_test = sc.transform(x_test)
model=Sequential()
model.add(Dense(3,activation='sigmoid',input_dim=scaled_x_train.shape[1]))
model.add(Dense(1,activation='sigmoid'))
model.fit(scaled_x_train,y_train,epochs=100,verbose=0)
y_pred= model.predict(scaled_x_test)


