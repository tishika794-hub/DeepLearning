from keras.layers import *
from keras.models import Model

#define 2 sets of inputs
inputA = Input(shape=(32,))
inputB = Input(shape=(128,))

#the 1st branch operates on 1st input
x = Dense(8,activation='relu')(inputA)
x1 = Dense(4,activation='relu')(x)

#the 2nd branch operates on 2nd input
y = Dense(64,activation='relu')(inputB)
y1 = Dense(32,activation='relu')(y)
y2 = Dense(4,activation='relu')(y1)

#combine output of 2 branches
combined = concatenate([x1, y2])

#apply FC layer and then regression prediction on combined outputs
z = Dense(2, activation='relu')(combined)
z1 = Dense(1, activation='linear')(z)

#our model will accept inputs of 2 branches and output single 
model = Model(input=[inputA, inputB], outputs=z1)

from keras.utils import plot_model
plot_model(model)