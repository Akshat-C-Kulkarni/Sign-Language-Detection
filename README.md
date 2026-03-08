<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="900" height="200">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a0533"/>
      <stop offset="100%" style="stop-color:#0f172a"/>
    </linearGradient>
    <linearGradient id="acc6" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#f472b6"/>
      <stop offset="100%" style="stop-color:#c084fc"/>
    </linearGradient>
  </defs>
  <rect width="900" height="200" fill="url(#bg6)" rx="12"/>
  <!-- Camera frame -->
  <rect x="660" y="25" width="200" height="150" rx="6" fill="none" stroke="#f472b630" stroke-width="2"/>
  <!-- Corner brackets -->
  <path d="M 660 50 L 660 25 L 685 25" stroke="#f472b6" stroke-width="2" fill="none"/>
  <path d="M 835 25 L 860 25 L 860 50" stroke="#f472b6" stroke-width="2" fill="none"/>
  <path d="M 660 150 L 660 175 L 685 175" stroke="#f472b6" stroke-width="2" fill="none"/>
  <path d="M 835 175 L 860 175 L 860 150" stroke="#f472b6" stroke-width="2" fill="none"/>
  <!-- Hand silhouette dots (ASL) -->
  <circle cx="760" cy="100" r="6" fill="#f472b6" opacity="0.9"/>
  <circle cx="748" cy="80" r="4" fill="#c084fc" opacity="0.8"/>
  <circle cx="755" cy="62" r="3" fill="#c084fc" opacity="0.7"/>
  <circle cx="763" cy="50" r="3" fill="#c084fc" opacity="0.6"/>
  <circle cx="765" cy="78" r="4" fill="#f9a8d4" opacity="0.8"/>
  <circle cx="773" cy="59" r="3" fill="#f9a8d4" opacity="0.7"/>
  <circle cx="778" cy="47" r="3" fill="#f9a8d4" opacity="0.6"/>
  <circle cx="782" cy="76" r="4" fill="#e879f9" opacity="0.7"/>
  <circle cx="792" cy="60" r="3" fill="#e879f9" opacity="0.6"/>
  <circle cx="797" cy="49" r="3" fill="#e879f9" opacity="0.5"/>
  <!-- Lines -->
  <line x1="760" y1="100" x2="748" y2="80" stroke="#f472b640" stroke-width="1.5"/>
  <line x1="748" y1="80" x2="755" y2="62" stroke="#f472b640" stroke-width="1"/>
  <line x1="755" y1="62" x2="763" y2="50" stroke="#f472b640" stroke-width="1"/>
  <line x1="760" y1="100" x2="765" y2="78" stroke="#c084fc40" stroke-width="1.5"/>
  <line x1="765" y1="78" x2="773" y2="59" stroke="#c084fc40" stroke-width="1"/>
  <!-- Letter label -->
  <rect x="716" y="128" width="30" height="22" rx="4" fill="#f472b630"/>
  <text x="731" y="143" font-family="monospace" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">A</text>
  <text x="760" y="155" font-family="monospace" font-size="9" fill="#c084fc" text-anchor="middle">ASL Detected</text>
  <!-- Title -->
  <text x="50" y="82" font-family="Georgia, serif" font-size="32" font-weight="bold" fill="url(#acc6)">Sign Language</text>
  <text x="50" y="124" font-family="Georgia, serif" font-size="32" font-weight="bold" fill="url(#acc6)">Detection</text>
  <text x="50" y="162" font-family="monospace" font-size="12" fill="#6b7280">CNN · MediaPipe · OpenCV · Real-time ASL Recognition</text>
</svg>

# Sign Language Detection

> **Real-time ASL Sign Language recognition system using deep learning and computer vision — bridging communication for the hearing impaired**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-0F9D58?style=flat-square)](https://mediapipe.dev)
[![CNN](https://img.shields.io/badge/Model-CNN-FF6B35?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Complete-22c55e?style=flat-square)]()

</div>

---

## Overview

**Sign Language Detection** is a real-time computer vision system that recognizes American Sign Language (ASL) hand gestures and translates them into text. The system uses a CNN trained on hand landmark features extracted via MediaPipe, enabling fast and accurate gesture classification directly from webcam input.

This project addresses a real-world accessibility challenge: empowering the hearing-impaired community with a technology bridge to communicate more effectively.

---

## Architecture

```
┌───────────────────────────────────────────────────────────────────┐
│                   Sign Language Detection System                  │
│                                                                   │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────┐ │
│  │  Webcam     │───▶│  MediaPipe    │───▶│  21 Hand Landmarks  │ │
│  │  Live Feed  │     │  Hand Detect │     │  (x, y, z coords)   │ │
│  └─────────────┘     └──────────────┘     └────────┬────────────┘ │
│                                                    │              │
│                    ┌───────────────────────────────┘              │
│                    │  Preprocessing                               │
│                    │  (normalize, flatten, relative coords)       │
│                    ▼                                              │
│           ┌─────────────────┐                                     │
│           │  CNN Classifier  │                                    │
│           │  A-Z + Numbers   │                                    │
│           └────────┬────────┘                                     │
│                    │                                              │
│                    ▼                                              │
│           ┌──────────────────┐     ┌─────────────────┐            │
│           │  Predicted Sign  │───▶│  Text / Speech  │            │
│           │  (A, B, C...)    │     │  Output         │            │
│           └──────────────────┘     └─────────────────┘            │
└───────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Real-time ASL detection** at high frame rates using a standard webcam
- **21-landmark hand representation** via MediaPipe for robust feature extraction
- **CNN classifier** trained on normalized hand keypoints (invariant to scale/position)
- **A–Z alphabet + digits** detection coverage
- **Text output overlay** on live video feed
- **High accuracy** on validation set with minimal latency

---

## Detected Signs

| Category | Coverage |
|---|---|
| Alphabets | A–Z (excluding motion signs J, Z) |
| Digits | 0–9 |
| Common words | Hello, Thank You, Yes, No |

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| Deep Learning | TensorFlow / Keras |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Akshat-C-Kulkarni/Sign-Language-Detection.git
cd Sign-Language-Detection

# Install dependencies
pip install -r requirements.txt

# Run real-time detection
python detect.py

# Train model (optional)
python train.py
```

---

## Project Structure

```
Sign-Language-Detection/
├── backend/                      # Contains the Node.js Express server (`server.js`) that coordinates the app.
├── smart-hands-frontend/         # The React application source code.
├── realtime_sign_detect.py       # The core Python script for real-time sign language detection.
├── asl_model_v3.h5               # The trained model weights.
└── README.md
```

---

## Model Performance

| Metric | Value |
|---|---|
| Training Accuracy | ~97% |
| Validation Accuracy | ~93% |
| Inference Speed | Real-time (30fps) |
| Classes | 26+ |

---

## Author

**Akshat C. Kulkarni**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/akshatckulkarni)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github)](https://github.com/Akshat-C-Kulkarni)

---

<div align="center"><sub>Built with Python · TensorFlow · MediaPipe · OpenCV</sub></div>
