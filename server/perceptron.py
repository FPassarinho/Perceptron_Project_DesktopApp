# The code is prepared to read one-dimensional matrices,
# so data cannot be stored in two-dimensional format.
# If it is stored in 2D (which is the case), a conversion to 1D is required.

# The number of training epochs indicates how many times the model will pass through the entire training dataset.
# (10–50) for small datasets, 50–200 for medium datasets, 100–500+ for large datasets.
# The learning rate determines how big or small the adjustment of the model’s weights will be at each training iteration.
# If the learning rate is too high, the model might not converge or jump to a suboptimal solution.
# If it's too low, training may be too slow or get stuck in a local minimum.
# Small values: (0.00001 to 0.001)
# Medium values: (0.001 to 0.01)
# High values: (0.1 to 1.0)
# The more images there are, the more epochs are needed to iterate through them.
### SIGMOID FUNCTION - conversion of fyles included in time /130 images
###  EPOCHS - 550 / LEARNING RATE - 0.01 //// TIME - 11,46 /// Battery - 33.44 seconds
### EPOCHS - 1050 / LEARNING RATE - 0.005 //// TIME - 17,39  /// Battery - 54.12 seconds
### EPOCHS - 5100 / LEARNING RATE - 0.001 //// TIME - 70.27 /// Battery - 220 seconds
#### STEP-FUNCTION
### EPOCHS - 40 / LEARNING RATE - 0.01 //// TIME - 4,01 seconds /// Battery - 17.36 seconds
### EPOCHS - 400 / LEARNING RATE - 0.00001 //// TIME - 8.30 seconds /// Battery - 34.41 seconds

import os
import numpy as np
import json
from conversion_functions import *
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# Flask app setup
app = Flask(__name__)
CORS(app)

# Load datasets and functions configuration
with open("datasets.json", "r") as f:
    list_dataset = json.load(f)

with open("functions_options.json") as f:
    list_functions_options = json.load(f)

# Define paths
base_path = os.path.dirname(os.path.abspath(__file__))
data_file_dir = os.path.join(base_path, "data_file")
test_images_path = os.path.join(base_path, "test_images")

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "test_images")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Base URL for serving uploaded/test images
BASE_URL = "http://127.0.0.1:5000/server/test_images/"

############################################
# ------------ PERCEPTRON CLASS ------------
############################################
class Perceptron:
    def __init__(self, learning_rate, num_epochs, dir_path_train, dir_path_test, function, word):
        # Hyperparameters
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.dir_path_train = dir_path_train
        self.dir_path_test = dir_path_test
        self.function = function
        self.word = word

        # Each image is resized to 120x90 = 10800 pixels
        self.num_pixels = 10800  

        # Initialize weights and bias
        self.weights = np.random.uniform(-0.05, 0.05, self.num_pixels)
        self.bias = 0

        # Placeholders for training/testing data
        self.train_data = None
        self.train_labels = None
        self.test_data = None

        # Count training and testing samples
        self.num_train_samples = countImages(dir_path=dir_path_train)
        self.num_test_samples = countImages(dir_path=dir_path_test)

    ########################################
    # Neuron activation function
    ########################################
    def activation_function(self, x):
        if self.function == 'STEP_FUNCTION':
            return np.where(x >= 0, 1, 0)
        elif self.function == 'SIGMOID':
            return 1 / (1 + np.exp(-x))

    ########################################
    # Prediction (forward pass)
    ########################################
    def predict(self, input):
        return self.activation_function(np.dot(self.weights, input) + self.bias)

    ########################################
    # Training (adjust weights & bias)
    ########################################
    def train(self):
        # All training images belong to 'word' (example: 'A')
        self.train_labels = np.zeros(self.num_train_samples, dtype=int)
        n = int(self.num_train_samples / 2)  
        self.train_labels[:n] = 1  # First half marked as positive class

        # Load or create training dataset in .npz format
        npz_path = os.path.join(data_file_dir, f"image_data{self.word}.npz")
        if not os.path.exists(npz_path):
            loadStoreImagesFileNpz(self.num_train_samples, dir_path=self.dir_path_train, word=self.word)

        with np.load(npz_path) as data:
            self.train_data = np.array([data[key] for key in data.files])

        # Training loop
        for epoch in range(self.num_epochs):
            epoch_loss = 0
            for i in range(self.num_train_samples):
                prediction = self.predict(self.train_data[i])
                error = self.train_labels[i] - prediction

                # Mean squared error accumulation
                epoch_loss += error ** 2

                # Update weights and bias (gradient descent)
                self.weights += self.learning_rate * error * self.train_data[i]
                self.bias += self.learning_rate * error

            # Print debug info every 10 epochs
            if epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {epoch_loss:.4f}")

    ########################################
    # Evaluate model with test dataset
    ########################################
    def evaluate(self):
        self.test_data = loadStoreImages(self.num_test_samples, dir_path=self.dir_path_test)
        results = []

        for i in range(self.num_test_samples):
            prediction = self.predict(self.test_data[i])

            # Handle sigmoid separately (percentage confidence)
            if self.function == "SIGMOID":
                prediction_percentage = float(prediction * 100)
                if prediction_percentage >= 80:
                    results.append({
                        "image": i + 1,
                        "prediction": f"I think that image {i + 1} is an {self.word} with {prediction_percentage:.2f}",
                    })
                else:
                    results.append({
                        "image": i + 1,
                        "prediction": f"I think that image {i + 1} is not an {self.word} with {100 - prediction_percentage:.2f}",
                    })
            else:  # Step function (binary output)
                if prediction == 1:
                    results.append({"prediction": f"I Think that image {i + 1} is an {self.word}"})
                else:
                    results.append({"prediction": f"I Think that image {i + 1} is not an {self.word}"})

        return jsonify(results)

############################################
# ------------ FLASK ROUTES ---------------
############################################

@app.route('/predict', methods=['POST'])
def predict():
    # Get request params
    data = request.get_json()
    numberDataset = data["dataset_id"]
    numberFunction = data["function_id"]

    # Select dataset & word
    for option in list_dataset:
        if option["id"] == numberDataset:
            dataset = option["dataset"]
            word = option["word"]
            dataset_path = os.path.join(base_path, "datasets", dataset)

    # Select function config
    for option in list_functions_options:
        if option["id"] == numberFunction:
            num_epochs = option["num_epochs"]
            learning_rate = option["learning_rate"]
            function = option["function"]

    # Initialize and run perceptron
    perceptron = Perceptron(
        learning_rate=learning_rate,
        num_epochs=num_epochs,
        dir_path_train=dataset_path,
        dir_path_test=test_images_path,
        function=function,
        word=word
    )
    perceptron.train()
    return perceptron.evaluate()

# Get list of datasets
@app.route('/datasets', methods=['GET'])
def datasets():
    return jsonify(list_dataset)

# Get list of function configs
@app.route('/functions', methods=['GET'])
def functions():
    return jsonify(list_functions_options)

# Get uploaded test images (as URLs)
@app.route('/getImages', methods=['GET'])
def getImages():
    image_files = [
        f for f in os.listdir(UPLOAD_FOLDER)
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, f)) and f.lower().endswith('.png')
    ]
    image_files = sorted(image_files, key=numerical_sort)
    image_urls = [BASE_URL + f for f in image_files]
    return jsonify(image_urls)

# Serve image by filename
@app.route('/server/test_images/<path:filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Upload new images
@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist("files")
    saved_files = []

    # Ensure unique filenames
    numberTestImages = countImages(test_images_path)
    for i, file in enumerate(files, start=numberTestImages):
        filename = f"img-{i}.png"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        saved_files.append(filename)

    return jsonify({"message": "Files saved with success!", "files": saved_files})

# Delete specific image
@app.route('/deleteImage/<filename>', methods=['DELETE'])
def deleteImage(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)  # <--- missing before!
        return jsonify({"message": f"{filename} deleted successfully!"})
    else:
        return jsonify({"error": "File not found"}), 404

############################################
# ------------ APP ENTRYPOINT -------------
############################################
if __name__ == '__main__':
    app.run(port=5000, debug=True)
