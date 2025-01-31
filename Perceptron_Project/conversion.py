##################################################################################
#### Resize de imagens, e conversão de imagens que compoêm as training samples ###
##################################################################################

from conversion_functions import *

# PATH Train / pATH Test
dir_path_train = 'images'
dir_path_test = 'test_images'

train_samples = countImages(dir_path=dir_path_train)
test_samples = countImages(dir_path=dir_path_test)

#Resize de Imagens, Conversão para pixeis e armazenação num ficheiro TXT
loadStoreImagesFile(train_samples, dir_path=dir_path_train) 
#Resize de Imagens, Conversão para pixeis e armazenação num ficheiro NPZ
loadStoreImagesFileNpz(train_samples, dir_path=dir_path_train) 