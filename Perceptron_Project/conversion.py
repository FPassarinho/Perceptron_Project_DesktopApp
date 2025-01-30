##################################################################################
#### Resize de imagens, e conversão de imagens que compoêm as training samples ###
##################################################################################

from conversion_functions import *

#Train
dir_path_train = 'images'
dir_path_train_resize = 'resize_images'

#Test
dir_path_test = 'test_images'
dir_path_test_resize = 'resize_test_images'

train_samples = countImages(dir_path=dir_path_train)
test_samples = countImages(dir_path=dir_path_test)

#Conversão de tamanho de imagens de treino
resize_images(train_samples, dir_path=dir_path_train, dir_path_resize=dir_path_train_resize)

#Conversão de imagens de tamanho de imagens de teste
resize_images(test_samples, dir_path=dir_path_test, dir_path_resize=dir_path_test_resize)

#Conversão de imagens para ficheiro txt
loadStoreImagesFile(train_samples, dir_path=dir_path_train_resize) 

loadStoreImagesFileNpz(train_samples, dir_path=dir_path_train_resize) 