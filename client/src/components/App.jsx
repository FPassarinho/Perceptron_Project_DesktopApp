import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import IndexPage from './IndexPage';
import AboutPage from './AboutPage';
import PerceptronPage from './PerceptronPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<IndexPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/perceptron" element={<PerceptronPage />} />
      </Routes>
    </Router>
  );
}

export default App;
