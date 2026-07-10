import numpy as np
import pandas as pd

df = pd.DataFrame([[8,8,1],[7,9,1],[6,10,0],[5,5,0]],columns= ['cgpa','profile_score','placed'])
df.head()

def initialize_parameters(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for l in range(1,L):
        parameters['W'+str(l)] = np.ones((layer_dims[l-1],layer_dims[l]))*0.1
        parameters['b'+str(l)] = np.zeros((layer.dims[l],1))
    return parameters

# utility function
def sigmoid(z):
    A = 1/(1+np.exp(-z))
    return A

def linear_forward(A_prep,W,b):
    z = np.dot(W,A_prev)+b
    A = sigmoid(z)
    return A

def L_layer_forward(X, parameters):
    A = X
    L = len(parameters)//2
    for l in range(1,L+1):
        A_prev = A
        W1 = parameters['W'+str(l)]
        b1 = parameters['b'+str(l)]
        A = linear_forward(A_prev,W1,b1)
    return A, A_prev

def update_parameters(parameters,y,y_hat,A1,X):
    parameters['W2'][0][0] = parameters['W2'][0][0]+(0.001*(y-y_hat)*A1[0][0])
    parameters['W2'][0][0] = parameters['W2'][0][0]+(0.001*(y-y_hat)*A1[1][0])
    parameters['b1'][0][0] = parameters['b1'][1][0]+(0.001*(y-y_hat))

    parameters['W1'][0][0] = parameters['W1'][0][0]+(0.001*(y-y_hat)*parameters['W2'][0][0]*A1[0][0]*(1-A1[0][0]*X[0][0]))
    parameters['W1'][0][1] = parameters['W1'][0][1]+(0.001*(y-y_hat)*parameters['W2'][0][0]*A1[0][0]*(1-A1[0][0]*X[0][0]))
    parameters['b1'][0][0] = parameters['b1'][0][0]+(0.001*(y-y_hat)*parameters['W2'][0][0]*A1[0][0]*(1-A1[0][0]))

    parameters['W1'][1][0] = parameters['W1'][1][0]+(0.001*(y-y_hat)*parameters['W2'][1][0]*A1[1][0]*(1-A1[1][0]*X[0][0]))
    parameters['W1'][1][1] = parameters['W1'][1][1]+(0.001*(y-y_hat)*parameters['W2'][1][1]*A1[1][0]*(1-A1[1][0]*X[0][0]))
    parameters['b1'][1][0] = parameters['b1'][1][0]+(0.001*(y-y_hat)*parameters['W2'][1][0]*A1[1][0]*(1-A1[1][0]))

X = df[['cgpa','profile_score']].values[1].reshape(l,1)
y = df[['placed']].values[1][0]

y_hat, A1 = L_layer_forward(X, parameters)
y_hat = y_hat[0][0]

update_parameters(parameters, y, y_hat, A1, X)
print('Loss for this student-', -y*np.log(y_hat)-(1-y)*np.log(1-y_hat))

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
        update_parameters(parameters,y,y_hat,A1,X)
        Loss.append(-y*np.log(y_hat)-(1-y)*np.log(1-y_hat))
    print('epoch-',i+1,'Loss-'np.array(Loss).mean())
parameters
