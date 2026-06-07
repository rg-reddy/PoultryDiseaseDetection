import os
import numpy as np
import tensorflow as tf

from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from werkzeug.utils import secure_filename

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------

UPLOAD_FOLDER = "static/uploads"
MODEL_PATH = "model/poultry_disease_model.h5"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Load Model
# -----------------------------

print("Loading model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")

# -----------------------------
# Class Labels
# -----------------------------

labels = [
    "Coccidiosis",
    "Healthy",
    "New Castle Disease",
    "Salmonella"
]

# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Prediction Page
# -----------------------------

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        if "image" not in request.files:
            return "No file uploaded"

        file = request.files["image"]

        if file.filename == "":
            return "No file selected"

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        # -------------------------
        # Image Preprocessing
        # -------------------------

        img = load_img(
            filepath,
            target_size=(224, 224)
        )

        img_array = img_to_array(img)

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        # -------------------------
        # Prediction
        # -------------------------

        prediction = model.predict(
            img_array,
            verbose=0
        )

        predicted_index = np.argmax(prediction)

        print("\n==============================")
        print("Uploaded File:", filename)
        print("Prediction Scores:", prediction)
        print("Predicted Index:", predicted_index)
        print("Predicted Label:", labels[predicted_index])
        print("==============================\n")

        predicted_class = labels[predicted_index]

        image_path = "/" + filepath.replace("\\", "/")

        return render_template(
            "result.html",
            prediction=predicted_class,
            image_path=image_path
        )

    return render_template("predict.html")

# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )