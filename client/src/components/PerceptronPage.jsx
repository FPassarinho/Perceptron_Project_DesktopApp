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
  deleteImage,
} from "../services/apiServices";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import SimpleImageSlider from "react-simple-image-slider";
import "./perceptron.css";

const PerceptronPage = () => {
  const navigate = useNavigate();

  // State for dropdown selections
  const [selectedDatasetOption, setSelectedDatasetOption] = useState();
  const [selectedFunctionOption, setSelectedFunctionOption] = useState();

  // State for dropdown options
  const [datasetsOptions, setDatasetOptions] = useState([]);
  const [functionsOptions, setFunctionOptions] = useState([]);

  // State for prediction results and images
  const [predictResult, setPredictResult] = useState(
    "Your Data is being processed, it will take time depending on learning rate and the number of epochs!"
  );
  const [images, setImages] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  // Loading state for predictions
  const [loading, setLoading] = useState(false);

  // Fetch datasets and functions on mount
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

  // Fetch images on mount
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

  // Execute perceptron prediction
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

      // Call backend for prediction
      const response = await fecthPredict(
        selectedDatasetOption.value.id,
        selectedFunctionOption.value.id
      );

      // Concatenate predictions into text
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

  // Delete currently selected image
  const handleDeleteImage = async () => {
    if (images.length === 0) return;

    const url = images[currentIndex];
    const filename = url.split("/").pop();

    try {
      const response = await deleteImage(filename);
      toast.success(response.message, {
        position: "top-right",
        autoClose: 4000,
        hideProgressBar: true,
        theme: "colored",
      });

      // Update local state after deletion
      const updatedImages = images.filter((img, idx) => idx !== currentIndex);
      setImages(updatedImages);
      setCurrentIndex((prev) =>
        prev >= updatedImages.length ? updatedImages.length - 1 : prev
      );
    } catch (err) {
      toast.error("Failed to delete image", {
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
        <div className="main-card">
          {/* Top buttons and dropdowns */}
          <div className="button-div-perceptron">
            <button onClick={() => navigate("/about")}>About</button>
            {images.length > 0 ? (
              <>
                <button onClick={handleExecute} id="executerButton">
                  Execute
                </button>
                <button
                  className="delete-image-button"
                  onClick={handleDeleteImage}
                >
                  Delete Image
                </button>
              </>
            ) : (
              <p
                className="button-paragraph"
                style={{ color: "gray", fontStyle: "italic" }}
              >
                Upload images to enable execution.
              </p>
            )}
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

          {/* Drag & drop for image upload */}
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

                  // Refresh image list
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
              // Show error for rejected files
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
                    Drag 'n' drop some files here, or click to select files.
                    When dropped the files will be added automatically
                  </p>
                </div>
              </section>
            )}
          </Dropzone>

          {/* Results and images section */}
          <div className="div-middle">
            {/* Results textarea */}
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

            {/* Image slider */}
            <div className="slider-container-wrapper">
              <label>Images</label>
              <div className="slider-container">
                {images.length > 0 ? (
                  <>
                    <SimpleImageSlider
                      width={400}
                      height={300}
                      images={images.map((img) => ({ url: img }))}
                      showNavs={true}
                      onStartSlide={(idx) => setCurrentIndex(idx - 1)}
                    />
                    <div className="inline-slider">
                      {currentIndex + 1} / {images.length}
                    </div>
                  </>
                ) : (
                  <div className="no-images-placeholder">No images yet</div>
                )}
              </div>
            </div>
          </div>
          <ToastContainer />
        </div>
      </div>
    </>
  );
};

export default PerceptronPage;
