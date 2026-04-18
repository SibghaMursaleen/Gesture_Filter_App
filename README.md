# 🖐️ Gesture-Controlled Camera Filter App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg)](https://mediapipe.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A high-performance, real-time computer vision application that leverages hand gesture recognition to switch between various cinematic filters. Built with **Python**, **OpenCV**, and **MediaPipe**, this project demonstrates seamless human-computer interaction (HCI) through motion tracking.

---

## ✨ Features

- 🚀 **Real-time Processing**: Zero-latency hand landmark detection and tracking.
- 👋 **Intuitive Control**: Switch filters instantly using natural hand gestures.
- 🎨 **Diverse Filter Palette**: Includes Grayscale, Cartoonize, Blur, Sepia, Edge Detection, and Inversion.
- 🖥️ **HUD Overlay**: On-screen display indicating the active filter and hand tracking status.
- 🛠️ **Cross-Platform**: Runs on Windows, macOS, and Linux.

---

## ✋ Supported Gestures & Filters

| Gesture | Movement | Applied Filter | Description |
| :-- | :-- | :-- | :-- |
| ✋ | **Open Palm** | `Grayscale` | Classic black and white cinematic look. |
| ✌️ | **Peace Sign** | `Cartoon` | Stylized bilateral filter for a comic-book effect. |
| ✊ | **Fist** | `Blur` | High-radius Gaussian blur for privacy or focus. |
| ☝️ | **Index Finger** | `Sepia` | Vintage warmth with a classic sepia tone. |
| 🤟 | **Rock Sign** | `Edge Detection` | Canny edge detection for a technical/sketch layout. |
| 👌 | **OK Sign** | `Invert` | Color bitwise inversion for a high-contrast negative look. |

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Clone the Repository
```bash
git clone https://github.com/SibghaMursaleen/Gesture_Filter_App.git
cd Gesture_Filter_App
```

### 3. Install Dependencies
```bash
pip install opencv-python mediapipe numpy
```

---

## 🚀 Usage

Run the application using the following command:

```bash
python main.py
```

### ⌨️ Controls
- **Gestures**: Show your hand to the camera to trigger filters.
- **`Q` Key**: Press 'q' on your keyboard to exit the application.

---

## ⚙️ How it Works

1. **Capture**: Access the webcam stream using OpenCV's `VideoCapture`.
2. **Processing**: MediaPipe's Hand solution tracks 21 distinct 3D landmarks on the hand.
3. **Recognition**: Custom logic determines finger states (open/closed) by comparing coordinates of finger tips vs. joints.
4. **Rendering**: OpenCV applies image processing pipelines (Kernels, Thresholds, Transformations) based on the recognized gesture ID.

---

## 📂 Project Structure

```text
Gesture_Filter_App/
├── main.py          # Core application logic
├── README.md        # Project documentation
└── .gitignore       # Git exclusion rules
```

---

## 🚀 Future Roadmap

- [ ] Add support for dual-hand gestures for combined filters.
- [ ] Implement a recording feature to save filtered clips.
- [ ] UI enhancement with a sidebar for settings.
- [ ] Support for deep learning-based custom gesture training.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**Sibgha Mursaleen**
- [GitHub](https://github.com/SibghaMursaleen)
- [LinkedIn](https://www.linkedin.com/in/sibgha-mursaleen/)

---
<p align="center">Made with ❤️ for Computer Vision Enthusiasts</p>
