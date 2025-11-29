# AI GUN – Intelligent Threat Detection and Tracking System

AI GUN is an AI-driven security assistance system designed to automatically detect, classify, and track potential threats using computer vision and machine learning. Traditional surveillance systems depend heavily on human monitoring, which can be slow, inconsistent, and prone to error.
AI GUN addresses these limitations by offering real-time object detection, automated threat evaluation, and optional hardware-based tracking using servo motors.

---

## 1. Core Features

### 1.1 Object Detection and Recognition

Uses deep learning models to identify:

* People
* Face mask vs. no-mask
* Vehicles
* Other objects depending on the trained model

### 1.2 Threat Assessment

Evaluates detected objects based on configurable rules such as:

* Behavior
* Object type
* Presence of restricted items
* Movement patterns

### 1.3 Real-Time Alerts

Generates instant alerts containing:

* Detected object type
* Timestamp
* Location in frame
* Confidence scores

### 1.4 System and Hardware Integration

AI GUN can integrate with:

* CCTV cameras
* Drones
* External sensors
* Servo-mounted tracking modules

### 1.5 Continuous Learning

Supports model retraining and updates based on new datasets and real-world scenarios to improve accuracy over time.

---

## 2. Face Mask Detection Model

### Dataset

Kaggle dataset used for mask classification:
[https://www.kaggle.com/datasets/omkargurav/face-mask-dataset](https://www.kaggle.com/datasets/omkargurav/face-mask-dataset)

### Training Code

Training script available on Google Drive:
[https://drive.google.com/file/d/1QK4EG9YsXP_k8tHUktAwgIzCcJ9TCCai/view](https://drive.google.com/file/d/1QK4EG9YsXP_k8tHUktAwgIzCcJ9TCCai/view)

### Sample Output

<img width="720" height="1247" alt="model output" src="https://github.com/user-attachments/assets/e36bc7f2-dc81-487a-a306-e6e36c477651" />

---

## 3. Reference Material for Face Mask Module

### Tutorials

YouTube tutorial:
[https://www.youtube.com/watch?v=IOI0o3Cxv9Q&t=2892s](https://www.youtube.com/watch?v=IOI0o3Cxv9Q&t=2892s)

### Dataset Annotation Tools

LabelImg dataset used for manual labeling.
Custom dataset (Google Drive):
[https://drive.google.com/file/d/1xLWpKyu4luFNvhLEyu_9Q2ovYJj29doy/view](https://drive.google.com/file/d/1xLWpKyu4luFNvhLEyu_9Q2ovYJj29doy/view)

---

## 4. Cloud Training (Recommended)

Training on Google Colab is faster and easier.
Colab Notebook:
[https://colab.research.google.com/github/deepme987/Tensorflow-Object-Detection/blob/master/Object_Detection_Face_Mask_Detection.ipynb#scrollTo=V8V1RRQBN6kv](https://colab.research.google.com/github/deepme987/Tensorflow-Object-Detection/blob/master/Object_Detection_Face_Mask_Detection.ipynb#scrollTo=V8V1RRQBN6kv)

---

## 5. System Workflow

Complete workflow and planning document (PDF):
[https://github.com/Grandlobster/A.i_Gun/files/14457968/plan-1.1.pdf](https://github.com/Grandlobster/A.i_Gun/files/14457968/plan-1.1.pdf)

---

## 6. Servo Motor Module

Used for automatic target tracking and positioning.
Servo calibration and algorithms are located in the `servo/` folder.

### Reference Tutorials

* Servo Basics (SparkFun):
  [https://www.sparkfun.com/tutorials/304](https://www.sparkfun.com/tutorials/304)
* Prototype Laser Turret:
  [https://www.youtube.com/watch?v=S3CwzkT6cK4](https://www.youtube.com/watch?v=S3CwzkT6cK4)
* External Power Supply Guide:
  [https://www.youtube.com/watch?v=xHXVufb5AkQ](https://www.youtube.com/watch?v=xHXVufb5AkQ)
* Auto-Targeting Turret Reference:
  [https://github.com/tomash1234/auto-targeting-turret](https://github.com/tomash1234/auto-targeting-turret)
* Headshot Tracker Reference:
  [https://github.com/rizkydermawan1992/Face-Detection](https://github.com/rizkydermawan1992/Face-Detection)
* Servo Mounting Tutorial:
  [https://www.youtube.com/watch?v=IILDOLuBfzM](https://www.youtube.com/watch?v=IILDOLuBfzM)

---

## 7. Circuit and Components

Circuit Diagram:
![circuit](https://github.com/Grandlobster/A.i_Gun/assets/118823460/afff3a97-89cc-40bf-aa33-9fc057ea5522)

Additional schematic: <img width="386" height="340" alt="schematic" src="https://github.com/user-attachments/assets/08ece8c1-0c48-4ac8-8f6c-82781a9300c9" />

---

## 8. Future Improvements

* Servo auto-calibration
* Integration of newer models (YOLOv8, YOLO-NAS)
* Cloud-based real-time dashboard
* Improved hardware enclosure and mounting

---
