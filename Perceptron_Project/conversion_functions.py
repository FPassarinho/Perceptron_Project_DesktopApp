import numpy as np
import os
from PIL import Image

# No for aparece range + 1 porque assim considera o ultimo, por  exemplo 55 + 1 = <= 55. Sendo que quando é range(1, 55) é = < 55

# Conta o número de imagens 
def countImages(dir_path):
  count = 0
  for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      count += 1
  return count

# Dá resize à imagem
def resize_images(count, dir_path, dir_path_resize):
  for i in range(1, count + 1):
    image = Image.open(f"{dir_path}/img011-{i}.png")
    new_image = image.resize((120, 90))
    original_filename = (f"img011-{i}.png")
    save_path = os.path.join(dir_path_resize, original_filename)
    new_image.save(save_path)
  return

# Carrega a imagem original
def loadStoreImagesFile(count, dir_path):
  for i in range(1, count + 1):
    image = Image.open(f"{dir_path}/img011-{i}.png");
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

def loadStoreImages(count, dir_path):
  images_data = []
  for i in range(1, count + 1):
    image = Image.open(f"{dir_path}/img011-{i}.png");
    image = image.convert("L")  # Converter para escala de cinza -> # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(image)  
    pixel_matrix[pixel_matrix < 127] = 3
    pixel_matrix[pixel_matrix >= 127] = 255
    images_data.append(pixel_matrix)
  return images_data