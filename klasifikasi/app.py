from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from keras.models import load_model
import numpy as np
from PIL import Image
import io
import os

# from tensorflow.keras.models import load_model
# from tensorflow.keras.utils import CustomObjectScope
# from tensorflow.keras.layers import DepthwiseConv2D

# # Tentukan kelas yang tidak dikenali
# with CustomObjectScope({'DepthwiseConv2D': DepthwiseConv2D}):
#     model = load_model('keras_model.h5')

from tensorflow.keras import layers

class CustomDepthwiseConv2D(layers.DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        if 'groups' in kwargs:
            kwargs.pop('groups')  # Hapus argumen groups jika ada
        super().__init__(*args, **kwargs)

    def call(self, inputs):
        # Implementasi custom untuk menangani 'groups' jika diperlukan
        return super().call(inputs)

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import CustomObjectScope

# Definisikan custom layer di dalam CustomObjectScope
with CustomObjectScope({
    'DepthwiseConv2D': CustomDepthwiseConv2D
}):
    model = load_model('keras_model.h5')

app = Flask(__name__)

# Load the model
# model = tf.keras.models.load_model('keras_model.h5')

# Load class labels from label.txt
def load_class_labels(label_file):
    try:
        with open(label_file, 'r') as f:
            labels = f.read().splitlines()
        return labels
    except Exception as e:
        print(f"Error loading labels: {e}")
        return []

class_labels = load_class_labels('labels.txt')  # Ganti dengan path yang sesuai jika perlu

# Preprocessing function
def preprocess_image(image, target_size):
    """
    Function to preprocess the uploaded image to match the model's input format.
    """
    image = image.resize(target_size)  # Resize ke ukuran model
    image = np.array(image) / 255.0   # Normalisasi (0-1)
    image = np.expand_dims(image, axis=0)  # Tambahkan batch dimension
    return image

# @app.route("/", methods=["GET"])
# def home():
#     """
#     Home route to render a simple webpage for image upload.
#     """
#     return render_template("index.html")

@app.route("/classify", methods=["POST"])
def predict():
    """
    Route to handle predictions.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"})

    try:
        # Baca gambar dari file upload
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        processed_image = preprocess_image(image, target_size=(224, 224))  # Sesuaikan dengan input model

        # Pastikan model ada dan siap digunakan
        if model is None:
            return jsonify({"error": "Model not loaded"})

        # Prediksi
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions[0])

        if predicted_class < len(class_labels):
            result = class_labels[predicted_class]
        else:
            result = "Unknown Class"

        return jsonify({"prediction": result, "confidence": float(np.max(predictions))})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
