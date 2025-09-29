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
              You’ll be able to test it with pre-loaded images or upload your
              own. You can also tweak the activation function, learning rate,
              and number of training epochs to observe how the perceptron
              responds. The training data is stored in <code>.npz</code> files
              for compact and efficient handling.
            </p>
            <p>
              If you want to dive deeper, you can inspect the code or try a
              Python-only version that runs in the terminal. Before using these
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
                <li>
                  <a
                    href="https://github.com/FPassarinho/Perceptron_Project_DesktopTerminal.git"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Perceptron Project Desktop Terminal
                  </a>
                </li>
              </ul>
            </p>
          </div>

          {/* What is a perceptron */}
          <div>
            <h3>What is a perceptron?</h3>
            <p>
              The perceptron is the first artificial neural network
              architecture, developed by Frank Rosenblatt in 1958. It works like
              a single neuron in the brain: it receives multiple inputs and
              produces a single output. Mathematically, it sums the inputs
              weighted by certain values, adds a bias, and applies an activation
              function to determine the output (0 or 1).
            </p>
            <p>Key parameters include:</p>
            <ul>
              <li>
                <strong>Weights:</strong> how much each input counts
              </li>
              <li>
                <strong>Bias:</strong> a correction factor
              </li>
              <li>
                <strong>Activation function:</strong> determines how the output
                is decided
              </li>
              <li>
                <strong>Learning rate & epochs:</strong> control how the
                perceptron learns during training
              </li>
            </ul>
          </div>

          {/* How the program works */}
          <div>
            <h3>How this program works</h3>
            <p>
              To use the program, you first choose the dataset of test images or
              upload your own. Then select the letter you want to detect, the
              activation function, and the preset learning rate and number of
              epochs.
            </p>
            <p>
              Depending on the chosen function, processing time varies: SIGMOID
              is slower than STEP. Larger learning rates or more epochs also
              increase computation time. In extreme cases, a SIGMOID with
              maximum settings can take up to one minute.
            </p>
            <p>
              Once you run it, predictions appear in the “Results” section. You
              can remove individual images if needed. The program is designed so
              the perceptron reaches a very low epoch loss, producing reliable
              predictions.
            </p>
          </div>

          {/* Internal workings */}
          <div>
            <h3>How it works internally</h3>
            <p>
              Behind the scenes, the perceptron follows a simple but effective
              process:
            </p>
            <ol>
              <li>
                <strong>Pre-processing:</strong> Images are centered using a
                custom algorithm. This ensures the letter is in the middle,
                because even slight shifts could confuse the perceptron.
              </li>
              <li>
                <strong>Resizing:</strong> Images are resized to 120x90 pixels.
                This keeps processing fast while maintaining enough detail.
              </li>
              <li>
                <strong>Initialization:</strong> The perceptron class sets up
                weights, bias, the selected activation function, learning rate,
                and number of epochs.
              </li>
              <li>
                <strong>Training:</strong> The perceptron repeatedly predicts
                outputs for each image and adjusts weights using the error. This
                repeats for the number of epochs.
              </li>
              <li>
                <strong>Evaluation:</strong> Finally, the perceptron predicts
                whether each test image contains the target letter or not.
              </li>
            </ol>
            <p>
              Keep in mind that this is a simple neuron. Extremely large
              datasets, very high learning rates, or excessive epochs may slow
              down training or produce inaccurate results. The preset values
              were chosen through experimentation to provide reliable outcomes
              efficiently.
            </p>
            <p>
              This simple perceptron demonstrates a fundamental principle of
              artificial intelligence: learning through trial and error,
              adjusting parameters iteratively, and making decisions based on
              patterns of zeros and ones.
            </p>
            <p>
              <strong>Challenge:</strong> Try extending the code to a multilayer
              perceptron. Observe how adding layers and connections affects
              learning, prediction accuracy, and processing complexity.
            </p>
          </div>

          {/* Conclusion */}
          <div>
            <h3>Summary</h3>
            <p>
              In this section, you’ve learned how the perceptron works in theory
              and in practice. You can experiment with different parameters,
              upload your own images, and even extend the code for more complex
              neural networks. Don’t forget: training data is stored in{" "}
              <code>.npz</code> format, and the README files of the provided
              repositories contain important instructions for correct usage.
            </p>
          </div>
        </div>
      </div>
    </>
  );
};
export default AboutPage;
