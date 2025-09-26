import { useNavigate } from "react-router-dom";
import functionOptions from "../data/functionOptions.json";
import "./perceptron.css";

function predict(id1, id2) {
  fetch("http://127.0.0.1:5000", {
    method: "POST", 
    headers: {
      "Content-Type": "application/json", 
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok " + response.statusText);
      }
      return response.json(); 
    })
    .then((result) => {
      console.log("Server response:", result); a
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
const PerceptronPage = () => {
  const navigate = useNavigate();

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
