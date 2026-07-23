#pooling mai feature map ka size reduce hota hai , convolution layer kai baad include karte hai pooling layer
import tensorflow
from tensorflow import keras
from keras.layers import Dense,Flatten,MaxPooling2D
from keras import Sequential
from keras.datasets import mnist

(x_train, y_train),(x_test, y_test)= mnist.load_data()
model = Sequntial()
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',activation='relu',input_shape=(28,28,1)))
model.add(MaxPooling2D(32,pool_size=(2,2),strides=2,padding='valid'))
model.add(Conv2D(32,kernel_size=(3,3),padding='valid',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))
model.add(Flatten())

model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()
