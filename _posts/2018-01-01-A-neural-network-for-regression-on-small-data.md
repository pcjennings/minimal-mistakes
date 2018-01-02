I would like to see how to build a basic neural network for regression problems on small datasets. The aim is to see how well a neural net can perform when using 1,000 data points or fewer to train the model. Gaussian processes typically perform well on these problems and so I will be using this as a baseline upon which to compare the neural net.

## Dataset

I have just chosen a relatively simple dataset to perform some studies on. I won't go into detail on how it was generated, it is sufficient to say that there are approximately 20,000 data points and 200 features, with each data point having a single target. The dataset I am using, `example_data.csv`, can be downloaded from the [repository](https://github.com/pcjennings/pcjennings.github.io/tree/master/scripts/2018-01-01-A-neural-network-for-regression-on-small-data).

## Loading Data

To get the data from the raw csv format, I use the following code:

  ```python
  import numpy as np
  import pandas as pd

  from sklearn.preprocessing import scale

  # load and set up data
  data = pd.read_csv('example_data.csv')
  data = data.sample(data.shape[0])

  # preprocess
  X = scale(np.array(data.iloc[:, :-2]))
  Y = np.array(data.iloc[:, -2])

  # build training and test sets
  train_size = 1000
  X_train, Y_train = X[:train_size, :], Y[:train_size]
  X_test, Y_test = X[train_size:, :], Y[train_size:]
  ```

This simply reads in all the data, shuffles it and then selects the features and the targets. The all the features are scaled, though this method of globally scaling all train and test data together is not so realistic, but will work for this example. Finally, the data set is split into the train and test sets, resulting in four arrays.

The `train_size` parameter defines the size of the training dataset. In this example, the remaining data will be used as the test data set.

## General

In order to assess the various methods, I am using a root mean squared error cost function. As defined in the following snippet of code:

  ```python
  def cost(prediction, target):
    assert np.shape(prediction) == np.shape(target)
    r = prediction - target

    return np.sum(r**2) / len(target)
  ```

This will give the average error on the entire dataset. For comparative purposes, the code to set up a Gaussian process is as follows:

  ```python
  from sklearn.gaussian_process import GaussianProcessRegressor
  from sklearn.gaussian_process.kernels import RBF

  # set up Gaussian process regression
  gp_kernel = 1. * RBF(1.)
  gp = GaussianProcessRegressor(
      kernel=gp_kernel, alpha=1e-1,
      n_restarts_optimizer=100).fit(X_train, Y_train)
  p = gp.predict(X_test)
  e = cost(p, Y_test)

  print('GP error: {}'.format(e))
  ```

The radial basis function kernel is utilized along with a regularization applied to the covariance function. Hyperparameter optimizations is also performed.

## Neural Network

The starting setup of the neural network is as follows:

  ```python
  from sklearn.neural_network import MLPRegressor

  # set up neural network for regression
  nn = MLPRegressor(
      hidden_layer_sizes=(100,)
      ).fit(X_train, Y_train)
  p = nn.predict(X_test)
  e = cost(p, Y_test)

  print('NN error: {}'.format(e))
  ```

This just sets up a single hidden layer with 100 neurons (the default number). All other parameters in the model are initially set to the default.

## Results

For the default parameters of the neural net and a training data size of 100 data points, it is possible to get an accuracy of approximately 0.6 RMSE, on a range of approximately 20. This is pretty good, but it seems like there could be an improvement here, a Gaussian process with radial basis function kernel will typically perform approximately 35% better than the neural net.

The default number of neurons (100), in a single hidden layer, gives good results, increasing the number of neurons or layers tends to give worse results. The default activation function, `relu`, also appears to be pretty optimal. It is rarely that any of the other functions perform better through repeated sampling.

In order to improve this, the `lbfgs` solver can be used, instead of the default `adam` optimizer. The sklearn documentation suggests that this can perform better for small data sizes. This appears to give a relatively consistent improvement on the default neural net setup, where using the `lbfgs` solver, there is a 15% improvement on the `adam` solver.

The default L2-regularization of 1e-4 is perhaps a little small, with the potential to obtain more accurate predictions when it is set to slightly larger values in the interval 1e-1 to 1e-4. However, this generally has relatively little impact on the accuracy of predictions. The `max_iter` parameter can be set slightly larger when the regularization value is also larger (e.g. 1e-1).

## Conclusions

After some optimization of the neural network, it now gives comparable results to the Gaussian process. The following code was used to obtain these results from the neural net:

  ```python
  # set up neural network for regression
  nn = MLPRegressor(
      hidden_layer_sizes=(100,), solver='lbfgs',
      activation='relu', alpha=0.1,
      learning_rate='constant', max_iter=500
      ).fit(X_train, Y_train)
  p = nn.predict(X_test)
  e = cost(p, Y_test)

  print('NN error: {}'.format(e))
  ```

This process has resulted in a relatively good neural network, even if the setup is a little basic. In reality, there are many more steps that can be taken to produce a more optimized model, but this has produced good results. The final script, `sklearn_nn.py`, can be found in the [repository](https://github.com/pcjennings/pcjennings.github.io/tree/master/scripts/2018-01-01-A-neural-network-for-regression-on-small-data).
