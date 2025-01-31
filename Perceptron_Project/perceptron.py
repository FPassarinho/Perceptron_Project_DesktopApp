import math
import random
import array as arr
from conversion_functions import *

#O código está preparado para ler matrizes unidmensionais, então +e por que não se pode guardar os dados em bidimensional, 
# caso se guarde que é o caso, têm de se realizar a conversão de dados para unidmensional.
dir_path_train = 'images'
dir_path_test= 'test_images'

train_samples = countImages(dir_path=dir_path_train)
test_number = countImages(dir_path=dir_path_test)

INPUT_SIZE = 10800 #número de pixeis de cada imagem 120*90
NUM_TRAIN_SAMPLES = train_samples
NUM_TEST_SAMPLES = test_number 
#O número de Training Epochs indica quantas vezes o modelo passará por todo o conjunto de dados de treino durante o treino
NUM_EPOCHS = 50 #(10–50 for small datasets, 50–200 for medium datasets, 100–500+ for large datasets) 
LEARNING_RATE = 0.01

# O tran labels serve para dizzer caso as imagens que se encontram como train_samples são A ou não mas no projeto isso não se pretende pois partimos do pressuposto que todas são A 
# então vamos ter tudo a 1, se houvesse algumas que não fossem meteriamos a 0.
# A ideia aplica-se a ambos
test_labels = arr.array('i', [1] * NUM_TEST_SAMPLES);
train_labels = arr.array('i', [1] * NUM_TRAIN_SAMPLES)

# Obtenção dos dados do Ficheiro NPZ
train_data = [];
data = np.load('data_file/image_data.npz')
for key in data.files:
  train_data.append(data[key].flatten());

# Resize e conversão das imagens de teste
test_data = loadStoreImages(test_number, dir_path=dir_path_test)  

# Definição dos pessos
weights = [0] * INPUT_SIZE #vetor de pesos    

##############################################
### funçao calculo da ativaçao do neuronio ###
##############################################
def activation_function(soma_dos_pesos_amostra):
  # soma_dos_pesos_amostra = soma ponderada dos pixels de uma amostra
  sig = float(1.0 / (1 + math.exp(-soma_dos_pesos_amostra)))
  return sig

##########################
### Função de predição ###
##########################
def predict(input = []):
  sum = float(0);
  for i in range(INPUT_SIZE):
    sum += weights[i] * input[i];
  return activation_function(sum);

##############
### Treino ###
##############
def train():
  for epoch in range(NUM_EPOCHS):
    for sample in range(NUM_TRAIN_SAMPLES):
      prediction = float(predict(train_data[sample]))
      error = float(train_labels[sample] - prediction)
      for i in range (INPUT_SIZE):
        weights[i] += LEARNING_RATE * error * train_data[sample][i]

############
### Main ###
############
def main():
  for i in range(INPUT_SIZE):
    weights[i] = (0.10 * random.random() - 0.05)

  train()
  for i in range(NUM_TEST_SAMPLES):
    print(f"\n\nTesting image {i}... ")

    prediction = float(predict(test_data[i]))

    prediction_percentage = prediction * 100;

    if prediction_percentage > 80:
      print(f"\nAcho que é um A com {prediction_percentage:.2f} por cento de certeza\n");
    else:
      print(f"\nAcho que não é um A com {100-prediction_percentage:.2f}por cento de certeza\n");

  return 0

main()