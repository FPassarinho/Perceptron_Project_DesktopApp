import numpy as np
import os
from PIL import Image

# Conta o número de imagens 
def countImages(dir_path):
  count = 0
  for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      count += 1
  return count

# Dá resize é imagem
def resize_image(ount, open_dir_path, open_dir_path_resize):
  image = Image.open
  return


# Carrega a imagem original
def loadStoreImagesFile(count, open_dir_path):
  for i in range(1, count):
    image = Image.open(f"{open_dir_path}/img011-{i}.png");
    image = image.convert("L")  # Converter para escala de cinza   ->  # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(image)  
    pixel_matrix[pixel_matrix < 127] = 3
    pixel_matrix[pixel_matrix >= 127] = 255
    with open(f'data_file/pixel_data.txt', 'w') as file:
      file.write('[\n');
      for i in range(1, count):
        file.write('[\n');
        for row in pixel_matrix:
          file.write(', '.join(map(str, row)) + '\n');
        file.write('],\n');  
      file.write(']\n');

def loadStoreImages(count, open_dir_path):
  images_data = []
  for i in range(1, count):
    image = Image.open(f"{open_dir_path}/img011-{i}.png");
    image = image.convert("L")  # Converter para escala de cinza -> # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(image)  
    pixel_matrix[pixel_matrix < 127] = 3
    pixel_matrix[pixel_matrix >= 127] = 255
    images_data.append(pixel_matrix)
  return images_data