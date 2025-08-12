import Header from "./Header";
import { useNavigate } from "react-router-dom";
import "./aboutPage.css";

const AboutPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <Header />
      <div className="main-div-about">
        <div className="button-div-about">
          <button
            className="button-wrapper-about"
            onClick={() => navigate("/perceptron")}
          >
            <i class="bi bi-arrow-left"></i>
          </button>
        </div>
        <div className="text-div-about">
          <h3>What is this section?</h3>
          <p>
            In this section of the application, you’ll learn the basics of the
            perceptron and how it works in theory. After that, you’ll explore
            how to use this application to see what a perceptron is capable of
            and how even small changes can significantly affect its decisions.
            To dive deeper, you can visit this link ###link### to inspect and
            download all the code and try to understand as much as you can. Feel
            free to change anything you want and experiment with different
            variations. Also, if you want a cleaner and simpler way to test, you
            can check the version of this program that just uses Python and runs
            on the terminal.
          </p>
          <div>
            <h3>What is a perceptron and how it works?</h3>
            <p>
              O perceptron foi a primeira arquitetura de rede neuronais
              artificiais desenvolvida pelo cientista Frank Rosenblatt,em 1958.
              O perceptron pode ser pensado como um neurónio do nosso cérebro,
              que funciona de uma simples maneira utilizando só células de input
              que terminam numa única célula de output. De uma maneira mais
              científica isto quer dizer que o Perceptron é um modelo matemático
              que recebe diversas entradas e produz um único resultado, sendo
              ela ou 0 ou 1. - falar de ephocs, learning rate, pesos, epoch
              loss.
            </p>
          </div>
          <div>
            <h3>How the program works?</h3>
            <p>
              Após perceberem como funciona teóricamente o perceptron, agora é
              altura de perceberem como funciona este simples programa. O
              primeiro passo é decidirem se querem experimentar as imagens de
              teste que são fornecidas ou se pretendem utilizar uma imagem feita
              por vocês. Após essa escolha têm só de decidir que letra querem
              verificar se é ou não. Não se esqueçam que como é um simples
              perceptron, o programa vai só dizer se é a letra que vocês
              escolheram ou não. Após isso e como já aprenderam anteriormente,
              só têm de escolher a função que pretendem e o learning rate e o
              número de epochs que querem. O programa não permite que vocês
              escolham os valores que pretendem, mas permitem que escolham de
              entre um conjunto de valores pré-selecionados que faz com que o
              epoch loss seja perto de 0.000 que é o pretendido. --- (Acabar
              explica como é o funcionamento de todo o perceptron)
            </p>
          </div>
        </div>
      </div>
    </>
  );
};
export default AboutPage;
