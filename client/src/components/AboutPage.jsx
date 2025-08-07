import Header from "./Header";
import { useNavigate } from "react-router-dom";

const AboutPage = () => {
  const navigate = useNavigate();

  return (
    <div>
      <Header />
      <div>
        <button
          className="button-wrapper"
          onClick={() => navigate("/perceptron")}
        >
          Go back to perceptron
        </button>
      </div>
    </div>
  );
};
export default AboutPage;
