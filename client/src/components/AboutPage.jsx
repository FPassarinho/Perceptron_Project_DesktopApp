import Header from "./Header";
import { useNavigate } from "react-router-dom";

const AboutPage = () => {
  const navigate = useNavigate();

  return (
    <div>
      <Header />
      <div className="main-div-about">
        <div className="button-div-about">
          <button
            className="button-wrapper-about"
            onClick={() => navigate("/perceptron")}
          >
            <i class="bi bi-arrow-left"></i>
          </button>
        </div>
        <div className="text-div-about">
          <h2>What is this section?</h2>
          <p>
            In this section of the application, you’ll learn the basics of the
            perceptron and how it works in theory. After that, you’ll explore
            how to use this application to see what a perceptron is capable of
            and how even small changes can significantly affect its decisions.
            To dive deeper, you can visit this link ###link### to inspect and
            download all the code and try to understand as much as you can. Feel
            free to change anything you want and experiment with different
            variations.
          </p>
          <div>
            <h3>What is a perceptron and how it works?</h3>
            <p></p>
          </div>
          <div>
            <h3>How the program works?</h3>
          </div>
        </div>
      </div>
    </div>
  );
};
export default AboutPage;
