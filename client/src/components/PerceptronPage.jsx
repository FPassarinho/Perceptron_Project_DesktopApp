import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import Select from "react-select";
import {
  fetchDatasets,
  fetchFunctions,
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

  // Dropdown states
  const [selectedDatasetOption, setSelectedDatasetOption] = useState();
  const [selectedFunctionOption, setSelectedFunctionOption] = useState();

  const [datasetsOptions, setDatasetOptions] = useState([]);
  const [functionsOptions, setFunctionOptions] = useState([]);

  // Images and predictions
  const [images, setImages] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [predictResults, setPredictResults] = useState([]);

  const [loading, setLoading] = useState(false);
  const [deleteDisabled, setDeleteDisabled] = useState(false);

  // Fetch datasets and functions
  useEffect(() => {
    const getOptions = async () => {
      try {
        const dataDataset = await fetchDatasets();
        setDatasetOptions(
          dataDataset.map((d) => ({ value: d, label: d.text }))
        );

        const dataFunctions = await fetchFunctions();
        setFunctionOptions(
          dataFunctions.map((f) => ({ value: f, label: f.text }))
        );
      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };
    getOptions();
  }, []);

  // Fetch images
  useEffect(() => {
    const getImages = async () => {
      try {
        const dataImages = await fetchImages();
        setImages(dataImages);
        setPredictResults(
          new Array(dataImages.length).fill("Prediction will appear here.")
        );
      } catch (error) {
        console.error("Failed to fetch images:", error);
      }
    };
    getImages();
  }, []);

  // Adjust currentIndex if images are removed
  useEffect(() => {
    if (currentIndex >= images.length) setCurrentIndex(images.length - 1);
  }, [images]);

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

      const response = await fecthPredict(
        selectedDatasetOption.value.id,
        selectedFunctionOption.value.id
      );

      const resultsArray = response.map((p) => p.prediction);
      setPredictResults(resultsArray);
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

  // Delete image
  const handleDeleteImage = async () => {
    if (images.length === 0 || deleteDisabled) return;

    setDeleteDisabled(true);
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

      const updatedImages = images.filter((_, idx) => idx !== currentIndex);
      const updatedResults = predictResults.filter(
        (_, idx) => idx !== currentIndex
      );

      setImages(updatedImages);
      setPredictResults(updatedResults);
      setCurrentIndex(Math.min(currentIndex, updatedImages.length - 1));
    } catch (err) {
      toast.error("Failed to delete image", {
        position: "top-right",
        autoClose: 4000,
        hideProgressBar: true,
        theme: "colored",
      });
      console.error(err);
    } finally {
      setTimeout(() => setDeleteDisabled(false), 2000);
    }
  };

  return (
    <div className="container">
      <div className="main-card">
        {/* Top Buttons and Dropdowns */}
        <div className="button-div-perceptron">
          <button onClick={() => navigate("/about")}>About</button>
          <button onClick={() => navigate("/canvas")}>Draw Image</button>
          {images.length > 0 ? (
            <>
              <button
                className="delete-image-button"
                onClick={handleDeleteImage}
                disabled={deleteDisabled}
              >
                Delete Image
              </button>
              <button onClick={handleExecute} id="executerButton">
                Execute
              </button>
            </>
          ) : (
            <p className="button-paragraph">
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

        {/* Image Slider with Results */}
        <div className="div-middle">
          <div className="slider-container-wrapper">
            <label>Test Images</label>
            {images.length > 0 ? (
              <div className="slider-container">
                {loading && <div className="loading-dots-textarea">...</div>}

                <SimpleImageSlider
                  className="slider"
                  width={400}
                  height={300}
                  images={images.map((img) => ({ url: img }))}
                  showNavs={true}
                  startIndex={currentIndex}
                  onStartSlide={(idx) => setCurrentIndex(idx - 1)}
                />
                <div className="slider-index">
                  {currentIndex + 1} / {images.length}
                </div>

                <div className="image-result">
                  {predictResults[currentIndex] || "No prediction yet."}
                </div>
              </div>
            ) : (
              <div className="no-images-placeholder">No images yet</div>
            )}
          </div>
        </div>
        <ToastContainer />
      </div>
    </div>
  );
};

export default PerceptronPage;
