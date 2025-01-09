import math
import random
import array as arr
from conversion_functions import *

dir_path_train = 'resize_images'
dir_path_test= 'resize_test_images'

train_samples = countImages(dir_path=dir_path_train)
test_number = countImages(dir_path=dir_path_test)

INPUT_SIZE = 10800 #número de pixeis de cada imagem 120*90
NUM_TRAIN_SAMPLES = train_samples
NUM_TEST_SAMPLES = test_number
NUM_EPOCHS = 1000
LEARNING_RATE = 0.01

test_labels = arr.array('i', [1,1,0,0,0,0]);

train_labels = arr.array('i',[
	1,1,1,1,1,1,1,1,1,
	0,0,0,0,0,0,0,0,0
]);

# Abertura de dados do ficheiro TXT.
#train_data = open('data_file/pixel_data.txt', 'r').readlines() ###ERRO####

# Imagem de Teste que pretende ser convertida
test_data = loadStoreImages(test_number, dir_path=dir_path_test)   ### está a guardar tudo numa linha
train_data = loadStoreImages(train_samples, dir_path=dir_path_train)

weights = [0] * INPUT_SIZE #vetor de pesos    

##############################################
### funçao calculo da ativaçao do neuronio ###
##############################################
def activation_function(soma_dos_pesos_amostra):
  # soma_dos_pesos_amostra = soma ponderada dos pixels de uma amostra
  sig = 1.0 / (1 + math.exp(-soma_dos_pesos_amostra))
  return sig

##########################
### Função de predição ###
##########################
def predict(input = []):
  sum = float(0);
  assert len(input) == INPUT_SIZE, f"Erro: tamanho do input ({len(input)}) diferente de INPUT_SIZE ({INPUT_SIZE})."
  for i in range(1,INPUT_SIZE):
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
    if prediction > 0.8:
      print(f"\nAcho que é um A com {prediction} por cento de certeza\n");
    else:
      print(f"\nAcho que não é um A com {1-prediction}por cento de certeza\n");

  return 0

main()