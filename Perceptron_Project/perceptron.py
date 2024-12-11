import math
import random
import array as arr
from conversion_functions import *

open_dir_path_test = 'test_images'
dir_path_test = 'test_images'
dir_path_train = 'images'

train_samples = countImages(dir_path=dir_path_train)
test_number = countImages(dir_path=dir_path_test)

INPUT_SIZE = 1080000
NUM_TRAIN_SAMPLES = train_samples
NUM_TEST_SAMPLES = test_number
NUM_EPOCHS = 1000
LEARNING_RATE = 0.01

test_labels = arr.array('i', [255,255,3,3,3,3]);

train_labels = arr.array('i',[
	255,255,255,255,255,255,255,255,255,
	3,3,3,3,3,3,3,3,3
]);

# Abertura de dados do ficheiro TXT.
train_data = open('data_file/pixel_data.txt', 'r').readlines()

# Imagem de Teste que pretende ser conveertida
test_data = loadStoreImages(test_number, open_dir_path=open_dir_path_test)

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