import os.path
from conversion_functions import *

#O código está preparado para ler matrizes unidmensionais, então não se pode guardar os dados em bidimensional, 
# caso se guarde que é o caso, têm de se realizar a conversão de dados para unidmensional.
dir_path_train = 'dataset'
dir_path_test= 'test_images'

NUM_PIXELS_AMOSTRA = 10800 #número de pixeis de cada imagem 120*90
NUM_TRAIN_SAMPLES = countImages(dir_path=dir_path_train)
NUM_TEST_SAMPLES = countImages(dir_path=dir_path_test)
#O número de Training Epochs indica quantas vezes o modelo passará por todo o conjunto de dados de treino durante o treino
NUM_EPOCHS = 350 # (10–50) for small datasets, 50–200 for medium datasets, 100–500+ for large datasets) 
LEARNING_RATE = 0.01 #O learning rate determina o quão grande ou pequeno será o ajuste dos pesos do modelo a cada iteração do treinamento.
                    #Se a taxa de aprendizagem for muito alta, o modelo pode não convergir ou saltar para uma solução sub ótima.
                    #Se for muito baixa, o modelo pode demorar muito para aprender, ou ficar preso em um mínimo local (convergir muito lentamente).
                    # Valores pequenos:  (0.00001 a 0.001)
                    # Valores médios:  (0.001 a 0.01)
                    # Valores altos:  (0.1 a 1.0)

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
test_data = loadStoreImages(NUM_TEST_SAMPLES, dir_path=dir_path_test)  

# Pesos & Bias
weights = np.random.uniform(-0.05, 0.05, NUM_PIXELS_AMOSTRA)
bias = 0

##############################################
### funçao calculo da ativaçao do neuronio ###
##############################################
def activation_function(type, soma_dos_pesos_amostra):
  if type == 'STEP_FUNCTION':
    return np.where(soma_dos_pesos_amostra >= 0, 1, 0)
  elif type == 'SIGMOID':
    return 1 / (1 + np.exp(-soma_dos_pesos_amostra))  

##########################
### Função de predição ###
##########################
def predict(input):
  return activation_function('SIGMOID', np.dot(weights, input) + bias)

##############
### Treino ###
##############
def train():
  global bias
  global weights
  for epoch in range(NUM_EPOCHS):
    epoch_loss = 0
    for sample in range(NUM_TRAIN_SAMPLES):
      prediction = predict(train_data[sample])
      error = train_labels[sample] - prediction
      epoch_loss += error ** 2
      weights += LEARNING_RATE * error * train_data[sample]
      bias += LEARNING_RATE * error

    if epoch % 10 == 0:
      print(f"Epoch {epoch}: Loss = {epoch_loss:.4f}")

############
### Main ###
############
if __name__ == "__main__":
  train()

  print("\n\n *** ESTE PERCEPTRON considera que é um A quando a certeza for maior que 0.8 **\n");
  for i in range(NUM_TEST_SAMPLES):
    print(f"\n\nTesting image {i+1}... ")

    prediction = predict(test_data[i])

    prediction_percentage = prediction * 100;

    if prediction_percentage >= 80:
      print(f"\nAcho que é um A com {prediction_percentage:.2f} por cento de certeza\n");
    else:
      print(f"\nAcho que não é um A com {100-prediction_percentage:.2f} por cento de certeza\n");