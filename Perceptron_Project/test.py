import numpy as np

class Perceptron:

  def __init__(self, learning_rate=0.01, num_epochs=350):
    self.lr = learning_rate
    self.n_ep = num_epochs
    self.weights = None
    self.bias = None

  def step(self, x):
    return np.where(x >=0, 1, 0)
  
  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))
  
  def derivate_sigmoid(x):
    return sigmoid(x) * (1-sigmoid(x))
