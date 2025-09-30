# Perceptron_Project

# Scientific Initiation Project!

Perceptron Project (Electron + React + Flask + Python)

## Overview:

This project demonstrates a simple perceptron neural network for letter recognition. It has a Python backend to perform calculations and a React frontend running inside Electron for a desktop application experience
The perceptron is a fundamental neural network model that can solve linear classification problems. Training data is stored in .npz files for compact and efficient handling. You can experiment with pre-loaded datasets or upload your own images.

## Features:

- Train and test a simple perceptron with uploaded or pre-loaded images.
- Choose activation function, learning rate, and number of epochs.
- View results and uploaded images in a simple slider.
- Delete images if needed.

## Project Structure:

Perceptron_Project_DesktopApp
│
├── server/ # Python backend (Flask)
└── client/ # React + Electron frontend

## Requirements

To run this project you must have installed:

- **Python >= 3.10**
- **Node.js (>= 18.x)**
- **Visual Studio Build Tools** (required for some npm packages)
- **pip** (comes with Python)

## Backend:

Developed in Python with Flask and Flask-CORS to handle API requests.
Provides endpoints for:

- /datasets - fetch available datasets
- /functions - fetch available activation functions
- /predict - run perceptron predictions
- /upload - upload images
- /getImages - list images
- /deleteImage/<filename> - delete an image

## Backend Requirements:

- Python >= 3.10
- Flask
- Flask-CORS
- Numpy
- Pillow (for image processing)

## Install backend dependencies with:

- cd server
- pip install flask flask-cors numpy pillow

## Frontend:

- Built with React, Vite, and Electron Forge.
- Uses React plugin for Vite and Bootstrap icons.

## Install Frontend dependencies with:

- cd client
- npm install

## Run the application:

In one terminal run:

- cd server
- python perceptron.py

In other terminal run:

- cd client
- npm run start # Start development mode
- npm run make # Build the Electron app (Optional)

## How to Use:

- Start the backend server first (python perceptron.py).
- Start the frontend (npm run start) or run the Electron app (npm run make then open the executable).
- Upload images or use pre-loaded datasets.
- Select a dataset, a function (activation), and run the perceptron.
- Observe results in the “Results” section.
- Remove individual images if needed.

## How the Perceptron Works:

- Pre-processing: Images are centered using a custom algorithm to ensure correct input alignment.
- Resizing: Images are resized to 120x90 pixels to optimize processing speed while maintaining enough detail.
- Dataset Labeling: For training, an array is
  created to indicate the labels: half of the images are
  considered positive (the target letter) and the other half
  negative (not the target letter). This guides the perceptron
  during learning.
- Initialization: The perceptron sets up weights, bias, learning rate, epochs, and selected activation function.
- Training: Repeated predictions with weight and bias adjustments over the specified number of epochs.
- Evaluation: The perceptron outputs whether each image contains the target letter.

More details about how the programs work can be found inside the program in the about tab.

## Challenge:

- Try extending the code to a multilayer perceptron. Observe how additional layers and connections affect learning, prediction accuracy, and processing complexity.
