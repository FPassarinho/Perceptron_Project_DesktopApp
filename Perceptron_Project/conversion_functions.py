import numpy as np
import os
import cv2
from PIL import Image

# No for começa com 0 e acaba no count pois 0 é a primeira posição pois as imagens tão numeradas como se fossem vetores e 
#Count pois como no for o count não é inclusive se o count for 3410 ele vai escreve 3409, que é o que pretendemos 

# Conta o número de imagens 
def countImages(dir_path):
  count = 0
  for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      count += 1
  return count

# Dá resize à imagem (é necessário um path para definir onde elas vão guardadas)
def resize_images(count, dir_path, dir_path_resize):
  for i in range(0, count):
    image = Image.open(f"{dir_path}/img-{i}.png")
    new_image = image.resize((120, 90))
    original_filename = (f"img011-{i}.png")
    save_path = os.path.join(dir_path_resize, original_filename)
    new_image.save(save_path)
  return

# Função que centra a imagem no array
def center_array_image(pixel_matrix):
  data = pixel_matrix.flatten()
  first_index = next((i for i, x in enumerate(data) if x > 0), None)
  last_index = 10800 - 1 - next((i for i, x in enumerate(reversed(data)) if x > 0), None)

  sub_arr = [0.0] * 10800
  if (last_index - first_index) % 2 != 0:
    count = (10800 - (last_index - first_index + 1)) // 2
    sub_arr[count:count + (last_index - first_index + 1)] = data[first_index:last_index + 1]
  elif (last_index - first_index) % 2 == 0:
    count = (10800 - (last_index - first_index + 1)) // 2
    sub_arr[count:count + (last_index - first_index + 1)] = data[first_index:last_index + 1]

  return sub_arr

# Guarda as Imagens em Matrizes num ficheiro TXT, de treino
def loadStoreImagesFileTrain(count, dir_path):
  with open(f'data_file/pixel_data.txt', 'w') as file:
    file.write('[\n');

    for i in range(0, count):
      image = Image.open(f"{dir_path}/img-{i}.png");
      new_image = image.resize((120, 90));
      new_image = new_image.convert("L")# Converter para escala de cinza   ->  # Converte a imagem para escala de cinza e acessa os dados dos pixels
      pixel_matrix = np.array(new_image)  
      pixel_matrix = 1 - pixel_matrix / 255.0

      centered_matrix = center_array_image(pixel_matrix);

      file.write('  [\n');
      file.write('\t\t' + ' '.join(map(str, centered_matrix)))
      file.write('  ],\n');  
    file.write(']\n');

# Guarda as Imagens em Matrizes num ficheiro TXT, de teste
def loadStoreImagesFileTest(count, dir_path):
  with open(f'data_file/pixel_data_test.txt', 'w') as file:
    file.write('[\n');

    for i in range(0, count):
      image = Image.open(f"{dir_path}/img-{i}.png");
      new_image = image.resize((120, 90));
      new_image = new_image.convert("L")# Converter para escala de cinza   ->  # Converte a imagem para escala de cinza e acessa os dados dos pixels
      pixel_matrix = np.array(new_image)  
      pixel_matrix = 1 - pixel_matrix / 255.0

      centered_matrix = center_array_image(pixel_matrix);

      file.write('  [\n');
      file.write('\t\t' + ' '.join(map(str, centered_matrix)))
      file.write('  ],\n');  
    file.write(']\n');

def loadStoreImagesFileNpz(count, dir_path):
  image_dict = {}
  for i in range(0, count):
    image = Image.open(f"{dir_path}/img-{i}.png");
    new_image = image.resize((120, 90));
    new_image = new_image.convert("L")  # Converter para escala de cinza   ->  # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(new_image)  
    pixel_matrix = 1 - pixel_matrix / 255.0

    centered_matrix = center_array_image(pixel_matrix);

    image_dict[f"img011-{i}"] = centered_matrix

  np.savez("data_file/image_data.npz", **image_dict)

def loadStoreImages(count, dir_path):
  images_data = []
  for i in range(0, count):
    image = Image.open(f"{dir_path}/img-{i}.png");
    new_image = image.resize((120, 90));
    new_image = new_image.convert("L")  # Converter para escala de cinza -> # Converte a imagem para escala de cinza e acessa os dados dos pixels
    pixel_matrix = np.array(new_image)  
    pixel_matrix = 1 - pixel_matrix / 255.0

    centered_matrix = center_array_image(pixel_matrix);

    images_data.append(centered_matrix)

  return images_data

def takePicture():
  dir_path_train = 'test_images'
  cam = cv2.VideoCapture(0)
  cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  result, image = cam.read()
  count = countImages(dir_path_train)#é so count pois as imagens estão numeradas igual é sua posição nos vetores, isso faz com que o 
                                     #o número de imagem delas seja menos 1 do que o total delas.
                                     
  if result:
    cv2.imshow("Foto", image);
    cv2.imwrite(f"test_images/img-{count}.png", image);
    cv2.waitKey(0)
    cv2.destroyWindow("Foto")
  else:
    print("No image detected");

  cam.release()
  cv2.destroyAllWindows()

# Função de renomear os nomes dos ficheiros
def rename():
  pasta = r"C:\Filipe\Informatica_Faculdade\Investigacao\IA\Perceptron_Project\Perceptron_Project\dataset"  

  ficheiros = sorted(os.listdir(pasta))

  for i, ficheiro in enumerate(ficheiros, start=54):
    extensao = os.path.splitext(ficheiro)[1]  
    novo_nome = f"img-{i}{extensao}"  
    antigo_caminho = os.path.join(pasta, ficheiro)
    novo_caminho = os.path.join(pasta, novo_nome)
      
    os.rename(antigo_caminho, novo_caminho)