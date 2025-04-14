import time
import os
import glob
from conversion_functions import *

# The code is prepared to read one-dimensional matrices,
# so data cannot be stored in two-dimensional format.
# If it is stored in 2D (which is the case), a conversion to 1D is required.

# Constants
NUM_PIXELS_AMOSTRA = 10800  # number of pixels per image 120*90
DIR_PATH_TEST = 'test_images'

# Activation of weights & bias
weights = np.random.uniform(-0.05, 0.05, NUM_PIXELS_AMOSTRA)
bias = 0

# The number of training epochs indicates how many times the model will pass through the entire training dataset.
# (10–50) for small datasets, 50–200 for medium datasets, 100–500+ for large datasets.
# The learning rate determines how big or small the adjustment of the model’s weights will be at each training iteration.
# If the learning rate is too high, the model might not converge or jump to a suboptimal solution.
# If it's too low, training may be too slow or get stuck in a local minimum.
# Small values: (0.00001 to 0.001)
# Medium values: (0.001 to 0.01)
# High values: (0.1 to 1.0)
# The more images there are, the more epochs are needed to iterate through them.
list_functions_options = [
  {"id":1, "function": "SIGMOID", "num_epochs": 550, "learning_rate": 0.01},
  {"id":2, "function": "SIGMOID", "num_epochs": 1050, "learning_rate": 0.005},
  {"id":3, "function": "SIGMOID", "num_epochs": 5100, "learning_rate": 0.001},
  {"id":4, "function": "STEP_FUNCTION", "num_epochs": 40, "learning_rate": 0.01}, 
  {"id":5, "function": "STEP_FUNCTION", "num_epochs": 400, "learning_rate": 0.00001} #STOP NEED 1000 (more images)(learning rate of 0.00001 is the only that works)
]
### SIGMOID FUNCTION - conversion of fyles included in time
###  EPOCHS - 550 / LEARNING RATE - 0.01 //// TIME -  /// Battery - 33.44 seconds
### EPOCHS - 1050 / LEARNING RATE - 0.005 //// TIME -  /// Battery - 54.12 seconds
### EPOCHS - 5100 / LEARNING RATE - 0.001 //// TIME -  /// Battery - 220 seconds
#### STEP-FUNCTION
### EPOCHS - 40 / LEARNING RATE - 0.01 //// TIME - 0.24 seconds /// Battery - 17.36 seconds
### EPOCHS - 400 / LEARNING RATE - 0.00001 //// TIME - 4.88 seconds /// Battery - 34.41 seconds

# Dataset List
list_dataset = [
  {"id":1, "dataset": "datasets/datasetA", "word": "A"}, ###130 images
  {"id":2, "dataset": "datasets/datasetK", "word": "K"}, ###130 images
  {"id":3, "dataset": "datasets/datasetSTOP", "word": "STOP"} ###146
]

##############################################
### Neuron Activation Function Calculation ###
##############################################
def activation_function(function, soma_dos_pesos_amostra):
  if function == 'STEP_FUNCTION':
    return np.where(soma_dos_pesos_amostra >= 0, 1, 0)
  elif function == 'SIGMOID':
    return 1 / (1 + np.exp(-soma_dos_pesos_amostra))  

##########################
### Prediction Function ###
##########################
def predict(function, input):
  return activation_function(function, np.dot(weights, input) + bias)

##############
### Training ###
##############
def train(epochs, learning_rate, function):
  global bias, weights
  for epoch in range(epochs):
    epoch_loss = 0
    for sample in range(num_train_samples):
      prediction = predict(function, train_data[sample])
      error = train_labels[sample] - prediction
      epoch_loss += error ** 2
      weights += learning_rate * error * train_data[sample]
      bias += learning_rate * error

    if epoch % 10 == 0:
      print(f"Epoch {epoch}: Loss = {epoch_loss:.4f}")

################
### Template ###
################
def templateDataset():
  print("Welcome to perceptron, choose the letter of the dataset that you want!")
  print("\n1 - Dataset A")
  print("\n2 - Dataset k")
  print("\n3 - Dataset STOP")
  print("\n4 - Leave the program")

def templatePerceptron():
  print("\nChoose the function and options that you prefer!\n")
  print("\n1 - Sigmoid / 550 epochs / 0.01 learning Rate")
  print("\n2 - Sigmoid / 1050 epochs / 0.005 learning Rate")
  print("\n3 - Sigmoid / 5100 epochs / 0.001 learning Rate")
  print("\n4 - Step_Function / 40 epochs / 0.01 learning Rate")
  print("\n5 - Step_Function / 400 epochs / 0.00001 learning Rate")
  print("\n6 - Leave the program ")
  
############
### Main ###
############
if __name__ == "__main__":
  # Menu and definition of dataset, function, num_epochs and learning_rate
  templateDataset()
  while True:
    numberDataset = int(input("\nYour option -> : "))
    if numberDataset in [1,2,3,4]:
      break
    elif numberDataset == 3:
      exit()
    else:
      print("Wrong option, try again!")

  for option in list_dataset:
    if option["id"] == numberDataset:
      dataset = option["dataset"]
      word = option["word"]

  templatePerceptron()
  while True:
    numberMenu = int(input("\nYour option -> : "))
    if numberMenu in [1,2,3,4,5]:
      break
    elif numberMenu == 6:
      exit()
    else:
      print("Wrong option, try again!")

  for option in list_functions_options:
    if option["id"] == numberMenu:
      num_epochs = option["num_epochs"]
      learning_rate = option["learning_rate"]
      function = option["function"]

  # Counting the number of training and test samples
  num_train_samples = countImages(dir_path=dataset)
  num_test_samples = countImages(dir_path=DIR_PATH_TEST)

  # Train labels indicate whether the training images are 'A' or not.
  # In this project we assume all are 'A', so all labels will be 1.
  # If there were some that were not 'A', we would set those to 0.
  train_labels = np.zeros(num_train_samples, dtype=int)
  # Define the intervals where the labels should be 1 (This indicates where the A's are in the dataset)
  n = int(num_train_samples / 2)
  train_labels[:n] = 1  

  start = time.time()

  if not os.path.exists(f'data_file/image_data{word}.npz'):
    print("\nCreating training files...")
    loadStoreImagesFileNpz(num_train_samples, dir_path=dataset, word=word) 

  # Load data from NPZ file
  train_data = []
  with np.load(f'data_file/image_data{word}.npz') as data:
    train_data = np.array([data[key] for key in data.files])
  
  # Resize and convert test images
  test_data = loadStoreImages(num_test_samples, dir_path=DIR_PATH_TEST)  

  print("\nTraining the perceptron...")
  train(num_epochs, learning_rate, function)
  
  print("\n\nResults:\n")
  for i in range(num_test_samples):
    prediction = predict(function, test_data[i])

    if function == "SIGMOID":
      prediction_percentage = prediction * 100
      if prediction_percentage >= 80:
        print(f"Image {i+1} -> I think it's an {word} with {prediction_percentage:.2f} percent certainty")
      else:
        print(f"Image {i+1} -> I think it's not an {word} with {100 - prediction_percentage:.2f} percent certainty")
    elif function == "STEP_FUNCTION":
      if prediction == 1:
        print(f"Image {i+1} -> I think it's an {word}.")
      else:
        print(f"Image {i+1} -> I think it's not an {word}.")

  end = time.time()
  print(f"\nExecution time = {end - start:.2f} seconds\n")