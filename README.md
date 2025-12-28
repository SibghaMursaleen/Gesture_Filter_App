# Gesture Controlled Filter Application

## 📌 Project Overview

This project is a **Gesture Controlled Camera Filter Application** built
using **Python**, **OpenCV**, and **MediaPipe**.\
It allows users to control real-time camera filters using **hand
gestures**, without using a keyboard or mouse.

The system detects hand landmarks and applies different visual effects
based on recognized gestures.

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python 3.x\
-   OpenCV\
-   MediaPipe\
-   NumPy

------------------------------------------------------------------------

## 🎯 Features

-   Real-time webcam feed
-   Hand landmark detection
-   Gesture-based filter switching
-   On-screen filter indicator
-   Smooth and interactive experience

------------------------------------------------------------------------

## ✋ Supported Gestures & Filters

  Gesture        Description              Applied Filter
  -------------- ------------------------ ----------------
  🖐 Open Palm    All fingers open         Grayscale
  ✌ Peace Sign   Index + Middle finger    Cartoon
  ✊ Fist        All fingers closed       Blur
  ☝ One Finger   Only index finger open   Sepia
  🤟 Rock Sign   Index + Pinky open       Edge Detection
  👌 OK Sign     Thumb + Index close      Invert Colors

------------------------------------------------------------------------

## ⚙ How It Works

1.  Webcam captures live video frames.
2.  MediaPipe detects hand landmarks.
3.  Finger positions are analyzed to recognize gestures.
4.  OpenCV applies corresponding filters in real time.
5.  Filter name is displayed on the screen.

------------------------------------------------------------------------

## ▶ How to Run

1.  Install required libraries:

```{=html}
<!-- -->
```
    pip install opencv-python mediapipe numpy

2.  Run the Python script:

```{=html}
<!-- -->
```
    python gesture_filter_app.py

3.  Press **Q** to exit the application.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add gesture cooldown to avoid accidental switching
-   Video recording feature
-   Background removal or blur
-   Multi-hand support
-   AI-based gesture classification

------------------------------------------------------------------------

## 👩‍💻 Author

Developed as a Computer Vision mini-project using OpenCV and MediaPipe.

------------------------------------------------------------------------

## 📜 License

This project is for educational purposes.
