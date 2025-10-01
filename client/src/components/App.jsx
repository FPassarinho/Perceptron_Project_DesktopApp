import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IndexPage from "./IndexPage";
import AboutPage from "./AboutPage";
import PerceptronPage from "./PerceptronPage";
import CanvasPage from "./CanvasPage";
import Header from "./Header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<IndexPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/perceptron" element={<PerceptronPage />} />
        <Route path="/canvas" element={<CanvasPage />} />s
      </Routes>
    </Router>
  );
}

export default App;
