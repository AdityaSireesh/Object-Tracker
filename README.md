# Multi-Backend Object Tracker (CPU & GPU)

A versatile object tracking application built with Python. This project features a dual-backend architecture, allowing users to run a lightweight, CPU-based tracker using OpenCV's DNN module and YOLOv4, or switch to a high-performance, GPU-accelerated tracker using PyTorch and YOLOv8. 

## ✨ Features

*   **Dual Backend Options:** Easily toggle between CPU processing (OpenCV/YOLOv4) and GPU acceleration (PyTorch/YOLOv8).
*   **Real-Time Detection:** Generates accurate bounding boxes using YOLO architectures.
*   **Object Tracking Logic:** Calculates center points and tracks pixel movement between frames to assign and maintain unique vehicle IDs.

## 🛠️ Installation & Setup

### 🅰️ CPU Setup (OpenCV & YOLOv4)
The CPU tracker specifically requires OpenCV 4.x
```
pip install "opencv-python<5" numpy
```
Download the official [YOLOv4 weights file](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights)

### 🅱️ GPU Setup (PyTorch & YOLOv8)
Requires an NVIDIA GPU and CUDA Toolkit installed on your system.
```
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)
pip install ultralytics opencv-python numpy
```

## 🚀 Usage: Switching Between CPU and GPU
Switch tracker backend modifying the imports at the top of main.py.
- For CPU (YOLOv4):
`from object_detection import ObjectDetection`
- For GPU (YOLOv8):
`from gpu_object_detection import ObjectDetection`

## 📂 Project Structure
Object-Tracker/     <br>
├── main.py         <br>
├── object_detection.py      &emsp;&emsp;&emsp; # CPU YOLOv4 Logic        <br>
├── gpu_object_detection.py  &emsp; # GPU YOLOv8 Logic         <br>
└── dnn_model/               &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; # Required for CPU only   <br>
&emsp; ├── classes.txt       <br>
&emsp; ├── yolov4.cfg        <br>
&emsp; └── yolov4.weights    <br>   
