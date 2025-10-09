import { useNavigate } from "react-router-dom";
import "./aboutPage.css";

const AboutPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <div className="main-div-about">
        <div className="button-div-about">
          <button
            className="button-wrapper-about"
            onClick={() => navigate("/perceptron")}
          >
            <i className="bi bi-arrow-left"></i>
          </button>
        </div>

        <div className="text-div-about">
          {/* Introduction */}
          <div>
            <h3>What is this section?</h3>
            <p>
              Welcome! In this section, you’ll explore the basics of the
              perceptron and see how it works in practice. The perceptron is a
              simple type of neural network, but even small changes in its setup
              can produce interesting results.
            </p>
            <p>
              You’ll be able to test it with pre-loaded images or draw your own.
              You can also tweak the activation function, learning rate, and
              number of training epochs to observe how the perceptron responds.
            </p>
            <p>
              If you want to dive deeper, you can inspect the code by downloading the files that are in github. Before using these
              projects, it is highly recommended to read their README files for
              setup instructions and additional details.
              <ul>
                <li>
                  <a
                    href="https://github.com/FPassarinho/Perceptron_Project_DesktopApp.git"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Perceptron Project Desktop App
                  </a>
                </li>
              </ul>
            </p>
          </div>

          {/* What is a perceptron */}
          <div>
            <h3>What is a perceptron?</h3>
            <p>
              The Perceptron is one of the earliest computational models
              designed to imitate, in a very simplified way, how a biological
              neuron works. In a brain, neurons receive signals from other
              neurons and decide whether to activate based on those inputs.
              Similarly, a perceptron receives several input signals (for
              example, characteristics of an image or data about a situation),
              processes them, and produces an output — usually a decision such
              as “yes” or “no.” In this sense, a perceptron can be thought of as
              a simple decision-making unit capable of learning from examples
              (Russell & Norvig, 2021).
            </p>
          </div>

          {/* A Brief Historical background */}
          <div>
            <h3>A Brief Historical Background</h3>
            <p>
              The concept of the perceptron was introduced in 1958 by{" "}
              <strong>Frank Rosenblatt</strong>, a researcher at Cornell
              University (Rosenblatt, 1958). His objective was to create a
              machine capable of recognizing patterns and adapting its responses
              based on experience, rather than being explicitly programmed for
              each specific task. Rosenblatt even built a physical version of
              the perceptron using electronic circuits, demonstrating that the
              model could learn simple visual patterns.
            </p>
            <p>
              In the following decade, however, enthusiasm about perceptrons
              diminished. In 1969, <strong>Marvin Minsky</strong> and
              <strong> Seymour Papert</strong> published a book titled
              Perceptrons, in which they demonstrated that the model could not
              solve certain types of problems, especially those that were not
              linearly separable (Minsky & Papert, 1969). This criticism
              temporarily halted research in neural networks. Yet, in the 1980s,
              new ideas about using multiple layers of perceptrons — known as
              multilayer networks — revived the field and laid the groundwork
              for modern artificial intelligence (Goodfellow, Bengio &
              Courville, 2016; Mitchel, 2019).
            </p>
          </div>

          {/* The Importance of the Perceptron in Artificial Intelligence */}
          <div>
            <h3>The Importance of the Perceptron in Artificial Intelligence</h3>
            <p>
              Although the perceptron by itself can only handle simple learning
              tasks, its conceptual importance is immense. It introduced the
              revolutionary idea that
              <strong> machines could learn from data</strong> rather than being
              limited to instructions written by programmers. The perceptron
              inspired the development of modern artificial neural networks,
              which consist of many layers of interconnected “neurons.” These
              networks are the foundation of current artificial intelligence
              systems that recognize speech, identify faces in photos, translate
              languages, and even drive autonomous vehicles (Russell & Norvig,
              2021). In summary, the perceptron represents the{" "}
              <strong>first step in the history of machine learning.</strong> It
              transformed the way scientists thought about computation and
              learning, showing that computers could adapt and improve through
              experience — a principle that remains at the heart of artificial
              intelligence today.
            </p>
          </div>

          {/* References */}
          <div>
            <h3>References (related to the content above)</h3>
            <ul>
              <li>
                Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep
                Learning. MIT Press.
              </li>
              <li>
                Minsky, M., & Papert, S. (1969). Perceptrons: An Introduction to
                Computational Geometry. MIT Press.
              </li>
              <li>
                Mitchell, Melanie. (2019). Artificial Intelligence: A Guide for
                Thinking Humans. Farrar, Straus and Giroux.
              </li>
              <li>
                Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for
                Information Storage and Organization in the Brain. Psychological
                Review, 65(6), 386–408.
              </li>
              <li>
                Russell, S., & Norvig, P. (2021). Artificial Intelligence: A
                Modern Approach (4th ed.). Pearson.
              </li>
            </ul>
          </div>

          {/* Some educational and online resources */}
          <div>
            <h3>Some Educational and Online Resources</h3>

            <h4>Deep Learning 101: Lesson 7: Perceptron (Medium Post)</h4>
            <p>
              This article offers a clear, step-by-step exploration of the
              perceptron algorithm and its implementation in deep learning.
              <a
                href="https://muneebsa.medium.com/deep-learning-101-lesson-7-perceptron-f6a698d81be8"
                target="_blank"
                rel="noopener noreferrer"
              >
                Read here
              </a>
            </p>
            <br />

            <h4>Teachable Machine (Google Experiments)</h4>
            <p>
              An interactive web tool that allows students to train a simple
              perceptron-like model in the browser using images or sounds.{" "}
              <a
                href="https://teachablemachine.withgoogle.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Try it here
              </a>
            </p>
            <br />

            <h4>
              YouTube: “The Perceptron — Deep Learning Demystified” (IBM
              Technology, 2020)
            </h4>
            <p>
              A short and engaging video that visually explains how a perceptron
              works.{" "}
              <a
                href="https://www.youtube.com/watch?v=kft1AJ9WVDk"
                target="_blank"
                rel="noopener noreferrer"
              >
                Watch here
              </a>
            </p>
          </div>

          {/* How the program works */}
          <div>
            <h3>How to use this program</h3>
            <p>
              This program allows you to interactively experiment with a
              perceptron model. It comes with a set of{" "}
              <strong>preloaded test images</strong> that you can use right
              away, or you can <strong>draw your own test samples</strong>{" "}
              directly within the interface. Both the preloaded and the drawn
              images can be easily deleted or replaced at any time.
            </p>
            <p>
              <strong>Note:</strong> All input images are interpreted as{" "}
              <strong>uppercase machine-style letters</strong>. Lowercase or
              handwritten letters may produce unexpected results.
            </p>
            <p>
              Next, select the <strong>dataset</strong> corresponding to the
              letter you want to detect — for example, choosing{" "}
              <strong>Dataset A</strong> to test whether your test images
              represent the letter “A” or not. You can then customize the
              perceptron’s configuration by selecting the{" "}
              <strong>activation function</strong> (<em>Step</em> or{" "}
              <em>Sigmoid</em>), the <strong>learning rate</strong>, and the{" "}
              <strong>number of training epochs</strong>.
            </p>
            <p>
              Each parameter combination has been{" "}
              <strong>pre-optimized by the development team</strong>
              to achieve a balance between accuracy and computation time. Even
              with the most demanding configuration (Sigmoid with maximum epochs
              and learning rate), training completes in about one minute,
              producing results that are both efficient and insightful.
            </p>
            <p>
              Once training is complete, the perceptron evaluates all test
              images — both preloaded and drawn — and displays predictions in
              the <strong>Results</strong> section.
            </p>
          </div>

          {/* Internal workings */}
          <div>
            <h3>How it works internally</h3>
            <p>
              Under the hood, this application combines{" "}
              <strong>Python (Flask)</strong> on the backend with a{" "}
              <strong>JavaScript/React</strong> frontend running inside an{" "}
              <strong>Electron</strong> environment. This setup allows the
              entire system to function as a standalone desktop application
              while still leveraging web technologies for interactivity and
              visualization. The backend is responsible for image preprocessing,
              perceptron training, and prediction, while the Electron-based
              frontend provides an intuitive interface that communicates
              directly with the API.
            </p>

            <p>The process can be divided into three key stages:</p>

            <ol>
              <li>
                <strong>Image Preprocessing: </strong>
                Each image either preloaded or drawn by the user is resized to
                <code>120x90</code> pixels (10,800 values) and converted to
                grayscale. A custom centering algorithm ensures that the letter
                remains in the middle of the image, which prevents misalignment
                from confusing the perceptron. The pixel values are then
                normalized between 0 and 1 and flattened into a{" "}
                <strong>1D array</strong>, since the perceptron operates on
                vector inputs rather than on 2D matrices as images are.
              </li>

              <li>
                <strong>Dataset Preparation and Labeling: </strong>
                The program generates training data from the selected dataset.
                Half of the samples are labeled as <strong>
                  positive
                </strong>{" "}
                (the target letter) and the other half as{" "}
                <strong>negative</strong> (non-target). Images are stored in
                compressed <code>.npz</code> format for efficient loading. When
                the perceptron is initialized, these vectors are loaded directly
                into memory.
              </li>

              <li>
                <strong>Perceptron Initialization: </strong>
                Each image pixel is an input to the perceptron, and each input
                has a corresponding weight, initially randomized between -0.05
                and 0.05. The bias starts at 0 and acts as an adjustable offset,
                shifting the activation threshold so the perceptron can make
                better decisions even when input values are near zero. The
                user-selected learning rate controls how aggressively the
                weights are updated during training, while the number of epochs
                defines how many times the model will iterate over the full
                dataset.
              </li>

              <li>
                <strong>Training Phase: </strong>
                During training, the perceptron calculates the weighted sum of
                inputs (<code>w * x + bias</code>), applies the chosen
                activation function, and compares the prediction to the expected
                label. The error (<code>expected - predicted</code>) is then
                used to adjust both the weights and the bias according to the
                perceptron learning rule:
                <pre>w_new = w_old + learning_rate * error * input</pre>
                <pre>bias_new = bias_old + learning_rate * error</pre>
                This iterative correction continues for the defined number of
                epochs, gradually minimizing the loss and improving
                classification accuracy.
                <p>
                  <strong>Note: </strong>
                  Training time depends on several factors: the number of pixels
                  (image resolution), the size of the dataset, the learning
                  rate, and the number of epochs. More pixels, a larger dataset,
                  higher learning rates, or more epochs will all increase
                  computation time.
                </p>
              </li>

              <li>
                <strong>Activation Functions: </strong>
                This perceptron supports two activation modes:
                <ul>
                  <li>
                    <em>Step Function</em> — a binary decision: outputs 1 if the
                    weighted sum ≥ 0, else 0.
                  </li>
                  <li>
                    <em>Sigmoid Function</em> — outputs a smooth probability
                    between 0 and 1, allowing confidence estimation. Slower but
                    more expressive.
                  </li>
                </ul>
              </li>

              <li>
                <strong>Evaluation: </strong>
                After training, the perceptron evaluates all test images. With
                the step function, predictions are binary (is or isn’t the
                target letter). With the sigmoid, the model outputs a confidence
                percentage, e.g. “I am 92% sure this image is an A.” The results
                are then returned as JSON to the frontend.
              </li>
            </ol>

            <p>
              The backend is powered by <strong>Flask</strong>, which exposes
              multiple API endpoints:
            </p>
            <ul>
              <li>
                <code>/predict</code> — trains and evaluates the perceptron.
              </li>
              <li>
                <code>/datasets</code> — returns available datasets.
              </li>
              <li>
                <code>/functions</code> — returns activation and training
                configurations.
              </li>
              <li>
                <code>/getImages</code> — provides URLs of current test images.
              </li>
              <li>
                <code>/deleteImage</code> — removes selected test images and
                reorders filenames.
              </li>
            </ul>

            <p>
              The <strong>Electron-based React frontend</strong> communicates
              with these endpoints using <code>fetch()</code> requests. When the
              user selects a dataset, activation function, and parameters, the
              frontend sends this configuration to the <code>/predict</code>{" "}
              API. The backend then runs the full training process and returns
              structured prediction results that are displayed dynamically in
              the desktop interface.
            </p>

            <p>
              This architecture cleanly separates concerns: the Flask backend
              performs all computational logic and data management, while the
              Electron/React frontend handles interactivity and visualization.
              Together, they demonstrate how even a single-neuron perceptron can
              form the foundation of more complex neural networks and machine
              learning applications.
            </p>

            <p>
              <strong>Challenge: </strong>
              Try extending this perceptron into a{" "}
              <em>multilayer perceptron (MLP)</em>. Observe how additional
              layers and activation functions allow it to learn more abstract
              features and improve classification performance.
            </p>

            <p>Key concepts recap:</p>
            <ul>
              <li>
                <strong>Weights:</strong> control how much each pixel influences
                the decision.
              </li>
              <li>
                <strong>Bias:</strong> shifts the decision boundary to improve
                flexibility.
              </li>
              <li>
                <strong>Learning rate:</strong> defines how strongly weights
                change per iteration.
              </li>
              <li>
                <strong>Epochs:</strong> number of complete passes through the
                training dataset.
              </li>
              <li>
                <strong>Activation function:</strong> determines how the
                perceptron maps inputs to outputs.
              </li>
            </ul>
          </div>
          {/* Written By */}
          <div>
            <p>
              <em>
                Written By Sampaio & Passarinho with ChatGPT collaboration.
              </em>
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default AboutPage;
