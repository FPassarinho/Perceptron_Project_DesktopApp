import os
import sys
import json
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from perceptron import Perceptron
from conversion_functions import *

# ------------------------------
# Utility function to get absolute path
# ------------------------------
def resource_path(relative_path):
    """
    Get the absolute path to a resource, works for development and PyInstaller executable.
    PyInstaller uses a temporary folder (sys._MEIPASS) when frozen.
    """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller temporary folder
    else:
        base_path = os.path.abspath(".")  # Development path
    return os.path.join(base_path, relative_path)

# ------------------------------
# Paths for datasets, test images, and preprocessed data
# ------------------------------
datasets_json_path  = resource_path("datasets.json")
functions_json_path  = resource_path("functions_options.json")
test_images_path = resource_path("test_images")
data_file_path = resource_path("data_file")  # Folder for storing .npz files

# ------------------------------
# Initialize Flask app and enable CORS for cross-origin requests
# ------------------------------
app = Flask(__name__)
CORS(app)

# ------------------------------
# Load configuration JSON files
# - datasets.json: contains available datasets and corresponding words
# - functions_options.json: contains activation function options, learning rates, and epochs
# ------------------------------
with open(datasets_json_path, "r") as f:
    list_dataset = json.load(f)

with open(functions_json_path, "r") as f:
    list_functions_options = json.load(f)

# ------------------------------
# Define paths for uploaded images
# ------------------------------
base_path = os.path.dirname(os.path.abspath(__file__))
test_images_path = os.path.join(base_path, "test_images")
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "test_images")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists

# Base URL for serving images (used in frontend)
BASE_URL = "http://127.0.0.1:5000/server/test_images/"

# ------------------------------
# Endpoint: /predict
# - Receives JSON with dataset_id and function_id
# - Initializes perceptron with dataset, function, epochs, and learning rate
# - Trains the perceptron and returns evaluation results
# ------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    numberDataset = data["dataset_id"]
    numberFunction = data["function_id"]

    # ------------------------------
    # Retrieve dataset path and target word
    # ------------------------------
    for option in list_dataset:
        if option["id"] == numberDataset:
            dataset = option["dataset"]
            word = option["word"]
            dataset_path = os.path.join(base_path, "datasets", dataset)

    # ------------------------------
    # Retrieve function configuration: epochs, learning rate, activation function
    # ------------------------------
    for option in list_functions_options:
        if option["id"] == numberFunction:
            num_epochs = option["num_epochs"]
            learning_rate = option["learning_rate"]
            function = option["function"]

    # ------------------------------
    # Initialize, train, and evaluate perceptron
    # ------------------------------
    perceptron = Perceptron(
        learning_rate=learning_rate,
        num_epochs=num_epochs,
        dir_path_train=dataset_path,
        dir_path_test=test_images_path,
        function=function,
        word=word
    )
    perceptron.train()
    return jsonify(perceptron.evaluate())

# ------------------------------
# Endpoint: /datasets
# - Returns a list of available datasets in JSON format
# ------------------------------
@app.route('/datasets', methods=['GET'])
def datasets():
    return jsonify(list_dataset)

# ------------------------------
# Endpoint: /functions
# - Returns a list of available activation functions and training configurations
# ------------------------------
@app.route('/functions', methods=['GET'])
def functions():
    return jsonify(list_functions_options)

# ------------------------------
# Endpoint: /getImages
# - Returns URLs of uploaded test images, sorted numerically
# ------------------------------
@app.route('/getImages', methods=['GET'])
def getImages():
    image_files = [
        f for f in os.listdir(UPLOAD_FOLDER)
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, f)) and f.lower().endswith('.png')
    ]
    image_files = sorted(image_files, key=numerical_sort)
    image_urls = [BASE_URL + f for f in image_files if f]
    return jsonify(image_urls)

# ------------------------------
# Endpoint: Serve individual images
# - Used by frontend to display images
# ------------------------------
@app.route('/server/test_images/<path:filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ------------------------------
# Endpoint: /upload
# - Accepts multiple files from form-data
# - Saves them to the test_images folder with sequential filenames
# ------------------------------
@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist("files")
    saved_files = []
    numberTestImages = countImages(test_images_path)  # Current number of images

    for i, file in enumerate(files, start=numberTestImages):
        filename = f"img-{i}.png"  # Sequential filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        saved_files.append(filename)

    return jsonify({"message": "Files saved with success!", "files": saved_files})

# ------------------------------
# Endpoint: /deleteImage/<filename>
# - Deletes a specific image by filename
# - Renames remaining images to maintain sequential order
# ------------------------------
@app.route('/deleteImage/<filename>', methods=['DELETE'])
def deleteImage(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        rename_images(UPLOAD_FOLDER)  # Re-sequence image filenames
        return jsonify({"message": f"{filename} deleted successfully!"})
    else:
        return jsonify({"error": "File not found"}), 404

# ------------------------------
# Run the Flask app on localhost:5000
# ------------------------------
if __name__ == '__main__':
    app.run(port=5000, debug=True)
