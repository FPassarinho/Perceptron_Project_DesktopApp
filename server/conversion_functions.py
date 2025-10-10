import numpy as np
import os
import re
import json
from PIL import Image

# ------------------------------------------------------------
# Utility Functions for Handling Image Datasets
# ------------------------------------------------------------

# Counts the number of image files in a directory
# Useful for knowing how many images exist for training/testing
def countImages(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count

# Resizes images to a fixed size (120x90) and saves them in a target directory
# count: number of images to process
# dir_path: source directory
# dir_path_resize: destination directory
def resize_images(count, dir_path, dir_path_resize):
    for i in range(0, count):
        image = Image.open(f"{dir_path}/img-{i}.png")
        new_image = image.resize((120, 90))  # Resize to 120x90 pixels
        original_filename = f"img011-{i}.png"
        save_path = os.path.join(dir_path_resize, original_filename)
        new_image.save(save_path)
    return

# Centers the pixel values of an image array inside a 1D array
# Ensures that the letter is centered in the vector, which helps the perceptron learn better
def center_array_image(pixel_matrix):
    data = pixel_matrix.flatten()  # Flatten 2D image to 1D
    first_index = next((i for i, x in enumerate(data) if x > 0), None)
    last_index = 10800 - 1 - next((i for i, x in enumerate(reversed(data)) if x > 0), None)

    sub_arr = [0.0] * 10800  # Initialize empty centered array
    if (last_index - first_index) % 2 != 0:
        count = (10800 - (last_index - first_index + 1)) // 2
        sub_arr[count:count + (last_index - first_index + 1)] = data[first_index:last_index + 1]
    elif (last_index - first_index) % 2 == 0:
        count = (10800 - (last_index - first_index)) // 2
        sub_arr[count:count + (last_index - first_index + 1)] = data[first_index:last_index + 1]

    return sub_arr

# ------------------------------------------------------------
# Functions for Storing Images in Files
# ------------------------------------------------------------
# Saves images in a compressed .npz format (faster to load than TXT)
def loadStoreImagesFileNpz(count, dir_path, word):
    image_dict = {}
    for i in range(count):
        image = Image.open(f"{dir_path}/img-{i}.png")
        new_image = image.resize((120, 90))
        new_image = new_image.convert("L")
        pixel_matrix = np.array(new_image)
        pixel_matrix = 1 - pixel_matrix / 255.0

        centered_matrix = center_array_image(pixel_matrix)
        image_dict[f"img011-{i}"] = centered_matrix

    base_path = os.path.dirname(os.path.abspath(__file__))  # server/
    data_file_dir = os.path.join(base_path, "data_file")
    os.makedirs(data_file_dir, exist_ok=True)

    np.savez(os.path.join(data_file_dir, f"image_data{word}.npz"), **image_dict)


# Loads images from directory
def loadStoreImages(count, dir_path):
    images_data = []
    for i in range(0, count):
        image = Image.open(f"{dir_path}/img-{i}.png")
        new_image = image.resize((120, 90))
        new_image = new_image.convert("L")
        pixel_matrix = np.array(new_image)
        pixel_matrix = 1 - pixel_matrix / 255.0

        centered_matrix = center_array_image(pixel_matrix)
        images_data.append(centered_matrix)

    return images_data

# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

# Extracts the number from a filename for proper sorting (img-1, img-2, etc.)
def numerical_sort(value):
    match = re.search(r'(\d+)', value)
    return int(match.group(0)) if match else -1

# Renames images in a folder sequentially (img-0.png, img-1.png, ...)
# Useful after deleting images to maintain consistent numbering
def rename_images(folder):
    files = sorted(
        [f for f in os.listdir(folder) if f.lower().endswith(".png")],
        key=numerical_sort
    )
    for i, file in enumerate(files):
        extension = os.path.splitext(file)[1]
        new_name = f"img-{i}{extension}"
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, new_name)
        if old_path != new_path:
            os.rename(old_path, new_path)

# ------------------------------------------------------------
# Generic rename function
# ------------------------------------------------------------
def rename():
    folder = r"---"  # Replace with your dataset folder

    files = sorted(os.listdir(folder))
    for i, file in enumerate(files, start=0):
        extension = os.path.splitext(file)[1]
        new_name = f"img-{i}{extension}"
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)

## Uncomment to run dataset renaming
# rename()

# ------------------------------------------------------------
# Function to generate .npz for all datasets (development only)
# ------------------------------------------------------------
def generate_all_npz_local(datasets_json="datasets.json", datasets_base_path="datasets", data_file_dir="data_file"):
    """
    Creates .npz files for all datasets listed in the local JSON file.
    Should be used only locally for development. Does NOT run automatically.
    """
    # Base path = folder where this script lives (server/)
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Absolute paths inside server/
    datasets_json_path = os.path.join(base_path, datasets_json)
    datasets_base_path = os.path.join(base_path, datasets_base_path)
    data_file_dir = os.path.join(base_path, data_file_dir)
    
    os.makedirs(data_file_dir, exist_ok=True)

    # Load the list of datasets
    with open(datasets_json_path, "r") as f:
        list_dataset = json.load(f)

    for dataset_info in list_dataset:
        dataset_name = dataset_info["dataset"]
        word = dataset_info["word"]
        dataset_path = os.path.join(datasets_base_path, dataset_name)
        npz_path = os.path.join(data_file_dir, f"image_data{word}.npz")

        if not os.path.exists(npz_path):
            num_images = countImages(dataset_path)
            print(f"[DEV] Creating .npz for dataset '{dataset_name}' ({num_images} images)...")
            loadStoreImagesFileNpz(num_images, dataset_path, word)
        else:
            print(f"[DEV] .npz already exists for '{dataset_name}', skipping...")

generate_all_npz_local()