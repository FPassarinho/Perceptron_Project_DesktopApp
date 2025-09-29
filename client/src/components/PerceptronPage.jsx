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
  const [images, setImages] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(false);

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

  useEffect(() => {
    const getImages = async () => {
      try {
        const dataImages = await fetchImages();
        setImages(dataImages);
      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };
    getImages();
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
    setLoading(true);
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
    } finally {
      setLoading(false);
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
          onDrop={async (acceptedFiles) => {
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

              try {
                await fetchUpload(acceptedFiles);

                const dataImages = await fetchImages();
                setImages(dataImages);

                toast.success("Image list updated!", {
                  position: "top-right",
                  autoClose: 2000,
                  hideProgressBar: true,
                  theme: "colored",
                });
              } catch (error) {
                console.error("Error uploading or refreshing images:", error);
                toast.error("Failed to upload or refresh images!", {
                  position: "top-right",
                  autoClose: 4000,
                  hideProgressBar: true,
                  theme: "colored",
                });
              }
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
            <div className="textarea-wrapper">
              {loading && (
                <div className="loading-dots-textarea">
                  <span>.</span>
                  <span>.</span>
                  <span>.</span>
                </div>
              )}
              <textarea
                name="postContent"
                value={loading ? "" : predictResult}
                onChange={(e) => setPredictResult(e.target.value)}
                readOnly
              />
            </div>
          </div>
          <div className="slider-container-wrapper">
            <label>Images</label>
            <div className="slider-container">
              {images.length > 0 && (
                <SimpleImageSlider
                  width={400}
                  height={300}
                  images={images.map((img) => ({ url: img }))}
                  showNavs={true}
                  onStartSlide={(idx) => setCurrentIndex(idx - 1)}
                />
              )}
              {images.length > 0 && (
                <>
                  <div className="inline-slider">
                    {currentIndex + 1} / {images.length}
                  </div>
                  {/* <button
                    className="delete-image-button"
                    onClick={handleDeleteCurrentImage}
                  >
                    Delete Image
                  </button> */}
                </>
              )}
            </div>
          </div>
        </div>
        <ToastContainer />
      </div>
    </>
  );
};
export default PerceptronPage;
