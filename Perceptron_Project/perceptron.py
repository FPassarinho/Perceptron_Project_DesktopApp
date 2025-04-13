import time
import os
import glob
from conversion_functions import *

# The code is prepared to read one-dimensional matrices,
# so data cannot be stored in two-dimensional format.
# If it is stored in 2D (which is the case), a conversion to 1D is required.

# Constants
NUM_PIXELS_AMOSTRA = 10800  # number of pixels per image 120*90
DIR_PATH_DATA_FILE = 'data_file'
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
  {"id":1, "function": "SIGMOID", "num_epochs": 450, "learning_rate": 0.01},
  {"id":2, "function": "SIGMOID", "num_epochs": 950, "learning_rate": 0.005},
  {"id":3, "function": "SIGMOID", "num_epochs": 4600, "learning_rate": 0.001},
  {"id":4, "function": "STEP_FUNCTION", "num_epochs": 20, "learning_rate": 0.01},
  {"id":5, "function": "STEP_FUNCTION", "num_epochs": 350, "learning_rate": 0.00001}
]
### SIGMOID FUNCTION
###  EPOCHS - 450 / LEARNING RATE - 0.01 //// TIME -  /// Battery - 15.44 seconds
### EPOCHS - 950 / LEARNING RATE - 0.005 //// TIME -  /// Battery - 30.55 seconds
### EPOCHS - 4600 / LEARNING RATE - 0.001 //// TIME -  /// Battery - 125 seconds
#### STEP-FUNCTION
### EPOCHS - 20 / LEARNING RATE - 0.01 //// TIME - 0.24 seconds /// Battery - 2.36 seconds
### EPOCHS - 350 / LEARNING RATE - 0.00001 //// TIME - 4.88 seconds /// Battery - 14.18 seconds

# Dataset List
list_dataset = [
  {"id":1, "dataset": "datasetA"},
  {"id":2, "dataset": "datasetK"},
  {"id":3, "dataset": "datasetSTOP"}
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
  print("\n3 - Leave the program")

def templatePerceptron():
  print("\nChoose the function and options that you prefer!\n")
  print("\n1 - Sigmoid / 450 epochs / 0.01 learning Rate")
  print("\n2 - Sigmoid / 950 epochs / 0.005 learning Rate")
  print("\n3 - Sigmoid / 4600 epochs / 0.001 learning Rate")
  print("\n4 - Step_Function / 20 epochs / 0.01 learning Rate")
  print("\n5 - Step_Function / 350 epochs / 0.00001 learning Rate")
  print("\n6 - Leave the program ")
  
############
### Main ###
############
if __name__ == "__main__":
  # Menu and definition of dataset, function, num_epochs and learning_rate
  templateDataset()
  while True:
    numberDataset = int(input("\nYour option -> : "))
    if numberDataset in [1,2,3]:
      break
    elif numberDataset == 3:
      exit()
    else:
      print("Wrong option, try again!")

  for option in list_dataset:
    if option["id"] == numberDataset:
      dataset = option["dataset"]

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

  # Verify if the program has all required files
  if len(os.listdir(DIR_PATH_DATA_FILE)) < 3:
    files = glob.glob(os.path.join(DIR_PATH_DATA_FILE, '*'))
    for f in files:
      os.remove(f)
    loadStoreImagesFileTrain(num_train_samples, dir_path=dataset) 
    loadStoreImagesFileNpz(num_train_samples, dir_path=dataset) 
    loadStoreImagesFileTest(num_test_samples, dir_path=DIR_PATH_TEST)

  # Load data from NPZ file
  train_data = []
  with np.load('data_file/image_data.npz') as data:
    train_data = np.array([data[key] for key in data.files])
  
  # Resize and convert test images
  test_data = loadStoreImages(num_test_samples, dir_path=DIR_PATH_TEST)  

  train(num_epochs, learning_rate, function)
  
  print("\n\nResults:\n")
  for i in range(num_test_samples):
    prediction = predict(function, test_data[i])

    if function == "SIGMOID":
      prediction_percentage = prediction * 100
      if prediction_percentage >= 80:
        print(f"Image {i+1} -> I think it's an A with {prediction_percentage:.2f} percent certainty")
      else:
        print(f"Image {i+1} -> I think it's not an A with {100 - prediction_percentage:.2f} percent certainty")
    elif function == "STEP_FUNCTION":
      if prediction == 1:
        print(f"Image {i+1} -> I think it's an A.")
      else:
        print(f"Image {i+1} -> I think it's not an A.")

  end = time.time()
  print(f"\nExecution time = {end - start:.2f} seconds\n")