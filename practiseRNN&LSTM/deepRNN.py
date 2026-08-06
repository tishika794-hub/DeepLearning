import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keraslayers import Dense, Embedding, LSTM, GRU, SimpleRNN

#load dataset
(x_train, y_train), (x_test, y_test) = imdb.Load_data(num_words=10000)

# pad sequences to ensure same length
x_train = pad_sequences(x_train, maxlen=100)
x_test = pad_sequences(x_test, maxlen=100)

#define RNN model
model = Sequential()
model.add(Embedding(10000, 32, input_length=100)) #embedding layer to convert words to vector
model.add(SimpleRNN(5, return_sequences= True)) #rnn layer with 5 units
model.add(SimpleRNN(5)) #another rnn layer with 5 unit
model.add(Dense(1, activation='sigmoid')) 
model.summary()

#define LSTM model
model = Sequential()
model.add(Embedding(10000, 32, input_length=100))
model.add(LSTM(5, return_sequences= True))
model.add(LSTM(5))
model.add(Dense(1, activation= 'sigmoid'))
model.summary()

#define GRU model
model = Sequential()
model.add(Embedding(10000, 32, input_length=100))
model.add(GRU(5, return_sequences= True))
model.add(GRU(5))
model.add(Dense(1, activation= 'sigmoid'))
model.summary()

# compile the model
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split = 0.2 )
