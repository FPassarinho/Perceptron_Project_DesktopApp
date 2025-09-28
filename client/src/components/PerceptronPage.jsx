import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import Select from "react-select";
import Dropzone from "react-dropzone";
import {
  fetchDatasets,
  fetchFunctions,
  fetchUpload,
  fecthPredict,
} from "../services/apiServices";
import SimpleImageSlider from "react-simple-image-slider";
import "./perceptron.css";

const PerceptronPage = () => {
  const navigate = useNavigate();
  const [selectedDatasetOption, setSelectedDatasetOption] = useState();
  const [selectedFunctionOption, setSelectedFunctionOption] = useState();
  const [datasetsOptions, setDatasetOptions] = useState([]);
  const [functionsOptions, setFunctionOptions] = useState([]);
  const formData = new FormData();

  useEffect(() => {
    const getOptions = async () => {
      try {
        const dataDataset = await fetchDatasets();
        const options1 = dataDataset.map((d) => ({
          value: d,
          label: d.text,
        }));
        setDatasetOptions(options1);

        const dataFunctions = await fetchFunctions();
        const options2 = dataFunctions.map((f) => ({
          value: f,
          label: f.text,
        }));
        setFunctionOptions(options2);
      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };
    getOptions();
  }, []);

  return (
    <>
      <div className="button-div-perceptron">
        <button onClick={() => navigate("/about")}>About</button>
        <button id="rubberButton">Quit</button>
        <button id="clearButton">Execute</button>
        <Select
          className="my-select"
          options={datasetsOptions}
          value={selectedDatasetOption}
          onChange={setSelectedDatasetOption}
          placeholder="Select a dataset..."
        />
        <Select
          className="my-select"
          options={functionsOptions}
          value={selectedFunctionOption}
          onChange={setSelectedFunctionOption}
          placeholder="Select a function..."
        />
      </div>
      {/* <SimpleImageSlider
        width={896}
        height={504}
        images={images}
        showBullets={true}
        showNavs={true}
      /> */}
      <Dropzone
        onDrop={(acceptedFiles) => {
          console.log("Arquivos recebidos:", acceptedFiles);
          fetchUpload(acceptedFiles);
        }}
        accept={{ "image/png": [".png"] }}
      >
        {({ getRootProps, getInputProps }) => (
          <section>
            <div {...getRootProps()} className="dropzone">
              <input {...getInputProps()} />
              <p>
                Drag 'n' drop some files here, or click to select files. When
                dropped the files will be added automatically
              </p>
            </div>
          </section>
        )}
      </Dropzone>
      <textarea
        name="postContent"
        defaultValue="Your Data is being processed, it will take time, depending on learning rate and the number of epochs!"
        rows={4}
        cols={40}
      />
    </>
  );
};
export default PerceptronPage;
