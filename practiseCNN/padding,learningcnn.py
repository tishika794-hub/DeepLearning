#padding mai image ka size change karte hai by adding row and column along all 4 sides
import tensorflow
from tensorflow import keras
from keras.layers import Dense,Conv2D,Flatten
from keras import dataset
from keras.datasets import mnist
(x_train, y_train),(x_test,y_test) = mnist.load_data()

model = Sequntial()
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',activation='relu'))
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',activation='relu'))
model.add(Flatten())

model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()

#strides 
model = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',strides=(2,2),activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',strides=(2,2),activation='relu'))
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',strides=(2,2),activation='relu'))
model.add(Flatten())

model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()