// backend/server.js
const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 5000;

app.use(cors());

let pythonProcess = null;

// 📦 Path to the Python script and output file
const scriptPath = path.join(__dirname, "../realtime_sign_detect.py");
const outputFile = path.join(__dirname, "../output.txt");

// 🚀 Start the Python script
app.get("/start-script", (req, res) => {
  if (!pythonProcess) {
    console.log("🔄 Starting Python script...");
    pythonProcess = spawn("python", [scriptPath]);

    pythonProcess.stdout.on("data", (data) => {
      console.log(`📤 Python stdout: ${data}`);
    });

    pythonProcess.stderr.on("data", (data) => {
      console.error(`❌ Python stderr: ${data}`);
    });

    pythonProcess.on("close", (code) => {
      console.log(`✅ Python script exited with code ${code}`);
      pythonProcess = null;
    });

    res.send("✅ Script started");
  } else {
    res.send("⚠️ Script is already running");
  }
});

// 📝 Read the latest predicted text
app.get("/predicted-text", (req, res) => {
  if (fs.existsSync(outputFile)) {
    const text = fs.readFileSync(outputFile, "utf8");
    res.json({ text });
  } else {
    res.json({ text: "" });
  }
});

app.listen(PORT, () => {
  console.log(`🚀 Backend running at: http://localhost:${PORT}`);
});
