from keras.models import Model
model = Model(input = x,outputs = [output1,output2])
from keras.layers import *
x = Input(shape=(3,))
hidden1 = Dense(128,activation='relu')(x)
hidden2 = Dense(64,activation='relu')(hidden1)

output1 = Dense(1,activation='linear')(hidden2)
output2 = Dense(1,activation='sigmoid')(hidden2)
model.summary()

from keras.utils import plot_model
plot_model(model,show_shapes=True)
