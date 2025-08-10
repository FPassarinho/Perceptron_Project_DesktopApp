import Header from "./Header";
import rosenblatt from "../assets/perceptron/rosenblatt.png";
import { useNavigate } from "react-router-dom";

const IndexPage = () => {
  const navigate = useNavigate();

  return (
    <div>
      <Header />
      <div className="middle">
        <div className="text-content">
          <p>
            The perceptron was created in 1958 by Frank Rosenblatt and is a
            mathematical model inspired by biological neurons. It was the first
            supervised learning algorithm for neural networks and is capable of
            solving linear classification problems.
          </p>
        </div>
        <img
          className="rosenblatt_image"
          src={rosenblatt}
          alt="Frank Rosenblatt Image with Perceptron"
        />
      </div>
      <footer>
        <div className="item">
          <div>
            <h3>Authors:</h3>
            <p>
              Filipe Miguel Amaro Passarinho, Bachelor in Informatics Engineer
              Student - <u>filipeamaropassarinho@gmail.com</u>
            </p>
            <p>
              Fábio Ferrentini Sampaio, Ph.D. -
              <u>fabio.sampaio@estsetubal.ips.pt</u>
            </p>
          </div>
          <div className="polytechnic">
            <p>Polytechnic Institute of Setúbal</p>
          </div>
        </div>
        <div className="button-div-index">
          <button
            className="button-wrapper-index"
            onClick={() => navigate("/perceptron")}
          >
            <i className="bi bi-box-arrow-in-right"></i>
          </button>
        </div>
      </footer>
    </div>
  );
};
export default IndexPage;
