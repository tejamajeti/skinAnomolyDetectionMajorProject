import os
import uuid
import logging
from typing import Tuple, List, Dict
from urllib.parse import urlparse
from urllib.request import urlopen
from PIL import Image
from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from keras.models import load_model
from keras.utils import load_img, img_to_array
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow all origins
app.secret_key = os.urandom(24)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'skin_disease_model_ISIC_densenet.h5')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'jfif'}
IMAGE_UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'images')

# Ensure upload folder exists
os.makedirs(IMAGE_UPLOAD_FOLDER, exist_ok=True)

# Load model
try:
    model = load_model(MODEL_PATH)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    raise RuntimeError("Model failed to load")


def allowed_file(filename: str) -> bool:
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_valid_url(url: str) -> bool:
    """Validate URL format."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

classes = [
    'Actinic keratosis',
    'Atopic Dermatitis',
    'Benign keratosis',
    'Dermatofibroma',
    'Melanocytic nevus',
    'Melanoma',
    'Squamous cell carcinoma',
    'Tinea Ringworm Candidiasis',
    'Vascular lesion'
]

def predict(filename: str, model) -> Dict:
    """Predict skin disease from an image."""
    try:
        logger.info(f"Loading image: {filename}")  # Debugging log
        img = load_img(filename, target_size=(240, 240))
        img = img_to_array(img)
        img = img.reshape(1, 240, 240, 3)
        img = img.astype('float32') / 255.0

        logger.info(f"Running model prediction...")  # Debugging log
        result = model.predict(img)[0]
        
        sorted_indices = result.argsort()[-1]
        predictions = {
            f"class{1}": classes[sorted_indices]        }
        probabilities = {
            f"prob{1}": round(float(result[sorted_indices] * 100), 2) 
        }

        logger.info(f"Prediction result: {predictions}, {probabilities}")  # Debugging log
        return {**predictions, **probabilities}

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")  # Debugging log
        raise


@app.route('/')
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict_image():
    """Handle image prediction requests."""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Allowed: jpg, jpeg, png"}), 400
        
        filename = f"{uuid.uuid4()}.{file.filename.rsplit('.', 1)[1].lower()}"
        img_path = os.path.join(IMAGE_UPLOAD_FOLDER, filename)
        file.save(img_path)

        logger.info(f"Image saved at: {img_path}")  # Debugging log

        # Make prediction
        predictions = predict(img_path, model)
        logger.info(f"Predictions: {predictions}")  # Debugging log

        predictions["image_url"] = f"/static/images/{filename}"
        return jsonify(predictions)

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")  # Debugging log
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
