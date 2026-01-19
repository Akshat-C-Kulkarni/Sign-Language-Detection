import React, { useState, useEffect } from "react";
import axios from "axios";

const PredictionBox = () => {
  const [text, setText] = useState("");

  const fetchPrediction = async () => {
    try {
      const res = await axios.get("http://localhost:5000/predicted-text");
      setText(res.data.text);
    } catch (err) {
      console.error("Error fetching prediction");
    }
  };

  useEffect(() => {
    const interval = setInterval(fetchPrediction, 1000); // poll every second
    return () => clearInterval(interval);
  }, []);

  return (
    <textarea
      value={text}
      onChange={(e) => setText(e.target.value)}
      style={{
        width: "400px",
        height: "200px",
        fontSize: "1rem",
        padding: "1rem",
        border: "1px solid #ccc",
        borderRadius: "10px",
      }}
    />
  );
};

export default PredictionBox;
