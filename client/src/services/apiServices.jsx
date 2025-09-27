export const fecthPredict = async (id1, id2) => {
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok " + response.statusText);
      }
      return response.json();
    })
    .then((result) => {
      console.log("Server response:", result);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

export const fetchDatasets = async () => {
  const response = await fetch("http://127.0.0.1:5000/datasets", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Failed to Fetch");
  }

  return await response.json();
};

export const fetchFunctions = async () => {
  const response = await fetch("http://127.0.0.1:5000/functions", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Failed to Fetch");
  }
  return await response.json();
};
