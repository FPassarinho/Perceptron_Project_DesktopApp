import os
import sys
import json
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from perceptron import Perceptron
from conversion_functions import *

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller exe"""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller temporary folder
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Paths das pastas / arquivos
datasets_path = resource_path("datasets")
test_images_path = resource_path("test_images")
data_file_path = resource_path("data_file")  # folder

# Flask app
app = Flask(__name__)
CORS(app)

# Load configs
with open("datasets.json", "r") as f:
    list_dataset = json.load(f)

with open("functions_options.json") as f:
    list_functions_options = json.load(f)

# Paths
base_path = os.path.dirname(os.path.abspath(__file__))
test_images_path = os.path.join(base_path, "test_images")
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "test_images")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

BASE_URL = "http://127.0.0.1:5000/server/test_images/"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    numberDataset = data["dataset_id"]
    numberFunction = data["function_id"]

    # Dataset & word
    for option in list_dataset:
        if option["id"] == numberDataset:
            dataset = option["dataset"]
            word = option["word"]
            dataset_path = os.path.join(base_path, "datasets", dataset)

    # Function config
    for option in list_functions_options:
        if option["id"] == numberFunction:
            num_epochs = option["num_epochs"]
            learning_rate = option["learning_rate"]
            function = option["function"]

    # Train and evaluate
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


@app.route('/datasets', methods=['GET'])
def datasets():
    return jsonify(list_dataset)


@app.route('/functions', methods=['GET'])
def functions():
    return jsonify(list_functions_options)


@app.route('/getImages', methods=['GET'])
def getImages():
    image_files = [
        f for f in os.listdir(UPLOAD_FOLDER)
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, f)) and f.lower().endswith('.png')
    ]
    image_files = sorted(image_files, key=numerical_sort)
    image_urls = [BASE_URL + f for f in image_files]
    return jsonify(image_urls)


@app.route('/server/test_images/<path:filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist("files")
    saved_files = []
    numberTestImages = countImages(test_images_path)

    for i, file in enumerate(files, start=numberTestImages):
        filename = f"img-{i}.png"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        saved_files.append(filename)

    return jsonify({"message": "Files saved with success!", "files": saved_files})


@app.route('/deleteImage/<filename>', methods=['DELETE'])
def deleteImage(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"{filename} deleted successfully!"})
    else:
        return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
