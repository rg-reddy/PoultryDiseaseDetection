# Poultry Disease Detection System

## Project Overview

This project uses Transfer Learning with the VGG16 deep learning model to classify poultry diseases from poultry images.

The system predicts one of the following classes:

* Healthy
* Coccidiosis
* New Castle Disease
* Salmonella

A Flask web application is integrated with the trained model to provide real-time disease prediction through a simple and user-friendly interface.

---

## Features

* VGG16 Transfer Learning Model
* Poultry Disease Classification
* Image Upload and Preview
* Real-Time Disease Prediction
* Flask Web Application
* Responsive User Interface
* Sample Test Images
* Project Documentation and Demo Video

---

## Technologies Used

* Python
* TensorFlow
* Keras
* Flask
* HTML
* CSS
* NumPy
* OpenCV

---

## Dataset

Dataset Source:

Poultry Pathology Visual Dataset (Kaggle)

Classes:

* Healthy
* Coccidiosis
* New Castle Disease
* Salmonella

A subset of the dataset was used for training and testing purposes.

---

## Project Structure

```text
PoultryDiseaseProject
│
├── document/
│   └── Poultry_Disease_Detection_Report.pdf
│
├── video_demo/
│   └── Poultry_Disease_Detection_Demo.mp4
│
├── project_files/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
├── templates/
├── screenshots/
├── sample_images/
├── model/
├── dataset/
└── notebooks/
```

---

## Application Screenshots

### Home Page

![Home Page](screenshots/home_page.png)

### Prediction Page

![Prediction Page](screenshots/predict_page.png)

### Image Selected

![Image Selected](screenshots/image_selected.png)

### Healthy Prediction

![Healthy Prediction](screenshots/healthy_prediction.png)

### Coccidiosis Prediction

![Coccidiosis Prediction](screenshots/coccidiosis_prediction.png)

### Salmonella Prediction

![Salmonella Prediction](screenshots/salmonella_prediction.png)

### New Castle Disease Prediction

![New Castle Disease Prediction](screenshots/newcastle_prediction.png)

---

## Installation

```bash
pip install -r requirements.txt
python app.py
```

Open:

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

---

## Future Improvements

* Improve model accuracy using larger datasets
* Deploy the application to cloud platforms
* Add confidence score visualization
* Support mobile-friendly deployment

---

## Note

The trained model file is not included in this repository because the file size exceeds GitHub's standard upload limits.

---

## Author

**BORA RAJA GOPALA REDDY**

GitHub:
https://github.com/rg-reddy
