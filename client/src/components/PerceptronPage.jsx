import Header from "./Header";
import { useNavigate } from "react-router-dom";
import "./perceptron.css";

const PerceptronPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <Header />
      <div>
        <button onClick={() => navigate("/about")}>About</button>
        <button id="rubberButton">Quit</button>
        <button id="clearButton">Execute</button>
      </div>
      {/* <div className="toolbar">
        <button id="penButton">Pen</button>
        <button id="rubberButton">Rubber</button>
        <button id="clearButton">Clear</button>
        <button id="submitButton">Submit</button>
      </div>
      <canvas id="drawBoard"></canvas> */}
    </>
  );
};
export default PerceptronPage;
