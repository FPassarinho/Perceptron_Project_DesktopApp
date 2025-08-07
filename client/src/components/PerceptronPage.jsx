import Header from "./Header";
import { useNavigate } from "react-router-dom";

const PerceptronPage = () => {
  const navigate = useNavigate();

  return (
    <div>
      <Header />
      <div>
        <button onClick={() => navigate("/about")}>About</button>
      </div>
      <div className="toolbar">
        <button id="penButton">Pen</button>
        <button id="rubberButton">Rubber</button>
        <button id="clearButton">Clear</button>
        <button id="submitButton">Submit</button>
      </div>
      <canvas id="drawBoard"></canvas>
    </div>
  );
};
export default PerceptronPage;
