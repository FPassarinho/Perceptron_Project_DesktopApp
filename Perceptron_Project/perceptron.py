import time
from conversion_functions import *

#O código está preparado para ler matrizes unidmensionais, então não se pode guardar os dados em bidimensional, 
# caso se guarde que é o caso, têm de se realizar a conversão de dados para unidmensional.

DIR_PATH_TRAIN = 'dataset'
DIR_PATH_TEST= 'test_images'
NUM_PIXELS_AMOSTRA = 10800 #número de pixeis de cada imagem 120*90
NUM_TRAIN_SAMPLES = countImages(dir_path=DIR_PATH_TRAIN)
NUM_TEST_SAMPLES = countImages(dir_path=DIR_PATH_TEST)

# Pesos & Bias
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
list_functions_options = [
  {"id":1, "function": "SIGMOID", "num_epochs": 350, "learning_rate": 0.01},
  {"id":2, "function": "SIGMOID", "num_epochs": 700, "learning_rate": 0.005},
  {"id":3, "function": "SIGMOID", "num_epochs": 3500, "learning_rate": 0.001},
  {"id":4, "function": "STEP_FUNCTION", "num_epochs": 20, "learning_rate": 0.01},
  {"id":5, "function": "STEP_FUNCTION", "num_epochs": 400, "learning_rate": 0.00001}
]

### SIGMOID FUNCTION
### EPOCHS - 350 / LEARNING RATE - 0.01 //// TIME - 3,61 seconds
### EPOCHS - 700 / LEARNING RATE - 0.005 //// TIME - 7,61 seconds
### EPOCHS - 3500 / LEARNING RATE - 0.001 //// TIME - 38,58 seconds /// Bateria - 98,41
#### STEP-FUNCTION
### EPOCHS - 20 / LEARNING RATE - 0.01 //// TIME - 0,24 seconds
### EPOCHS - 400 / LEARNING RATE - 0.00001 //// TIME - 4,88 seconds


###Funções de conversão
# loadStoreImagesFileTrain(NUM_TRAIN_SAMPLES, dir_path=dir_path_train) 
# loadStoreImagesFileNpz(NUM_TRAIN_SAMPLES, dir_path=dir_path_train) 
# loadStoreImagesFileTest(NUM_TEST_SAMPLES, dir_path=dir_path_test)


# O train labels servem para dizer caso as imagens que se encontram como train_samples são A ou não mas no projeto isso não se pretende pois partimos do pressuposto que todas são A 
# então vamos ter tudo a 1, se houvesse algumas que não fossem meteriamos a 0.
train_labels = np.zeros(NUM_TRAIN_SAMPLES, dtype=int)
# Define os intervalos onde os labels devem ser 1 (Isto permite indicar no dataset onde de facto é A ou a)
train_labels[:54] = 1  

# Obtenção dos dados do Ficheiro NPZ
train_data = [];
data = np.load('data_file/image_data.npz')
for key in data.files:
  train_data.append(data[key]);

# Resize e conversão das imagens de teste
test_data = loadStoreImages(NUM_TEST_SAMPLES, dir_path=DIR_PATH_TEST)  

##############################################
### funçao calculo da ativaçao do neuronio ###
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
    for sample in range(NUM_TRAIN_SAMPLES):
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
def template():
  print("\nWelcome to perceptron, choose the function and options that you pretend!\n")
  print("\n1 - Sigmoid / 350 epochs / 0.01 learning Rate")
  print("\n2 - Sigmoid / 700 epochs / 0.005 learning Rate")
  print("\n3 - Sigmoid / 3500 epochs / 0.001 learning Rate")
  print("\n4 - Step_Function / 20 epochs / 0.01 learning Rate")
  print("\n5 - Step_Function / 400 epochs / 0.00001 learning Rate")
  
############
### Main ###
############
if __name__ == "__main__":
  template()
  numberMenu = int(input("\nYour opttion -> : "))

  for option in list_functions_options:
    if option["id"] == numberMenu:
      num_epochs = option["num_epochs"]
      learning_rate = option["learning_rate"]
      function = option["function"]
  
  start = time.time()
  train(num_epochs, learning_rate, function)

  for i in range(NUM_TEST_SAMPLES):
    print(f"\n\nTesting image {i+1}... ")

    prediction = predict(function, test_data[i])
    if function == "SIGMOID":
      print("\n\n *** ESTE PERCEPTRON considera que é um A quando a certeza for maior que 0.8 ***\n");
      prediction_percentage = prediction * 100;

      if prediction_percentage >= 80:
        print(f"\nAcho que é um A com {prediction_percentage:.2f} por cento de certeza\n")
      else:
        print(f"\nAcho que não é um A com {100-prediction_percentage:.2f} por cento de certeza\n")
    
    elif function == "STEP_FUNCTION":
      if prediction == 1:
        print(f"\nAcho que é um A.\n")
      else:
        print(f"\nAcho que não é um A.\n")

  end = time.time()
  print(f"Tempo de execução = {end - start:.2f} segundo");