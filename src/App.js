import React, { useState } from "react";
import axios from "axios";
import { Loader } from "lucide-react";
import TableComponent  from "./components/TableComponent";
import "./App.css";

const App = () => {
  const [file, setFile] = useState(null);
  const [predictions, setPredictions] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  console.log(predictions);
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setPredictions(null);
    setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select an image first.");
      return;
    }

    setLoading(true);
    setPredictions(null);
    setError(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:4000/predict", formData);
      setPredictions(response.data);
    } catch (error) {
      console.error("Prediction error", error);
      setError("Failed to predict. Please try again.");
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="main-container">
      {!predictions && (<div className="main-card">
        <h1 className="heading">Skin Disease Predictor</h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <input type="file" accept="image/*" onChange={handleFileChange} className="my-input" />
          <button type="submit" className="my-button">Predict</button>
        </form>
        {loading && <Loader className="animate-spin mx-auto mt-4" />}
        {error && <p className="error-msg">{error}</p>}
      </div>)}

      {predictions && (
        <div className="result-card">
          <h2 className="prediction-heading">Prediction Results</h2>
          {predictions.image_url && (
            <img src={`http://localhost:4000${predictions.image_url}`} alt="Uploaded" className="result-img" />
          )}
          <TableComponent data={predictions} />
        </div>
      )}
    </div>
  );
};

export default App;
