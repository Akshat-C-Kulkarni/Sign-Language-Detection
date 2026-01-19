import React from "react";

const StartButton = () => {
  const startPrediction = async () => {
    try {
      await fetch("http://localhost:5000/start-script"); // optional if you want to use a local server
      alert("Prediction started. Check webcam window.");
    } catch (err) {
      alert("Could not start prediction.");
    }
  };

  return (
    <button
      onClick={startPrediction}
      style={{
        marginTop: "1.5rem",
        padding: "1rem 2rem",
        fontSize: "1rem",
        cursor: "pointer",
        backgroundColor: "#3498db",
        color: "#fff",
        border: "none",
        borderRadius: "10px",
      }}
    >
      Start Prediction
    </button>
  );
};

export default StartButton;
