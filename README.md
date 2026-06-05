<div align="center">

# 😷 Face Mask Detection AI

### Real-Time Face Mask Detection using TensorFlow, MobileNetV2 & OpenCV

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">

</div>

---

## 🚀 Overview

A real-time computer vision application that detects whether a person is wearing a face mask using a MobileNetV2-based deep learning model.

---

## ⚡ Features

<table>
<tr>
<td>📹 Real-Time Detection</td>
<td>🧠 MobileNetV2 Transfer Learning</td>
</tr>

<tr>
<td>🖼️ Image Prediction</td>
<td>⚡ Fast Inference</td>
</tr>

<tr>
<td>🎯 Face Detection</td>
<td>📊 Binary Classification</td>
</tr>
</table>

---

## 🏗️ Pipeline

```mermaid
flowchart TD
    A[Webcam / Image] --> B[Face Detection]
    B --> C[Face Cropping]
    C --> D[Preprocessing]
    D --> E[MobileNetV2]
    E --> F[Prediction]
    F --> G[Mask / No Mask]
```

## 📂 Project Structure

```text
MaskDetectionAI
│
├── dataset/
├── train.py
├── webcam.py
├── predict.py
├── mask_detector.h5
├── README.md
├── requirements.txt
└── .gitignore
```

## 📸 Demo

<p align="center">
  <img src="screenshots/demo.png" width="700">
</p>

## 🛠️ Run Project

```bash
pip install -r requirements.txt
python train.py
python webcam.py
```

## 👨‍💻 Author

### Sathvik Munaga

AI End Semester Project
