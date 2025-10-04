# Scientific Initiation Project - Perceptron Projec

Perceptron Project (Electron + React + Flask + Python)

## Authors

- Filipe Miguel Amaro Passarinho - <filipeamaropassarinho@gmail.com>
- Fábio Ferrentini Sampaio, Ph.D. - <fabio.sampaio@estsetubal.ips.pt>

## Overview

This project demonstrates a **simple perceptron neural network for letter recognition**. It has a Python backend to perform calculations and a React frontend running inside Electron for a desktop application experience
The perceptron is a **fundamental neural network model that can solve linear classification problems**. Training data is stored in .npz files for compact and efficient handling. You can experiment with pre-loaded datasets or upload your own images.

## Features

- Train and test a simple perceptron with uploaded or pre-loaded images.
- Choose activation function, learning rate, and number of epochs.
- View results and uploaded images in a simple slider.
- Delete images if needed.

## Project Structure

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

## Backend

Developed in Python with Flask and Flask-CORS to handle API requests.
Provides endpoints for:

- /datasets - fetch available datasets
- /functions - fetch available activation functions
- /predict - run perceptron predictions
- /upload - upload images
- /getImages - list images
- /deleteImage/`<filename>` - delete an image

## Backend Requirements

- Python >= 3.10
- Flask
- Flask-CORS
- Numpy
- Pillow (for image processing)

## Install backend dependencies with

- cd server
- python -m venv venv - to create virtual enviroment
- venv\Scripts\activate
- pip install flask flask-cors numpy pillow opencv-python

## Frontend

- Built with React, Vite, and Electron Forge.
- Uses React plugin for Vite and Bootstrap icons.

## Install Frontend dependencies with

- cd client
- npm install

## Running the application

In one terminal run:

- cd server
- venv/Scripts/Activate
- python server.py

In other terminal run:

- cd client
- npm run start # Start development mode
- npm run make # Build the Electron app (Optional)

## How to Use

- Start the backend server first (python perceptron.py).
- Start the frontend (npm run start) or run the Electron app (npm run make then open the executable).
- Draw or delete your test images.
- Select a dataset, a function (activation), and run the perceptron.
- Observe results in the “Results” section.

## How the Perceptron Works

### 1. Preprocessing

- Images are converted to grayscale and normalized (values between 0 and 1).
- Each image is resized to 120x90 pixels (total 10800 pixels).
- A centering algorithm ensures the letter is aligned in the center of the vector.

### 2. Dataset Labeling

- For training, half the images are positive (containing the target letter) and the other half negative.
- This labeling guides the perceptron during learning.

### 3. Initialization

- Weights are randomly initialized and bias is set.
- Learning parameters include learning rate, number of epochs, and activation function.

### 4. Training

- For each epoch, the perceptron predicts the output for every training image.
- Error is calculated (error = label - prediction) and weights and bias are updated:
- w = w + \text{learning_rate} \times \text{error} \times x b = b + \text{learning_rate} \times \text{error}

- Available activation functions:
  - Step Function: output is 0 or 1
  - Sigmoid: output between 0 and 1, useful for confidence estimation

### 5. Evaluation

- The perceptron predicts whether each test image contains the target letter.
- For sigmoid, confidence is shown as a percentage.
- Results are returned in JSON for the React interface to display.

### 6. Data Storage

- Training and testing: images converted to 1D arrays and saved in .npz files for optimized reading.
- Resizing: ensures speed without losing letter shape.
- Centering: avoids letter displacement, improving accuracy.

### Additional Notes

- Learning Rate: controls the step size for weight adjustments.
  - Small: slow but stable training
  - Large: fast training, but may not converge
- Epochs: number of full passes through the dataset. Larger datasets require more epochs.
- Sigmoid vs Step: Sigmoid gives a confidence score, Step gives binary output.

## Challenge

- Try extending the code to a multilayer perceptron. Observe how additional layers and connections affect learning, prediction accuracy, and processing complexity.
