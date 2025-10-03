import "./canvasPage.css";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";
import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchUpload } from "../services/apiServices";

const CanvasPage = () => {
  const navigate = useNavigate();
  const canvasRef = useRef(null);
  const [drawing, setDrawing] = useState(false);
  const [initialized, setInitialized] = useState(false);

  // Inicializa o canvas com fundo branco
  const initCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas || initialized) return;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    setInitialized(true);
  };

  const startDrawing = (e) => {
    initCanvas(); // garante que fundo branco exista antes de desenhar
    setDrawing(true);
    draw(e);
  };

  const endDrawing = () => {
    setDrawing(false);
    const ctx = canvasRef.current.getContext("2d");
    ctx.beginPath();
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "white"; // fundo branco ao limpar
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
  };

  const saveCanvas = async () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    // já tem fundo branco, então só precisa salvar
    canvas.toBlob(async (blob) => {
      if (!blob) return;

      const file = new File([blob], "canvas.png", { type: "image/png" });
      try {
        const result = await fetchUpload([file]);
        console.log("Uploaded:", result);
        toast.success("Image uploaded successfully!", {
          position: "top-right",
          autoClose: 4000,
          hideProgressBar: true,
          theme: "colored",
        });
        clearCanvas();
      } catch (err) {
        console.error("Upload failed", err);
        toast.error("Upload failed!", {
          position: "top-right",
          autoClose: 4000,
          hideProgressBar: true,
          theme: "colored",
        });
      }
    }, "image/png");
  };

  const draw = (e) => {
    if (!drawing) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    const rect = canvas.getBoundingClientRect();

    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineWidth = 22;
    ctx.lineCap = "round";
    ctx.strokeStyle = "black";

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  return (
    <>
      <div className="container">
        <div className="main-card">
          <div className="button-div-canvas">
            <button
              className="button-wrapper-canvas"
              onClick={() => navigate("/perceptron")}
            >
              <i className="bi bi-arrow-left"></i>
            </button>
          </div>
          <h2>Draw the letter that you want to test</h2>
          <canvas
            className="canvas"
            width={500}
            height={375}
            ref={canvasRef}
            onMouseDown={startDrawing}
            onMouseUp={endDrawing}
            onMouseMove={draw}
            onMouseLeave={endDrawing}
          />
          <div className="canvas-buttons">
            <button onClick={clearCanvas}>Clear</button>
            <button onClick={saveCanvas}>Save</button>
          </div>
        </div>
      </div>
      <ToastContainer />
    </>
  );
};

export default CanvasPage;
