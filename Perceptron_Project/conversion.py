from conversion_functions import *

open_dir_path_train = 'images'
dir_path = 'images'

train_samples = countImages(dir_path=dir_path)

#Conversão de imagens para ficheiro txt
loadStoreImagesFile(train_samples, open_dir_path=open_dir_path_train)