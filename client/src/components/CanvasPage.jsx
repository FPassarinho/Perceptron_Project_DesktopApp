import "./canvasPage.css";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

const CanvasPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <div className="container">
        <div className="main-card">
          <div className="button-div-about">
            <button
              className="button-wrapper-about"
              onClick={() => navigate("/perceptron")}
            >
              <i className="bi bi-arrow-left"></i>
            </button>
          </div>
          <h2>Draw the letter that you want to test</h2>
          <canvas className="canvas" />
          <div className="canvas-buttons">
            <button>Clear</button>
            <button>Pencil</button>
            <button>Rubber</button>
            <button>Save</button>
          </div>
        </div>
      </div>
    </>
  );
};

export default CanvasPage;
