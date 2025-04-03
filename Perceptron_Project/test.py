import numpy as np

class Perceptron:

  def __init__(self, num_pixels, learning_rate, num_epochs, dir_path_train, dir_path_test):
    self.num_pixels = num_pixels
    self.learning_rate  = learning_rate
    self.num_epochs  = num_epochs
    self.dir_path_train = dir_path_train
    self.dir_path_test = dir_path_test

    self.weights = np.random.uniform(-0.05, 0.05, self.num_pixels)
    self.bias = 0

  def step(self, x):
    return np.where(x >=0, 1, 0)
  
  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))
