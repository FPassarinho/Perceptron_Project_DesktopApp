import "./canvasPage.css";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";
import React, { useRef, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const CanvasPage = () => {
  const navigate = useNavigate();
  const canvasRef = useRef(null);
  const [drawing, setDrawing] = useState(false);

  const startDrawing = (e) => {
    setDrawing(true);
    draw(e);
  };

  const endDrawing = () => {
    setDrawing(false);
    const ctx = canvasRef.current.getContext("2d");
    ctx.beginPath();
  };

  const draw = (e) => {
    if (!drawing) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    const rect = canvas.getBoudingClientRect();

    const x = e.clientx - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineWidth = 8;
    ctx.lineCap = "round";
    ctx.strokeStyle = "balck";

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

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
          <canvas
            className="canvas"
            ref={canvasRef}
            onMouseDown={startDrawing}
            onMouseUp={endDrawing}
            onMouseMove={draw}
            onMouseLeave={endDrawing}
          />
          <div className="canvas-buttons">
            <button>Clear</button>
            <button>Save</button>
          </div>
        </div>
      </div>
    </>
  );
};

export default CanvasPage;
