import { useNavigate } from "react-router-dom";
import functionOptions from "../data/functionOptions.json";
import "./perceptron.css";

const PerceptronPage = () => {
  const navigate = useNavigate();
  // const [selected, setSelected] = useState("");

  // const values = Object.values(functionOptions);

  return (
    <>
      <div className="button-div-perceptron">
        <button onClick={() => navigate("/about")}>About</button>
        <button id="rubberButton">Quit</button>
        <button id="clearButton">Execute</button>
      </div>
      <div className="options-select">
        {/* <select value={selected} onChange={(e) => setSelected(e.target.value)}>
          <option value="">-- Selecione --</option>
          {values.map((value, index) => (
            <option key={index} value={value}>
              {value}
            </option>
          ))}
        </select> */}
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
