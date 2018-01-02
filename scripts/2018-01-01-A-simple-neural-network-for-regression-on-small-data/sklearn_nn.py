"""A basic neural net with sklearn."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import scale
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.neural_network import MLPRegressor


def cost(prediction, target):
    """Root mean squared error cost function."""
    assert np.shape(prediction) == np.shape(target)
    r = prediction - target

    return np.sum(r**2) / len(target)


# load and set up data
data = pd.read_csv('example_data.csv')
data = data.sample(data.shape[0])

# preprocess
X = scale(np.array(data.iloc[:, :-2]))
Y = np.array(data.iloc[:, -2])

# build training and test sets
train_size = 100
X_train, Y_train = X[:train_size, :], Y[:train_size]
X_test, Y_test = X[train_size:, :], Y[train_size:]

print('start training Gaussian process')

# set up Gaussian process regression
gp_kernel = 1. * RBF(1.)
gp = GaussianProcessRegressor(
    kernel=gp_kernel, alpha=1e-1,
    n_restarts_optimizer=100).fit(X_train, Y_train)
p = gp.predict(X_test)
e = cost(p, Y_test)
print('GP error: {}'.format(e))

# plot the results
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(121)
ax.plot(Y_test, p, 'o', alpha=0.2)
plt.title('GP error: {0:.3f}'.format(e))
plt.xlabel('target')
plt.ylabel('prediction')

print('start training neural network')

# set up neural network for regression
nn = MLPRegressor(
    hidden_layer_sizes=(100,), solver='lbfgs', activation='relu', alpha=0.1,
    learning_rate='constant', max_iter=500
    ).fit(X_train, Y_train)
p = nn.predict(X_test)
e = cost(p, Y_test)
print('NN error: {}'.format(e))

# plot the results
ax = fig.add_subplot(122)
plt.plot(Y_test, p, 'o', alpha=0.2)
plt.title('NN error: {0:.3f}'.format(e))
plt.xlabel('target')
plt.ylabel('prediction')

plt.show()
