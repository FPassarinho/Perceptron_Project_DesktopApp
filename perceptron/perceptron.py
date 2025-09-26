import os
import numpy as np
import json
from conversion_functions import *
from flask import Flask, jsonify, request
from flask_cors import CORS

# The code is prepared to read one-dimensional matrices,
# so data cannot be stored in two-dimensional format.
# If it is stored in 2D (which is the case), a conversion to 1D is required.

# The number of training epochs indicates how many times the model will pass through the entire training dataset.
# (10–50) for small datasets, 50–200 for medium datasets, 100–500+ for large datasets.
# The learning rate determines how big or small the adjustment of the model’s weights will be at each training iteration.
# If the learning rate is too high, the model might not converge or jump to a suboptimal solution.
# If it's too low, training may be too slow or get stuck in a local minimum.
# Small values: (0.00001 to 0.001)
# Medium values: (0.001 to 0.01)
# High values: (0.1 to 1.0)
# The more images there are, the more epochs are needed to iterate through them.
### SIGMOID FUNCTION - conversion of fyles included in time /130 images
###  EPOCHS - 550 / LEARNING RATE - 0.01 //// TIME - 11,46 /// Battery - 33.44 seconds
### EPOCHS - 1050 / LEARNING RATE - 0.005 //// TIME - 17,39  /// Battery - 54.12 seconds
### EPOCHS - 5100 / LEARNING RATE - 0.001 //// TIME - 70.27 /// Battery - 220 seconds
#### STEP-FUNCTION
### EPOCHS - 40 / LEARNING RATE - 0.01 //// TIME - 4,01 seconds /// Battery - 17.36 seconds
### EPOCHS - 400 / LEARNING RATE - 0.00001 //// TIME - 8.30 seconds /// Battery - 34.41 seconds

app = Flask(__name__)
CORS(app)

with open("datasets.json", "r") as f:
    list_dataset = json.load(f)

with open("functions_options.json") as f:
    list_functions_options = json.load(f)

base_path = os.path.dirname(os.path.abspath(__file__))
data_file_dir = os.path.join(base_path, "data_file")

class Perceptron:
  def __init__(self, learning_rate, num_epochs, dir_path_train, dir_path_test, function, word):
    self.learning_rate  = learning_rate
    self.num_epochs  = num_epochs
    self.dir_path_train = dir_path_train
    self.dir_path_test = dir_path_test
    self.function = function
    self.word = word
    self.num_pixels = 10800 # number of pixels per image 120*90
    # Activation of weights & bias
    self.weights = np.random.uniform(-0.05, 0.05, self.num_pixels)
    self.bias = 0

    self.train_data = None
    self.train_labels = None
    self.test_data = None

    # Counting the number of training and test samples
    self.num_train_samples = countImages(dir_path=dir_path_train)
    self.num_test_samples = countImages(dir_path=dir_path_test)

  ##############################################
  ### Neuron Activation Function Calculation ###
  ##############################################
  def activation_function(self, x):
    if self.function == 'STEP_FUNCTION':
      return np.where(x >= 0, 1, 0)
    elif self.function == 'SIGMOID':
      return 1 / (1 + np.exp(-x))
    
  ###########################
  ### Prediction Function ###
  ###########################
  def predict(self, input):
    return self.activation_function(np.dot(self.weights, input) + self.bias)

  ################
  ### Training ###
  ################
  def train(self):  
    # Train labels indicate whether the training images are 'A' or not.
    # In this project we assume all are 'A', so all labels will be 1.
    # If there were some that were not 'A', we would set those to 0.
    self.train_labels = np.zeros(self.num_train_samples, dtype=int)
    # Define the intervals where the labels should be 1 (This indicates where the A's are in the dataset)
    n = int(self.num_train_samples / 2)
    self.train_labels[:n] = 1

    # load or create train data
    npz_path = os.path.join(data_file_dir, f"image_data{self.word}.npz")

    if not os.path.exists(npz_path):
        loadStoreImagesFileNpz(self.num_train_samples, dir_path=self.dir_path_train, word=self.word)

    with np.load(npz_path) as data:
        self.train_data = np.array([data[key] for key in data.files])

    # Training the perceptron
    for epoch in range(self.num_epochs):
      epoch_loss = 0
      for i in range(self.num_train_samples):
        prediction = self.predict(self.train_data[i])
        error = self.train_labels[i] - prediction
        epoch_loss += error ** 2
        self.weights += self.learning_rate * error * self.train_data[i]
        self.bias += self.learning_rate * error

      if epoch % 10 == 0:
        print(f"Epoch {epoch}: Loss = {epoch_loss:.4f}")

  def evaluate(self):
    # Resultados
    # Resize and convert test images
    self.test_data = loadStoreImages(self.num_test_samples, dir_path=self.dir_path_test)

    results = []
    for i in range(self.num_test_samples):
      prediction = self.predict(self.test_data[i])

      if self.function == "SIGMOID":
        prediction_percentage = float(prediction * 100)
        if prediction_percentage >= 80:
          results.append({
            "image": i + 1,
            "prediction": f"I think that is an {self.word} with {prediction_percentage:.2f}",
        })
        else:
          results.append({
            "image": i + 1,
            "prediction": f"I think that is not an {self.word} with {100 - prediction_percentage:.2f}",
        })
      else:
        if prediction == 1:
          results.append({
            "image": i + 1,
            "prediction": f"I Think that is an {self.word}",
        })
        else:
          results.append({
            "image": i + 1,
            "prediction": f"I Think that is not an {self.word}",
        })

    return jsonify(results)

@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()
  numberDataset = data["dataset_id"]
  numberMenu = data["function_id"]

  # Definition of dataset, letter, function, num_epochs and learning_rate
  for option in list_dataset:
    if option["id"] == numberDataset:
      dataset = option["dataset"]
      word = option["word"]

  dataset_path = os.path.join(base_path, "datasets", dataset)
  test_images_path = os.path.join(base_path, "test_images")

  for option in list_functions_options:
    if option["id"] == numberMenu:
      num_epochs = option["num_epochs"]
      learning_rate = option["learning_rate"]
      function = option["function"]

  perceptron = Perceptron(
    learning_rate=learning_rate,
    num_epochs=num_epochs,
    dir_path_train=dataset_path,
    dir_path_test=test_images_path,
    function=function,
    word=word
  )

  perceptron.train()
  return perceptron.evaluate()

if __name__ == '__main__':
  app.run(port=5000, debug=True)