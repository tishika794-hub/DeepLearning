#mnist dataset (picture of handwritten images with lex pixel ,hame 70k data par model ko train karna hai ss tarike sai ki ham koi nayi picture de to vo number identify kar paye using artificial neural network)
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()#iss case mai hamne train test split nhi kiya kyuki ye dataset already keras mai present hai in a ready to use way
x_train.shape() #data actuall images kai form mai nhi hai ye pixels kai form mai hai 28*28 pixels ka image hai in a array
#jab hamne shape use kiya to hame pata chala ki 60000 images hai aur har image 28*28 pixels ka hai
#y train mai 60000 labels hai aur har label 0-9 mai se koi number hai
import matplotlib.pyplot as plt
plt.imshow(x_train[0]) #to see first image of the dataset
#ab ham apna neural network train karenge ki kab koun sa pixel hone pai koun sa value hota hai
# array mai max value 255 hai ab ham array kai har number ko 255 sai divide karenge to get max value 1 array ka range 0-1 mai rakhne nai weights ki value thik rahengi for prediction
x_train = x_train/255
x_test = x_test/255
model = Sequential()
#keras mai flatten hota hai jo 2D array ko 1D mai convert karta hai
model.add(Flatten(input_shape=(28,28))) #input shape 28,28 hai
model.add(Dense(128,activation='relu')) #hidden layer
model.add(Dense(10,activation='softmax')) #output layer 
model.compile(loss='sparse_categorical_crossentropy',optimizer= 'adam',metrics=['accuracy']) 
model.fit(x_train, y_train,epochs=10)
y_prob = model.predict(x_test)
y_pred = y_prob.argmax(axis=1) #isse array mai vo number aa jayenge jinki images bani hai
accuracy_score(y_test,y_pred)
#ham model ki aquarcy improve karsakte hai by adding more hidden layers and changing the number of neurons in the hidden layer
#ham apne arcitecture mai 128 nodes lennge aur output mai 10 nodes esa isliye kyuki ye multiclass input hai ismai 10 category hai 0-9 to jab bhi ham multiclass mai kaam karte hai jitne class hote hai utne output nodes lagate hai

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train/255
x_test = x_test/255
model = Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128,activation='relu'))
model.add(Dense(64,activation='relu'))
model.fit()