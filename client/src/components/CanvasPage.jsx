import "./canvasPage.css";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";
import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchUpload } from "../services/apiServices";

const CanvasPage = () => {
  const navigate = useNavigate();
  const canvasRef = useRef(null); // reference to the canvas element
  const [drawing, setDrawing] = useState(false); // track if user is drawing
  const [initialized, setInitialized] = useState(false); // ensure canvas is initialized once

  // Initialize the canvas with a white background
  const initCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas || initialized) return;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "white"; // fill white background
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath(); // start a new drawing path
    setInitialized(true);
  };

  // Start drawing when mouse is pressed
  const startDrawing = (e) => {
    initCanvas(); // ensure canvas has white background
    setDrawing(true);
    draw(e); // start drawing immediately
  };

  // Stop drawing when mouse is released
  const endDrawing = () => {
    setDrawing(false);
    const ctx = canvasRef.current.getContext("2d");
    ctx.beginPath(); // reset path to avoid connecting lines
  };

  // Clear canvas and reset background
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
  };

  // Save canvas as PNG and upload to backend
  const saveCanvas = async () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

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
        clearCanvas(); // clear after upload
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

  // Draw on canvas
  const draw = (e) => {
    if (!drawing) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    const rect = canvas.getBoundingClientRect();

    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineWidth = 22; // brush thickness
    ctx.lineCap = "round"; // smooth edges
    ctx.strokeStyle = "black";

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  return (
    <>
      <div className="container">
        <div className="main-card-canvas">
          <div className="button-div-canvas">
            {/* Navigate back to perceptron page */}
            <button
              className="button-wrapper-canvas"
              onClick={() => navigate("/perceptron")}
            >
              <i className="bi bi-arrow-left"></i>
            </button>
          </div>
          <h3>Draw the letter that you want to test</h3>
          {/* Canvas element */}
          <canvas
            className="canvas"
            width={500}
            height={375}
            ref={canvasRef}
            onMouseDown={startDrawing}
            onMouseUp={endDrawing}
            onMouseMove={draw}
            onMouseLeave={endDrawing} // stop drawing if cursor leaves canvas
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
