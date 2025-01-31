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

# Dá resize à imagem (é necessário um path para definir onde elas vão guardadas)
def resize_images(count, dir_path, dir_path_resize):
  for i in range(1, count + 1):
    image = Image.open(f"{dir_path}/img011-{i}.png")
    new_image = image.resize((120, 90))
    original_filename = (f"img011-{i}.png")
    save_path = os.path.join(dir_path_resize, original_filename)
    new_image.save(save_path)
  return

# Guarda as Imagens em Matrizes num ficheiro TXT
def loadStoreImagesFile(count, dir_path):
  with open(f'data_file/pixel_data.txt', 'w') as file:
    file.write('[\n');

    for i in range(1, count + 1):
      image = Image.open(f"{dir_path}/img011-{i}.png");
      new_image = image.resize((120, 90));
      new_image = new_image.convert("L")# Converter para escala de cinza   ->  # Converte a imagem para escala de cinza e acessa os dados dos pixels
      pixel_matrix = np.array(new_image)  
      pixel_matrix[pixel_matrix < 127] = 0
      pixel_matrix[pixel_matrix >= 127] = 1
      file.write('  [\n');
      for row in pixel_matrix:
        file.write('  ' + '  ' + ' '.join(map(str, row)) + '\n');
      file.write('  ],\n');  
    file.write(']\n');

def loadStoreImagesFileNpz(count, dir_path):
  image_dict = {}
  for i in range(1, count + 1):
    image = Image.open(f"{dir_path}/img011-{i}.png");
    new_image = image.resize((120, 90));
    new_image = new_image.convert("L")  # Converter para escala de cinza   ->  # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(new_image)  
    pixel_matrix[pixel_matrix < 127] = 0
    pixel_matrix[pixel_matrix >= 127] = 1

    image_dict[f"img011-{i}"] = pixel_matrix

  np.savez("data_file/image_data.npz", **image_dict)

def loadStoreImages(count, dir_path):
  images_data = []
  for i in range(1, count + 1):
    image = Image.open(f"{dir_path}/img011-{i}.png");
    new_image = image.resize((120, 90));
    new_image = new_image.convert("L")  # Converter para escala de cinza -> # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(new_image)  
    pixel_matrix[pixel_matrix < 127] = 0
    pixel_matrix[pixel_matrix >= 127] = 1

    flattened_pixels = pixel_matrix.flatten()

    images_data.append(flattened_pixels)

  return images_data