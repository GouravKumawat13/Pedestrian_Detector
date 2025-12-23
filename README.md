# Pedestrian Detection using OpenCV (HOG + SVM)

This project implements a **pedestrian detection system** using classical computer vision techniques provided by OpenCV. It uses the **Histogram of Oriented Gradients (HOG)** feature descriptor combined with a **pre-trained Support Vector Machine (SVM)** model to detect humans in static images.

---

## 📌 Project Overview

- Implemented a pedestrian detection system using OpenCV’s **HOG feature descriptor**.
- Utilized OpenCV’s **pre-trained SVM model** specifically designed for human detection.
- Focuses on **classical computer vision techniques** without using deep learning models.

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- HOG (Histogram of Oriented Gradients)  
- SVM (Support Vector Machine)

---

## ⚙️ How It Works (Step-by-Step)

1. **Initialize HOG Descriptor**
   - Create a HOG descriptor object using OpenCV.
   - HOG extracts gradient-based features that capture human shape and structure.

2. **Load Pre-trained SVM Model**
   - Use OpenCV’s default SVM detector trained for pedestrian detection.
   - Avoids the need for manual model training.

3. **Load Input Image**
   - Read a static image using OpenCV’s image handling utilities.
   - Image is loaded in BGR color format by default.

4. **Convert Image to Grayscale**
   - Convert the input image from BGR to grayscale.
   - Reduces computational complexity and improves detection efficiency.

5. **Apply Multi-scale Detection**
   - Use a sliding window approach across multiple scales.
   - Enables detection of pedestrians of different sizes within the image.

6. **Configure Detection Parameters**
   - **Window Stride:** Controls the step size of the sliding window.
   - **Padding:** Improves detection near image borders.
   - **Scale Factor:** Handles variations in pedestrian size.

7. **Detect Pedestrians**
   - Extract HOG features from the image.
   - Use SVM classification to identify human figures.
   - Obtain bounding box coordinates for each detected pedestrian.

8. **Draw Bounding Boxes**
   - Draw rectangles around detected pedestrians.
   - Visually highlights detection results.

9. **Display Output**
   - Display the final image using OpenCV GUI functions.
   - Shows detected pedestrians with bounding boxes.

---

## 🚀 Future Enhancements and Scope

- Extend the system to support **real-time pedestrian detection** using live webcam feeds and video streams.
- Improve detection accuracy by **fine-tuning HOG parameters** and minimizing false-positive detections.
- Incorporate **confidence score thresholds** to retain only high-confidence pedestrian detections.
- Implement **Non-Maximum Suppression (NMS)** to effectively handle overlapping bounding boxes.
- Enable **batch processing of images** to support large-scale pedestrian detection tasks.
- Enhance result visualization by displaying **detection counts and confidence metrics** directly on output images.
- Perform a comparative analysis between **classical HOG + SVM methods** and **deep learning–based object detection models** (e.g., YOLO, SSD) to evaluate accuracy and performance trade-offs.
- Refactor the codebase into a **modular and reusable Python package** with configurable parameters for improved scalability and maintainability.

---

## ▶️ Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/GouravKumawat13/pedestrian-detection-opencv.git
