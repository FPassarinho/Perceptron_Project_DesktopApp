# Scientific Initiation Project - Perceptron Project

[![License](https://img.shields.io/badge/License-BSD--2--Clause-blue.svg)](LICENSE)

## Authors

- Filipe Miguel Amaro Passarinho - <filipeamaropassarinho@gmail.com>
- Fábio Ferrentini Sampaio, Ph.D. - <fabio.sampaio@estsetubal.ips.pt>

## Overview

This project demonstrates a **simple perceptron neural network for letter recognition**. It has a Python backend to perform calculations and a React frontend running inside Electron for a desktop application experience
The perceptron is a **fundamental neural network model that can solve linear classification problems**. Training data is stored in .npz files for compact and efficient handling. You can experiment with pre-loaded datasets.

## Features

- Train and test a simple perceptron with drawn or preloaded images.
- Choose activation function, learning rate, and number of epochs.
- View results and uploaded images in a simple slider.
- Delete images if needed.

## Project Structure

Perceptron_Project_DesktopApp

- server/ Python backend (Flask)
- client/ React + Electron frontend

## Requirements

To run this project you must have installed:

- **Python >= 3.10**
- **Node.js (>= 18.x)**
- **Visual Studio Build Tools** (required for some npm packages)
- **pip** (comes with Python)

## Backend Requirements

- Python >= 3.10
- Flask
- Flask-CORS
- Numpy
- Pillow (for image processing)

## Install backend dependencies

- cd server
- python -m venv venv
- venv\Scripts\activate
- pip install flask flask-cors numpy pillow waitress

## Frontend

- Built with React, Vite, and Electron Forge.
- Uses React plugin for Vite and Bootstrap icons.

## Install Frontend dependencies

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

## Creating the .exe for production

**_NOTE:_** Before building the production application, if you have made any changes to the datasets, it is mandatory to generate the corresponding .npz files. Otherwise, the production build will only include the .npz files that already exist.

There is a helper function in `server/conversion_functions.py` called `generate_all_npz_local()` that will automatically create .npz files for all datasets. This function is intended for local development only and should be run before building the executable if you have added or modified datasets.

In one terminal:

- cd server
- venv/Scripts/activate
- pip install pyinstaller
- pyinstaller --onefile --noconsole --clean --collect-all flask --optimize=2 --add-data "datasets;datasets" --add-data "data_file;data_file" --add-data "test_images;test_images" --add-data "datasets.json;." --add-data "functions_options.json;." --name server server.py

In another terminal:

- cd client
- npm run make

## What is a perceptron?

The Perceptron is one of the earliest computational models designed to imitate, in a very simplified way, how a biological neuron works. In a brain, neurons receive signals from other neurons and decide whether to activate based on those inputs. Similarly, a perceptron receives several input signals (for example, characteristics of an image or data about a situation), processes them, and produces an output — usually a decision such as “yes” or “no.” In this sense, a perceptron can be thought of as a simple decision-making unit capable of learning from examples (Russell & Norvig, 2021).

## A Brief Historical Background

The concept of the perceptron was introduced in 1958 by Frank Rosenblatt, a researcher at Cornell University (Rosenblatt, 1958). His objective was to create a machine capable of recognizing patterns and adapting its responses based on experience, rather than being explicitly programmed for each specific task. Rosenblatt even built a physical version of the perceptron using electronic circuits, demonstrating that the model could learn simple visual patterns.

In the following decade, however, enthusiasm about perceptrons diminished. In 1969, Marvin Minsky and Seymour Papert published a book titled Perceptrons, in which they demonstrated that the model could not solve certain types of problems, especially those that were not linearly separable (Minsky & Papert, 1969). This criticism temporarily halted research in neural networks. Yet, in the 1980s, new ideas about using multiple layers of perceptrons — known as multilayer networks — revived the field and laid the groundwork for modern artificial intelligence (Goodfellow, Bengio & Courville, 2016; Mitchel, 2019)

## The Importance of the Perceptron in Artificial Intelligence

Although the perceptron by itself can only handle simple learning tasks, its conceptual importance is immense. It introduced the revolutionary idea that **machines could learn from data** rather than being limited to instructions written by programmers. The perceptron inspired the development of modern artificial neural networks, which consist of many layers of interconnected “neurons.” These networks are the foundation of current artificial intelligence systems that recognize speech, identify faces in photos, translate languages, and even drive autonomous vehicles (Russell & Norvig, 2021). In summary, the perceptron represents the **first step in the history of machine learning.** It transformed the way scientists thought about computation and learning, showing that computers could adapt and improve through experience — a principle that remains at the heart of artificial intelligence today.

## References (related to the content above)

- Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
- Minsky, M., & Papert, S. (1969). Perceptrons: An Introduction to Computational Geometry. MIT Press.
- Mitchell, Melanie. (2019). Artificial Intelligence: A Guide for Thinking Humans. Farrar, Straus and Giroux.
- Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. Psychological Review, 65(6), 386–408.
- Russell, S., & Norvig, P. (2021). Artificial Intelligence: A Modern Approach (4th ed.). Pearson.

## How to use this program

This program allows you to interactively experiment with a perceptron model. It comes with a set of **preloaded test images** that you can use right away, or you can **draw your own test samples** directly within the interface. Both the preloaded and the drawn images can be easily deleted or replaced at any time.

**Note:** All input images are interpreted as **uppercase machine-style letters.** Lowercase or handwritten letters may produce unexpected results.

Next, select the **dataset** corresponding to the letter you want to detect — for example, choosing **Dataset A** to test whether your test images represent the letter “A” or not. You can then customize the perceptron’s configuration by selecting the **activation function** Step or Sigmoid, the **learning rate**, and the **number of training epochs.**

Each parameter combination has been **pre-optimized by the development team** to achieve a balance between accuracy and computation time. Even with the most demanding configuration (Sigmoid with maximum epochs and learning rate), training completes in about one minute, producing results that are both efficient and insightful.

Once training is complete, the perceptron evaluates all test images — both preloaded and drawn — and displays predictions in the **Results** section.

## How the Project Works internally

Under the hood, this application combines Python (Flask) on the backend with a JavaScript/React frontend running inside an Electron environment. This setup allows the entire system to function as a standalone desktop application while still leveraging web technologies for interactivity and visualization. The backend is responsible for image preprocessing, perceptron training, and prediction, while the Electron-based frontend provides an intuitive interface that communicates directly with the API.

The process can be divided into three key stages

**1. Image Preprocessing:** Each image either preloaded or drawn by the user is resized to120x90 pixels (10,800 values) and converted to grayscale. A custom centering algorithm ensures that the letter remains in the middle of the image, which prevents misalignment from confusing the perceptron. The pixel values are then normalized between 0 and 1 and flattened into a 1D array, since the perceptron operates on vector inputs rather than on 2D matrices as images are.

**2. Dataset Preparation and Labeling:** The program generates training data from the selected dataset. Half of the samples are labeled as positive (the target letter) and the other half as negative (non-target). Images are stored in compressed .npz format for efficient loading. When the perceptron is initialized, these vectors are loaded directly into memory.

**3. Perceptron Initialization:** Each image pixel is an input to the perceptron, and each input has a corresponding weight, initially randomized between -0.05 and 0.05. The bias starts at 0 and acts as an adjustable offset, shifting the activation threshold so the perceptron can make better decisions even when input values are near zero. The user-selected learning rate controls how aggressively the weights are updated during training, while the number of epochs defines how many times the model will iterate over the full dataset

**4. Training Phase:** During training, the perceptron calculates the weighted sum of inputs `(w * x + bias)`, applies the chosen activation function, and compares the prediction to the expected label. The error (expected - predicted) is then used to adjust both the weights and the bias according to the perceptron learning rule:

- `w_new = w_old + learning_rate * error * input`
- `bias_new = bias_old + learning_rate * error`

This iterative correction continues for the defined number of epochs, gradually minimizing the loss and improving classification accuracy.

**Note:** Training time depends on several factors: the number of pixels (image resolution), the size of the dataset, the learning rate, and the number of epochs. More pixels, a larger dataset, higher learning rates, or more epochs will all increase computation time.

**5. Activation Functions:** This perceptron supports two activation modes:

- Step Function — a binary decision: outputs 1 if the weighted sum ≥ 0, else 0.
- Sigmoid Function — outputs a smooth probability between 0 and 1, allowing confidence estimation. Slower but more expressive.

**6. Evaluation:** After training, the perceptron evaluates all test images. With the step function, predictions are binary (is or isn’t the target letter). With the sigmoid, the model outputs a confidence percentage, e.g. “I am 92% sure this image is an A.” The results are then returned as JSON to the frontend.

The backend is powered by Flask, which exposes multiple API endpoints:

- `/predict` — trains and evaluates the perceptron.
- `/datasets` — returns available datasets.
- `/functions` — returns activation and training configurations.
- `/getImages` — provides URLs of current test images.
- `/deleteImage` — removes selected test images and reorders filenames

The **Electron-based React frontend** communicates with these endpoints using `fetch()` requests. When the user selects a dataset, activation function, and parameters, the frontend sends this configuration to the `/predict` API. The backend then runs the full training process and returns structured prediction results that are displayed dynamically in the desktop interface.
This architecture cleanly separates concerns: the Flask backend performs all computational logic and data management, while the Electron/React frontend handles interactivity and visualization. Together, they demonstrate how even a single-neuron perceptron can form the foundation of more complex neural networks and machine learning applications.

**Challenge:** Try extending this perceptron into a multilayer perceptron (MLP). Observe how additional layers and activation functions allow it to learn more abstract features and improve classification performance.

Key concepts recap:

- **Weights:** control how much each pixel influences the decision.
- **Bias:** shifts the decision boundary to improve flexibility.
- **Learning rate:** defines how strongly weights change per iteration.
- **Epochs:** number of complete passes through the training dataset.
- **Activation function:** determines how the perceptron maps inputs to outputs.
