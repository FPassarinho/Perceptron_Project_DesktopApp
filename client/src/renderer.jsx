import { createRoot } from "react-dom/client";
import App from "./components/App";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./index.css";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
