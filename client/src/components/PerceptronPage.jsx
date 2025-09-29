import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import Select from "react-select";
import Dropzone from "react-dropzone";
import {
  fetchDatasets,
  fetchFunctions,
  fetchUpload,
  fecthPredict,
  fetchImages,
} from "../services/apiServices";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import SimpleImageSlider from "react-simple-image-slider";
import "./perceptron.css";

const PerceptronPage = () => {
  const navigate = useNavigate();
  const [selectedDatasetOption, setSelectedDatasetOption] = useState();
  const [selectedFunctionOption, setSelectedFunctionOption] = useState();
  const [datasetsOptions, setDatasetOptions] = useState([]);
  const [functionsOptions, setFunctionOptions] = useState([]);
  const [predictResult, setPredictResult] = useState(
    "Your Data is being processed, it will take time depending on learning rate and the number of epochs!"
  );

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

  const handleExecute = async () => {
    if (!selectedDatasetOption || !selectedFunctionOption) {
      toast.error("Select a dataset or function before starting!", {
        position: "top-right",
        autoClose: 4000,
        hideProgressBar: true,
        theme: "colored",
      });
      return;
    }
    try {
      toast.success("Execution started!", {
        position: "top-right",
        autoClose: 4000,
        hideProgressBar: true,
        theme: "colored",
      });
      const response = await fecthPredict(
        selectedDatasetOption.value.id,
        selectedFunctionOption.value.id
      );
      const predictionText = response.map((p) => p.prediction).join("\n");
      setPredictResult(predictionText);
    } catch (err) {
      toast.error("Error while trying to predict!", {
        position: "top-right",
        autoClose: 4000,
        hideProgressBar: true,
        theme: "colored",
      });
      console.error(err);
    }
  };

  return (
    <>
      <div className="container">
        <div className="button-div-perceptron">
          <button onClick={() => navigate("/about")}>About</button>
          <button id="quitButton">Quit</button>
          <button onClick={handleExecute} id="executerButton">
            Execute
          </button>
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
        <Dropzone
          onDrop={(acceptedFiles) => {
            if (acceptedFiles.length > 0) {
              toast.success(
                `${acceptedFiles.length} file(s) added successfully!`,
                {
                  position: "top-right",
                  autoClose: 3000,
                  hideProgressBar: true,
                  theme: "colored",
                }
              );

              console.log("Files received:", acceptedFiles);
              fetchUpload(acceptedFiles);
            }
          }}
          onDropRejected={(fileRejections) => {
            fileRejections.forEach((file) => {
              toast.error(
                `File "${file.file.name}" rejected. Only PNG images are allowed.`,
                {
                  position: "top-right",
                  autoClose: 4000,
                  hideProgressBar: true,
                  theme: "colored",
                }
              );
            });
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
        <div className="div-middle">
          <div className="div-results">
            <label>Results</label>
            <textarea
              name="postContent"
              value={predictResult}
              onChange={(e) => setPredictResult(e.target.value)}
              readOnly
              rows={15}
              cols={35}
            />
          </div>
          {/* <SimpleImageSlider
            width={896}
            height={504}
            images={images}
            showBullets={true}
            showNavs={true}
          /> */}
        </div>
        <ToastContainer />
      </div>
    </>
  );
};
export default PerceptronPage;
