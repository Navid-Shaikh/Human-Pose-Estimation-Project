# Real-Time Human Pose Estimation with MediaPipe

https://github.com/user-attachments/assets/your-video-asset-id
<!-- Replace the above line with the actual GitHub video embed link after uploading (instructions below) -->

<video src="demo.mp4" controls></video>
<!-- Alternative if direct video doesn't preview well: Use the GitHub asset link above -->

A real-time human pose estimation project built using **MediaPipe** and **OpenCV**. Detects 33 key body landmarks from your webcam, draws a smooth skeleton overlay, and runs in **full-screen mode** for an immersive demo.

This is a solid foundation for my ongoing final-year project on **exercise tracking and posture analysis**!

## 🚀 Features
- Real-time pose detection with Google's pre-trained MediaPipe model
- High accuracy (`model_complexity=2`, smoothed landmarks, higher confidence thresholds)
- Full-screen immersive display (1920x945)
- Toggle full-screen with **F** key
- Higher webcam resolution (1280x720) for better input quality
- Smooth, stable tracking with reduced jitter

## 📸 Sample Outputs

![Pose Example 1](outputs/output1.jpg)
![Pose Example 2](outputs/output2.jpg)
![Pose Example 3](outputs/output3.jpg)

*(Add 2–3 clear screenshots in the `outputs/` folder for quick visual reference)*

## 🛠️ Tech Stack
- Python
- MediaPipe (Google)
- OpenCV

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Navid-Shaikh/human-pose-estimation-mediapipe.git
   cd human-pose-estimation-mediapipe
