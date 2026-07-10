import numpy as np
import pandas as pd
df = pd.DataFrame([[8,8,1],[7,9,1],[6,10,0],[5,5,0]],columns=['cgpa','profile_score','placed'])
df.head()
import tensorflow
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(2,activation='sigmoid',input_dim=2))
model.add(Dense(1,activation='sigmoid'))
model.summary()
model.get_weights()
new_weights = [np.array([[0.1,0.1],[0.1,0.1]],dtype = np.float32),np.array([0.,0.],dtype=np.float32),np.array([[0.1],[0.1]],dtype=np.float32),np.array([0.],dtype=np.float32)]
optimizer = keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='binary_cross_entropy',optimizer=optimizer)
model.fit(df.iloc[:,0:-1].values,df['lpa'].values,epochs=75,verbose=1,batch_size=1)
model.get_weights()


