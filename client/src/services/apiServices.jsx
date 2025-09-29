export const fecthPredict = async (dataset_id, function_id) => {
  const data = { dataset_id, function_id };
  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Error in prediction: " + response.statusText);
    }

    const result = await response.json();
    console.log("Server response (predict):", result);
    return result;
  } catch (error) {
    console.error("fecthPredict error:", error);
    throw error;
  }
};

export const fetchUpload = async (files) => {
  const formData = new FormData();
  files.forEach((file) => formData.append("files", file));

  try {
    const response = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Upload error: " + response.statusText);
    }

    const result = await response.json();
    console.log("Server response (upload):", result);
    return result;
  } catch (error) {
    console.error("fetchUpload error:", error);
    throw error;
  }
};

export const fetchDatasets = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/datasets", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new Error("Error getting datasetts " + response.statusText);
    }

    const result = await response.json();
    console.log("Server response (datasets):", result);
    return result;
  } catch (error) {
    console.error("fetchDatasets error:", error);
    throw error;
  }
};

export const fetchFunctions = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/functions", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new Error("Error getting functions: " + response.statusText);
    }

    const result = await response.json();
    console.log("Server response (functions):", result);
    return result;
  } catch (error) {
    console.error("fetchFunctions error:", error);
    throw error;
  }
};

export const fetchImages = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/getImages", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new Error("Error getting images: " + response.statusText);
    }

    const result = await response.json();
    console.log("Server response (images):", result);
    return result;
  } catch (error) {
    console.error("fetchImages error:", error);
    throw error;
  }
};

export const deleteImage = async (filename) => {
  try {
    const response = await fetch(
      `http://127.0.0.1:5000/deleteImage/${filename}`,
      {
        method: "DELETE",
      }
    );
    if (!response.ok) {
      throw new Error("Error getting images: " + response.statusText);
    }
    const result = await response.json();
    console.log("Server response (images):", result);
    return result;
  } catch (error) {
    console.error("fetchImages error:", error);
    throw error;
  }
};
