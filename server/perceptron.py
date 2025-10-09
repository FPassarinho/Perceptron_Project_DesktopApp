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
from conversion_functions import *  # Utilities for image processing (load, resize, center, etc.)

# Base path for storing/loading processed data
base_path = os.path.dirname(os.path.abspath(__file__))
data_file_dir = os.path.join(base_path, "data_file")


class Perceptron:
    """
    Simple Perceptron Neural Network for binary classification of images (letters).
    """

    def __init__(self, learning_rate, num_epochs, dir_path_train, dir_path_test, function, word):
        # ------------------------------
        # Hyperparameters and Config
        # ------------------------------
        self.learning_rate = learning_rate    # Step size for weight updates
        self.num_epochs = num_epochs          # Number of full passes over the training data
        self.dir_path_train = dir_path_train  # Path to training images
        self.dir_path_test = dir_path_test    # Path to testing images
        self.function = function              # Activation function: 'STEP_FUNCTION' or 'SIGMOID'
        self.word = word                      # Target letter for classification

        # Each image is resized to 120x90 pixels = 10800 features
        self.num_pixels = 120 * 90

        # Initialize weights randomly in small range [-0.05, 0.05] and bias = 0
        self.weights = np.random.uniform(-0.05, 0.05, self.num_pixels)
        self.bias = 0

        # Placeholders for training and test data
        self.train_data = None
        self.train_labels = None
        self.test_data = None

        # Count number of training and testing samples
        self.num_train_samples = countImages(dir_path=dir_path_train)
        self.num_test_samples = countImages(dir_path=dir_path_test)

    # ------------------------------
    # Activation Function
    # ------------------------------
    def activation_function(self, x):
        """
        Apply the selected activation function.
        STEP_FUNCTION: outputs 0 or 1
        SIGMOID: outputs value in [0,1] as probability
        """
        if self.function == 'STEP_FUNCTION':
            return np.where(x >= 0, 1, 0)
        elif self.function == 'SIGMOID':
            return 1 / (1 + np.exp(-x))

    # ------------------------------
    # Prediction
    # ------------------------------
    def predict(self, input):
        """
        Compute weighted sum + bias and pass through activation function.
        input: 1D numpy array of image pixel values (flattened)
        """
        return self.activation_function(np.dot(self.weights, input) + self.bias)

    # ------------------------------
    # Training
    # ------------------------------
    def train(self):
        """
        Train the perceptron using the provided training dataset.
        Steps:
        1. Load or create training data as 1D arrays (.npz file)
        2. Initialize labels (1 for positive samples, 0 for negative)
        3. Loop over epochs and update weights and bias using perceptron learning rule
        """
        # Initialize training labels (first half = positive, second half = negative)
        self.train_labels = np.zeros(self.num_train_samples, dtype=int)
        n = int(self.num_train_samples / 2)
        self.train_labels[:n] = 1

        # Load preprocessed image data from .npz file or create it if missing
        npz_path = os.path.join(data_file_dir, f"image_data{self.word}.npz")
        if not os.path.exists(npz_path):
            loadStoreImagesFileNpz(self.num_train_samples, dir_path=self.dir_path_train, word=self.word)

        # Load training data into memory
        with np.load(npz_path) as data:
            self.train_data = np.array([data[key] for key in data.files])

        # ------------------------------
        # Training loop over epochs
        # ------------------------------
        for epoch in range(self.num_epochs):
            epoch_loss = 0  # Sum of squared errors for this epoch

            # Loop over each training sample
            for i in range(self.num_train_samples):
                prediction = self.predict(self.train_data[i])        # Predicted output
                error = self.train_labels[i] - prediction            # Difference from true label
                epoch_loss += error ** 2                              # Accumulate squared error

                # Update weights and bias (perceptron learning rule)
                self.weights += self.learning_rate * error * self.train_data[i]
                self.bias += self.learning_rate * error

            # Print loss every 10 epochs
            if epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {epoch_loss:.4f}")

    # ------------------------------
    # Evaluation
    # ------------------------------
    def evaluate(self):
        """
        Evaluate the perceptron on test images.
        Returns a list of dictionaries with predictions and confidence.
        """
        # Load test images as 1D arrays
        self.test_data = loadStoreImages(self.num_test_samples, dir_path=self.dir_path_test)
        results = []

        # Loop over each test image
        for i in range(self.num_test_samples):
            prediction = self.predict(self.test_data[i])

            if self.function == "SIGMOID":
                # Convert sigmoid output to percentage confidence
                prediction_percentage = float(prediction * 100)
                if prediction_percentage >= 80:
                    # Confident prediction that image is the target letter
                    results.append({
                        "image": i + 1,
                        "prediction": f"• I am certain that image {i + 1} is an {self.word} with {prediction_percentage:.2f}% confidence!\n"
                    })
                else:
                    # Confident prediction that image is NOT the target letter
                    results.append({
                        "image": i + 1,
                        "prediction": f"• I am certain that image {i + 1} is not an {self.word} with {100 - prediction_percentage:.2f}% confidence!\n",
                    })
            else:
                # Step function: simple 0 or 1 output
                if prediction == 1:
                    results.append({"prediction": f"• I think that image {i + 1} is an {self.word}!\n"})
                else:
                    results.append({"prediction": f"• I think that image {i + 1} is not an {self.word}!\n"})

        return results
