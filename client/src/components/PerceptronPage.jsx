import { useNavigate } from "react-router-dom";
import { useEffect, useState, useRef } from "react";
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
import ImageGallery from "react-image-gallery";
import "react-image-gallery/styles/css/image-gallery.css";
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
  const galleryRef = useRef(null);

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
  const getImages = async () => {
    try {
      const dataImages = await fetchImages();
      setImages(dataImages);
      setPredictResults(
        new Array(dataImages.length).fill("Prediction will appear here.")
      );
      setCurrentIndex(0);
    } catch (error) {
      console.error("Failed to fetch images:", error);
    }
  };

  useEffect(() => {
    getImages();
  }, []);

  useEffect(() => {
    if (galleryRef.current) {
      galleryRef.current.slideToIndex(currentIndex);
    }
  }, [currentIndex, images]);

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
  // Delete image com confirmação
  // Estados adicionais
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [imageToDelete, setImageToDelete] = useState(null);

  // Abre modal
  const confirmDeleteImage = (index) => {
    setImageToDelete(index);
    setShowDeleteModal(true);
  };

  // Função real de delete
  const executeDeleteImage = async () => {
    if (imageToDelete === null || deleteDisabled) return;
    setDeleteDisabled(true);
    const url = images[imageToDelete];
    const filename = url.split("/").pop();

    try {
      await deleteImage(filename);
      toast.success("Image deleted successfully", {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: true,
        theme: "colored",
      });

      setImages((prevImages) => {
        const newImages = prevImages.filter((_, idx) => idx !== imageToDelete);

        setCurrentIndex((prevIndex) =>
          prevIndex >= newImages.length ? newImages.length - 1 : prevIndex
        );

        setPredictResults((prevResults) =>
          prevResults.filter((_, idx) => idx !== imageToDelete)
        );

        return newImages;
      });
    } catch (err) {
      toast.error("Failed to delete image", {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: true,
        theme: "colored",
      });
      console.error(err);
    } finally {
      setDeleteDisabled(false);
      setShowDeleteModal(false);
      setImageToDelete(null);
    }
  };

  return (
    <>
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
                  onClick={() => confirmDeleteImage(currentIndex)}
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
                  <div className="gallery-wrapper">
                    <ImageGallery
                      ref={galleryRef}
                      items={images.map((url) => ({
                        original: url,
                        thumbnail: url,
                      }))}
                      showThumbnails={false}
                      showPlayButton={false}
                      showFullscreenButton={false}
                      startIndex={currentIndex}
                      onSlide={(index) => setCurrentIndex(index)}
                      additionalClass="my-custom-gallery"
                    />
                  </div>

                  <div className="slider-index">
                    {currentIndex + 1} / {images.length}
                  </div>

                  {currentIndex < predictResults.length && (
                    <div className="image-result">
                      {loading ? (
                        <span className="loading-dots"></span>
                      ) : (
                        predictResults[currentIndex] || "No prediction yet."
                      )}
                    </div>
                  )}
                </div>
              ) : (
                <div className="no-images-placeholder">No images yet</div>
              )}
            </div>
          </div>
          <ToastContainer />
        </div>
      </div>
      {showDeleteModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Confirm Deletion</h3>
            <p>Are you sure you want to delete this image?</p>
            <div className="modal-buttons">
              <button onClick={() => setShowDeleteModal(false)}>Cancel</button>
              <button onClick={executeDeleteImage}>Delete</button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default PerceptronPage;
