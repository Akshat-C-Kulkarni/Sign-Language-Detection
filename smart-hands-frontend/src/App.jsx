import React from "react";
import Header from "./components/Header";
import StartButton from "./components/StartButton";
import PredictionBox from "./components/PredictionBox";
import ShareButton from "./components/ShareButton";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Header />
      <StartButton />
      <div className="content">
        <PredictionBox />
        <ShareButton />
      </div>
    </div>
  );
}

export default App;