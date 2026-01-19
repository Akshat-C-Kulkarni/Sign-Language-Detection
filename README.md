# Sign Language Detection App

This project is a real-time American Sign Language (ASL) detection application. It uses computer vision and deep learning to translate hand gestures into text instantly.

## 🌟 Introduction

The application bridges the communication gap by interpreting ASL gestures in real-time. It leverages a Python-based deep learning model for gesture recognition and presents the output through a modern, user-friendly React frontend.

## 🔄 Workflow

1.  **Frontend (React)**: The user interface where the comprehensive "Workflow" is displayed and users can interact with the system.
2.  **Backend (Node.js/Express)**: Acts as an intermediary, managing the execution of the Python script and serving data to the frontend.
3.  **AI Engine (Python)**:
    -   Captures video from the webcam.
    -   Processes frames using **MediaPipe** for hand tracking.
    -   Predicts gestures using a trained **TensorFlow/Keras** model.
    -   Outputs the detected text to a shared file (`output.txt`), which the backend reads and sends to the frontend.

## 📂 Folder Structure

-   `backend/`: Contains the Node.js Express server (`server.js`) that coordinates the app.
-   `smart-hands-frontend/`: The React application source code.
-   `realtime_sign_detect.py`: The core Python script for real-time sign language detection.
-   `ASL_Project.zip` / `asl_dataset/`: Project datasets and resources.
-   `asl_model_v3.h5`: The trained model weights.

## 🚀 How to Run the App

### Prerequisites

-   **Node.js** & **npm** installed.
-   **Python 3.x** installed.

### 1. Install Dependencies

**Python:**
Ensure you have the necessary Python libraries installed (e.g., `opencv-python`, `mediapipe`, `tensorflow`, `numpy`).
```bash
pip install opencv-python mediapipe tensorflow numpy
```

**Backend:**
Navigate to the backend directory and install Node modules:
```bash
cd backend
npm install
```

**Frontend:**
Navigate to the frontend directory and install dependencies:
```bash
cd smart-hands-frontend
npm install
```

### 2. Start the Application

You need to run the backend and frontend terminals simultaneously.

**Step 1: Start the Backend**
From the `backend` directory:
```bash
node server.js
```
*This will start the server on port 5000.*

**Step 2: Start the Frontend**
From the `smart-hands-frontend` directory:
```bash
npm start
```
*This will launch the React app in your browser (usually at http://localhost:3000).*

### 3. Usage

-   Once the app is running, use the UI controls to start the detection script.
-   The webcam window will appear, tracing your hand landmarks.
-   Perform ASL gestures, and the predicted text will appear on the screen in real-time.
