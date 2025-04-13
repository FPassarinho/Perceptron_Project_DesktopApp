import time
import os
import glob
from conversion_functions import *

#O código está preparado para ler matrizes unidmensionais, então não se pode guardar os dados em bidimensional, 
# caso se guarde que é o caso, têm de se realizar a conversão de dados para unidmensional.

#Constants
NUM_PIXELS_AMOSTRA = 10800 #número de pixeis de cada imagem 120*90
DIR_PATH_DATA_FILE = 'data_file'
DIR_PATH_TEST = 'test_images'

# Activation of weights & bias
weights = np.random.uniform(-0.05, 0.05, NUM_PIXELS_AMOSTRA)
bias = 0

#O número de Training Epochs indica quantas vezes o modelo passará por todo o conjunto de dados de treino durante o treino
# (10–50) for small datasets, 50–200 for medium datasets, 100–500+ for large datasets) 
#O learning rate determina o quão grande ou pequeno será o ajuste dos pesos do modelo a cada iteração do treinamento.
#Se a taxa de aprendizagem for muito alta, o modelo pode não convergir ou saltar para uma solução sub ótima.
#Se for muito baixa, o modelo pode demorar muito para aprender, ou ficar preso em um mínimo local (convergir muito lentamente).
# Valores pequenos:  (0.00001 a 0.001)
# Valores médios:  (0.001 a 0.01)
# # Valores altos:  (0.1 a 1.0)
###quantas mais imagens existirem, mais epochs são necessários para rodar as imagens
list_functions_options = [
  {"id":1, "function": "SIGMOID", "num_epochs": 450, "learning_rate": 0.01},
  {"id":2, "function": "SIGMOID", "num_epochs": 950, "learning_rate": 0.005},
  {"id":3, "function": "SIGMOID", "num_epochs": 4600, "learning_rate": 0.001},
  {"id":4, "function": "STEP_FUNCTION", "num_epochs": 20, "learning_rate": 0.01},
  {"id":5, "function": "STEP_FUNCTION", "num_epochs": 350, "learning_rate": 0.00001}
]
### SIGMOID FUNCTION
###  EPOCHS - 450 / LEARNING RATE - 0.01 //// TIME -  ///Battery - 15,44 seconds
### EPOCHS - 950 / LEARNING RATE - 0.005 //// TIME -   /// Battery - 30,55 seconds
### EPOCHS - 4600 / LEARNING RATE - 0.001 //// TIME -  /// Battery - 125 seconds
#### STEP-FUNCTION
### EPOCHS - 20 / LEARNING RATE - 0.01 //// TIME - 0,24 seconds /// Battery - 2.36 segundos
### EPOCHS - 350 / LEARNING RATE - 0.00001 //// TIME - 4,88 seconds /// Battery - 14,18 segundos

###### Dataset List
list_dataset = [
  {"id":1, "dataset": "datasetA"},
  {"id":2, "dataset": "datasetK"},
  {"id":3, "dataset": "datasetSTOP"}
]

##############################################
### Função calculo da ativaçao do neuronio ###
##############################################
def activation_function(function, soma_dos_pesos_amostra):
  if function == 'STEP_FUNCTION':
    return np.where(soma_dos_pesos_amostra >= 0, 1, 0)
  elif function == 'SIGMOID':
    return 1 / (1 + np.exp(-soma_dos_pesos_amostra))  

##########################
### Função de predição ###
##########################
def predict(function, input):
  return activation_function(function, np.dot(weights, input) + bias)

##############
### Treino ###
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
  print("\n3 - Left the program")

def templatePerceptron():
  print("\nChoose the function and options that you pretend!\n")
  print("\n1 - Sigmoid / 450 epochs / 0.01 learning Rate")
  print("\n2 - Sigmoid / 950 epochs / 0.005 learning Rate")
  print("\n3 - Sigmoid / 4600 epochs / 0.001 learning Rate")
  print("\n4 - Step_Function / 20 epochs / 0.01 learning Rate")
  print("\n5 - Step_Function / 350 epochs / 0.00001 learning Rate")
  print("\n6 - Left the program ")
  
############
### Main ###
############
if __name__ == "__main__":
  #Menu, and definition of dataset, function, num_epochs and learning_rate
  templateDataset()
  while True:
    numberDataset = int(input("\nYour opttion -> : "))
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
    numberMenu = int(input("\nYour opttion -> : "))
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

  #Counting the number of train and test samples
  num_train_samples = countImages(dir_path=dataset)
  num_test_samples = countImages(dir_path=DIR_PATH_TEST)

  # O train labels servem para dizer caso as imagens que se encontram como train_samples são A ou não mas no projeto isso não se pretende pois partimos do pressuposto que todas são A 
  # então vamos ter tudo a 1, se houvesse algumas que não fossem meteriamos a 0.
  train_labels = np.zeros(num_train_samples, dtype=int)
  # Define os intervalos onde os labels devem ser 1 (Isto permite indicar no dataset onde de facto é A ou a)
  n = int(num_train_samples/2)
  train_labels[:n] = 1  

  
  start = time.time()

  #Verifing if the program have all the files needed
  if len(os.listdir(DIR_PATH_DATA_FILE)) < 3:
    files = glob.glob(os.path.join(DIR_PATH_DATA_FILE, '*'))
    for f in files:
      os.remove(f)
    loadStoreImagesFileTrain(num_train_samples, dir_path=dataset) 
    loadStoreImagesFileNpz(num_train_samples, dir_path=dataset) 
    loadStoreImagesFileTest(num_test_samples, dir_path=DIR_PATH_TEST)

  # Obtenção dos dados do Ficheiro NPZ
  train_data = [];
  with np.load('data_file/image_data.npz') as data:
    for key in data.files:
      train_data.append(data[key]);
    
  # Resize e conversão das imagens de teste
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