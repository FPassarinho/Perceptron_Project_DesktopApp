import numpy as np
import os
import cv2
from PIL import Image

# In the for loop, it starts at 0 and ends at count because 0 is the first position,
# as the images are numbered like vectors.
# Count is used because the for loop is non-inclusive, so if count is 3410, it will write up to 3409, which is what we want.

# Counts the number of images
def countImages(dir_path):
  count = 0
  for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      count += 1
  return count

# Resizes the image (requires a path to define where they will be saved)
def resize_images(count, dir_path, dir_path_resize):
  for i in range(0, count):
    image = Image.open(f"{dir_path}/img-{i}.png")
    new_image = image.resize((120, 90))
    original_filename = (f"img011-{i}.png")
    save_path = os.path.join(dir_path_resize, original_filename)
    new_image.save(save_path)
  return

# Function that centers the image in the array
def center_array_image(pixel_matrix):
  data = pixel_matrix.flatten()
  first_index = next((i for i, x in enumerate(data) if x > 0), None)
  last_index = 10800 - 1 - next((i for i, x in enumerate(reversed(data)) if x > 0), None)

  sub_arr = [0.0] * 10800
  if (last_index - first_index) % 2 != 0:
    count = (10800 - (last_index - first_index + 1)) // 2
    sub_arr[count:count + (last_index - first_index + 1)] = data[first_index:last_index + 1]
  elif (last_index - first_index) % 2 == 0:
    count = (10800 - (last_index - first_index)) // 2
    sub_arr[count:count + (last_index - first_index + 1)] = data[first_index:last_index + 1]

  return sub_arr

# Saves images as matrices in a TXT file for training
def loadStoreImagesFileTrain(count, dir_path, word):
  with open(f'data_file/pixel_data{word}.txt', 'w') as file:
    file.write('[\n');

    for i in range(0, count):
      image = Image.open(f"{dir_path}/img-{i}.png");
      new_image = image.resize((120, 90));
      new_image = new_image.convert("L")  # Convert to grayscale
      pixel_matrix = np.array(new_image)
      pixel_matrix = 1 - pixel_matrix / 255.0

      centered_matrix = center_array_image(pixel_matrix)

      file.write('  [\n');
      file.write('\t\t' + ' '.join(map(str, centered_matrix)))
      file.write('  ],\n');
    file.write(']\n');

# Saves images as matrices in a TXT file for testing
def loadStoreImagesFileTest(count, dir_path, word):
  with open(f'data_file/pixel_data_test{word}.txt', 'w') as file:
    file.write('[\n');

    for i in range(0, count):
      image = Image.open(f"{dir_path}/img-{i}.png");
      new_image = image.resize((120, 90));
      new_image = new_image.convert("L")  # Convert to grayscale
      pixel_matrix = np.array(new_image)
      pixel_matrix = 1 - pixel_matrix / 255.0

      centered_matrix = center_array_image(pixel_matrix)

      file.write('  [\n');
      file.write('\t\t' + ' '.join(map(str, centered_matrix)))
      file.write('  ],\n');
    file.write(']\n');

# Saves images in a compressed .npz format
def loadStoreImagesFileNpz(count, dir_path, word):
  image_dict = {}
  for i in range(0, count):
    image = Image.open(f"{dir_path}/img-{i}.png");
    new_image = image.resize((120, 90));
    new_image = new_image.convert("L")  # Convert to grayscale
    pixel_matrix = np.array(new_image)
    pixel_matrix = 1 - pixel_matrix / 255.0

    centered_matrix = center_array_image(pixel_matrix)

    image_dict[f"img011-{i}"] = centered_matrix

  np.savez(f"data_file/image_data{word}.npz", **image_dict)

# Loads and stores images for testing (returns list of pixel arrays)
def loadStoreImages(count, dir_path):
  images_data = []
  for i in range(0, count):
    image = Image.open(f"{dir_path}/img-{i}.png");
    new_image = image.resize((120, 90));
    new_image = new_image.convert("L")  # Convert to grayscale
    pixel_matrix = np.array(new_image)
    pixel_matrix = 1 - pixel_matrix / 255.0

    centered_matrix = center_array_image(pixel_matrix)

    images_data.append(centered_matrix)

  return images_data

# Function to take a picture from the webcam
def takePicture():
  dir_path_train = 'test_images'
  cam = cv2.VideoCapture(0)
  cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  result, image = cam.read()
  count = countImages(dir_path_train)  # just count, since the image numbers match their position in the vector
                                       # this makes the image number one less than the total

  if result:
    cv2.imshow("Photo", image);
    cv2.imwrite(f"test_images/img-{count}.png", image);
    cv2.waitKey(0)
    cv2.destroyWindow("Photo")
  else:
    print("No image detected");

  cam.release()
  cv2.destroyAllWindows()

# Function to rename file names
def rename():
  folder = r"---"

  files = sorted(os.listdir(folder))

  for i, file in enumerate(files, start=155):
    extension = os.path.splitext(file)[1]
    new_name = f"img-{i}{extension}"
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)