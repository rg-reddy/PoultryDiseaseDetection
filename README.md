# Poultry Disease Detection System

## Project Overview

This project uses Transfer Learning with the VGG16 deep learning model to classify poultry diseases from poultry images.

The system predicts one of the following classes:

* Healthy
* Coccidiosis
* New Castle Disease
* Salmonella

A Flask web application is integrated with the trained model to provide real-time disease prediction through a simple and user-friendly interface.

The project was developed as part of the SmartInternz Virtual Internship Program in collaboration with APSCHE.

---

## Features

* VGG16 Transfer Learning Model
* Poultry Disease Classification
* Image Upload and Preview
* Real-Time Disease Prediction
* Flask Web Application
* Responsive User Interface
* Sample Test Images
* Project Documentation
* Project Demonstration Video
* Disease Prediction Results Display
* User-Friendly Web Interface

---

## Technologies Used

### Programming Language

* Python

### Deep Learning Framework

* TensorFlow
* Keras

### Web Framework

* Flask

### Frontend Technologies

* HTML
* CSS

### Libraries

* NumPy
* OpenCV
* Pillow

### Version Control

* Git
* GitHub

---

## Dataset

Dataset Source:

https://www.kaggle.com/datasets/chandrashekarnatesh/poultry-diseases

Dataset Classes:

* Healthy
* Coccidiosis
* New Castle Disease
* Salmonella

A subset of the dataset was used for training and testing purposes.

### Dataset Note

The original dataset is not included in this repository due to GitHub storage limitations.

Please download the dataset from the Kaggle link above and organize it into the appropriate folders before training the model.

Example Structure:

```text
dataset/
├── train/
├── test/
└── val/
```

---

## Model Information

The trained model file (`poultry_disease_model.h5`) is not included in this repository because its size exceeds GitHub's file upload limitations.

Model Details:

* Model Architecture: VGG16 Transfer Learning
* Framework: TensorFlow / Keras
* File Format: .h5
* Model Size: Approximately 374 MB

The application was developed, trained, and tested using the trained model stored locally.

To run the application successfully, place the trained model file inside the following directory:

```text
model/
└── poultry_disease_model.h5
```

---

## Project Structure

```text
PoultryDiseaseProject
│
├── document/
│   └── Poultry_Disease_Report.docx
│
├── video_demo/
│   └── Poultry_Disease_Detection_Demo.mp4
│
├── project_files/
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   ├── static/
│   └── sample_images/
│
├── model/
│
├── dataset/
│
├── notebooks/
│
├── screenshots/
│
├── sample_images/
│
├── static/
│
├── templates/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Application Screenshots

### Home Page

![Home Page](screenshots/01_home_page.png)

### Prediction Page

![Prediction Page](screenshots/02_prediction_page.png)

### Image Upload

![Image Upload](screenshots/03_image_uploaded.png)

### Healthy Prediction

![Healthy Prediction](screenshots/04_healthy_prediction.png)

### Coccidiosis Prediction

![Coccidiosis Prediction](screenshots/05_coccidiosis_prediction.png)

### Salmonella Prediction

![Salmonella Prediction](screenshots/06_salmonella_prediction.png)

### New Castle Disease Prediction

![New Castle Disease Prediction](screenshots/07_newcastle_disease_prediction.png)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rg-reddy/PoultryDiseaseDetection.git
```

Navigate to the project directory:

```bash
cd PoultryDiseaseDetection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the trained model file:

```text
model/
└── poultry_disease_model.h5
```

Run the application:

```bash
python app.py
```

Open the application:

```text
http://127.0.0.1:5000
```

---

## Results

The developed system successfully classifies poultry diseases into:

* Healthy
* Coccidiosis
* New Castle Disease
* Salmonella

using a VGG16 Transfer Learning model integrated with a Flask web application.

The application provides real-time disease prediction from uploaded poultry images through an intuitive web interface.

---

## Project Report

Project documentation is available in:

```text
document/Poultry_Disease_Report.docx
```

---

## Demonstration Video

Project demonstration video is available in:

```text
video_demo/Poultry_Disease_Detection_Demo.mp4
```

---

## Future Improvements

* Improve model accuracy using larger datasets
* Deploy the application to cloud platforms
* Add confidence score visualization
* Support mobile-friendly deployment
* Develop an Android application
* Integrate cloud-based prediction services
* Add disease treatment recommendations
* Support additional poultry diseases

---

## Project Links

### GitHub Repository

https://github.com/rg-reddy/PoultryDiseaseDetection

### LinkedIn Profile

https://www.linkedin.com/in/raja-gopala-reddy-bora-754b172a1

### Dataset

https://www.kaggle.com/datasets/chandrashekarnatesh/poultry-diseases

---

## Internship Information

**Program:** SmartInternz Virtual Internship Program

**Project Title:** Transfer Learning-Based Classification of Poultry Diseases for Enhanced Health Management

**Department:** Computer Science and Engineering (Artificial Intelligence & Machine Learning)

**College:** Maharaj Vijayaram Gajapathi Raj College of Engineering

**Faculty Mentor:** Satyanarayana Reddy

**Academic Year:** 2026–2027

---

## Author

**BORA RAJA GOPALA REDDY**

GitHub:
https://github.com/rg-reddy

LinkedIn:
https://www.linkedin.com/in/raja-gopala-reddy-bora-754b172a1
