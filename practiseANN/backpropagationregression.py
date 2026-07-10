import numpy as np
import pandas as pd
df = pd.DataFrame([[8,8,4],[7,9,5],[6,10,6],[5,12,7]], columns=['cgpa','resume_score','package'])
def initialize_parameters(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for l in range(1, L):
        parameters['w' + str(l)] = np.ones((layer_dims[l-1], layers_dims[l]))*0.01
        parameters['b' + str(l)] = np.zeros((1, layers_dims[l]))
    return parameters

def linear_forward(A_prev, W, b):
    Z = np.dot(A_prev, W) + b
    return Z

def L_layer_forward(X, parameters):
    A = X
    L = len(parameters)//2
    for l in range(1, L):
        A_prev = A
        w1 = parameters['w' + str(l)]
        b1 = parameters['b' + str(l)]
        #print("A" + str(l-1)+ ":" , A_prev)
        #
        #
        #
        A = linear_forward(A_prev, parameters['w' + str(l)], parameters['b' + str(l)])
        print("A" + str(l)+ ":" , A)
        print("**"*20)
    return A, A_prev

X = df[['cgpa','resume_score']].values[0].reshape(2,1)
y = df[['lpa']].values[0][0]

parameters = initialize_parameters([2,2,1])

y_hat[0][0] = y_hat
y_hat, A1 = L_layer_forward(X, parameters)

#loss nikalenge
(y-A2)**2

#LOSS nikalliya parameter update karenge
def update_parameters(parameters, y, y_hat, A1, X):
    parameters['W2'][0][0] = parameters['W2'][0][0]+(0.001*2*(y-y_hat)*A1[0][0])
    parameters['W2'][1][0] = parameters['W2'][1][0]+(0.001*2*(y-y_hat)*A1[1][0])
    parameters['b2'][0][0] = parameters['W2'][1][0]+(0.001*2*(y-y_hat))

    parameters['W1'][0][0] = parameters['W1'][0][0]+(0.001*2*(y-y_hat)*parameters['W2'][0][0]*X[0][0])
    parameters['W1'][0][1] = parameters['W1'][0][1]+(0.001*2*(y-y_hat)*parameters['W2'][0][1]*X[0][0])
    parameters['b1'][0][0] = parameters['b1'][0][0]+(0.001*2*(y-y_hat)*parameters['W2'][0][0])

    parameters['W1'][1][0] = parameters['W1'][1][0]+(0.001*2*(y-y_hat)*parameters['W2'][0][0]*X[0][0])
    parameters['W1'][1][1] = parameters['W1'][1][1]+(0.001*2*(y-y_hat)*parameters['W2'][0][0]*X[0][0])
    parameters['b1'][1][0] = parameters['W1'][1][0]+(0.001*2*(y-y_hat)*parameters['W2'][0][0])

#epochs implementation
parameters = initialize_parameters([2,2,1])
epochs = 5
for i in range(epochs):
    Loss = []
    for j in range(df.shape[0]):
        X = df[['cgpa','profile_score']].values[j].reshape(2,1)
        y = df[['lpa']].values[j][0]
        y_hat, A1 = L_layer_forward(X, parameters)
        y_hat = y_hat[0][0]

        update_parameters(parameters, y, y_hat, A1, X)
        Loss.append((y-y_hat)**2)
    print('epoch-',i+1, 'loss-',np.array(Loss).mean())
parameters
