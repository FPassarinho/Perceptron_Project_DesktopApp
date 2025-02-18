##################################################################################
#### Resize de imagens, e conversão de imagens que compoêm as training samples ###
##################################################################################

from conversion_functions import *

# PATH Train / PATH Test
dir_path_train = 'dataset'
dir_path_test = 'test_images'

train_samples = countImages(dir_path=dir_path_train)
test_samples = countImages(dir_path=dir_path_test)

#Resize de Imagens, Conversão para pixeis e armazenação num ficheiro TXT das imagens de treino
loadStoreImagesFileTrain(train_samples, dir_path=dir_path_train) 
#Resize de Imagens, Conversão para pixeis e armazenação num ficheiro NPZ
loadStoreImagesFileNpz(train_samples, dir_path=dir_path_train) 
#Resize de Imagens, Conversão para pixeis e armazenação num ficheiro TXT das imagens de teste
loadStoreImagesFileTest(test_samples, dir_path=dir_path_test)

#Tirar foto
# takePicture() 

#Rename dataset
# rename()