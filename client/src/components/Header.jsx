import logo from "../assets/logo.png";
import polytechnic_setubal_logo from "../assets/polytechnic_setubal_logo.png";
import { Link } from "react-router-dom";
import "./header.css";

const Header = () => {
  return (
    <div>
      <header>
        <div className="header">
          <Link to="/">
            <img className="logo" src={logo} alt="Porject Logo" />
          </Link>
          <div className="top_text">
            <h1>MIND OF A PERCEPTRON</h1>
          </div>
          <a href="https://ips.pt/">
            <img
              className="logo_polytechnic"
              src={polytechnic_setubal_logo}
              alt="Polytechnic Setúbal Logo"
            />
          </a>
        </div>
      </header>
    </div>
  );
};

export default Header;
