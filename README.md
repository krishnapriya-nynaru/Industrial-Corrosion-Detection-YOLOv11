# Industrial-Corrosion-Detection-YOLOv11
 This repository showcases industrial corrosion detection using the YOLOv11 model trained on a custom dataset. It identifies and classifies 18 corrosion-related types, including different severity levels like Low, Medium, and High corrosion, as well as Rust. The project aims to deliver an efficient and accurate solution for industrial maintenance and asset management.
## Corrosion Detection Using YOLOv11
This repository implements an industrial corrosion detection system using the YOLOv11 model, trained on a custom dataset. The model is capable of detecting and classifying 18 different corrosion-related types, ranging from various severity levels such as Low, Medium, and High corrosion to specific forms like Rust, Oxidation, and Crevice corrosion. The project aims to provide an automated solution for inspecting and managing industrial assets, aiding in preventive maintenance and reducing the risk of undetected corrosion.

## Table of Contents
- [Key Features](#key-features)
- [Model Training](#model-training)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Key Features:
- ***18 Corrosion Classes:*** Detect various corrosion types, including Corrosion, Rust, Oxidation-Corrosion, High-Corrosion, and more.
- ***Custom Dataset:*** Trained on a specially curated corrosion dataset for high accuracy in industrial applications.
- ***Efficient Inference:*** Powered by YOLOv11 for fast and reliable real-time detection.
- ***Use Cases:*** Applicable to industrial asset management, corrosion monitoring, and preventive maintenance systems.

## Model Training
The corrosion detection model was trained using the YOLOv11 architecture on a custom dataset sourced from Roboflow. The dataset contains 18 corrosion-related classes, ranging from various severity levels such as Rust, High-Corrosion, and Oxidation-Corrosion, designed to enable accurate detection of corrosion in industrial settings.

### Dataset
***Dataset Source:*** [Rust Dataset on Roboflow](https://universe.roboflow.com/rust-r6xzj/rust-dataset-uk2zn)

***Classes:*** 18 corrosion-related types, including Low, Medium, and High corrosion, as well as various corrosion forms like Rust, Crevice, and Oxidation.

### Training Specifications & Hyperparameters
**Model:** YOLOv11
**Framework:** Ultralytics YOLOv11
**Epochs:** 100
**Batch Size:** 16
**Image Size:** 640x640
**Optimizer:** Adam (with custom learning rate)
**Learning Rate:** 0.001 (adjusted for training stability)
**Warmup Epochs:** 5
**Momentum:** 0.937
**Weight Decay:** 0.0005
**Data Augmentation:** Used during training to enhance model robustness
### Training Process
The model was trained for 100 epochs, with training taking approximately 2 hours on a machine with an ***NVIDIA GPU***.
The training process followed the standard ***YOLOv11 training pipeline***, ensuring robust model performance and accuracy.

**Roboflow Integration:** The dataset was preprocessed and augmented via Roboflow, ensuring it met the input specifications for YOLOv11 training.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/krishnapriya-nynaru/Industrial-Corrosion-Detection-YOLOv11.git
2. Install required packages :
    ```bash
    pip install "ultralytics<=8.3.40" supervision roboflow opencv-python matplotlib
3. Change to Project Directory
    ```bash
    cd Industrial_corrosion_detection_yolov11

## Usage
Run the script with Python

For a single image:
```bash
python corrosion_detection.py --input path/to/image.jpg --model /path/to/model
```
For a folder of images:
```bash
python corrosion_detection.py --input path/to/image_folder --model /path/to/model
```
For a video file:
```bash
python corrosion_detection.py --input path/to/video.mp4 --model /path/to/model
```
For webcam (e.g., default webcam):
```bash
python corrosion_detection.py --input 0 --model /path/to/model
```
**Explanation:**

***--input:*** Accepts paths to images, folders, videos, or webcam ID.

***--model:*** Specifies the path to the trained YOLOv11 model.

***--output:*** Specifies the output folder for saving results (optional, defaults to results)

## Results

![alt text](https://github.com/krishnapriya-nynaru/Industrial-Corrosion-Detection-YOLOv11/blob/main/Industrial_corrosion_detection_yolov11/results/outputcorrosion_1.jpg?raw=true) 
![alt text](https://github.com/krishnapriya-nynaru/Industrial-Corrosion-Detection-YOLOv11/blob/main/Industrial_corrosion_detection_yolov11/results/outputcorrosion_7.jpg?raw=true) 
## Contributing
Contributions are welcome! To contribute to this project:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure the code passes all tests.
4. Submit a pull request with a detailed description of your changes.

If you have any suggestions for improvements or features, feel free to open an issue!

## Acknowledgments
- [**YOLOv11 for object detection.**](https://github.com/ultralytics/yolov11)
- [**Managed and augmented the corrosion dataset**](https://roboflow.com/)
- [**OpenCV for computer vision functionalities.**](https://opencv.org/)
- [**The framework used for model training.**](https://pytorch.org/)

