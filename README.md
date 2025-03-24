# 🩺 Skin Disease Predictor


### A Flask + React application that predicts skin diseases from uploaded images using a Deep Learning model.

## 📌 Features
  ✅ Upload an image (JPG, JPEG, PNG) <br/>
  ✅ AI-based prediction of skin diseases <br/>
  ✅ Top 4 conditions with probability scores <br/>
  ✅ Simple, user-friendly UI

## 📂 Project Structure
```
📦 Skin-Disease-Predictor
├── 📁 backend (Flask Server)
│   ├── app.py # Flask API for prediction
│   ├── skin_disease_model_ISIC_densenet.h5 # Trained deep learning model
│   ├── requirements.txt # Python dependencies
│   ├── 📁 static/images/ # Uploaded images storage
│   ├── 📁 templates/ # HTML templates (if used)
│   └── ...
├── 📁 frontend (React App)
│   ├── src/App.js # Main React file
│   ├── src/index.js # React entry point
│   ├── 📁 public/ # Static files
│   ├── package.json # React dependencies
└── ...
```
## 🚀 Setup Guide
### 1️⃣ Install Dependencies
   #### 📌 Backend (Flask)
    pip install -r requirements.txt
#### 📌 Frontend (React)
    npm install
### 2️⃣ Start the Flask Server
    python app.py
<P> Runs on: http://localhost:4000/ <br/>
Endpoints:
POST /predict → Uploads image and gets prediction</P>

### 3️⃣ Start the React App
    npm start
<p> Runs on: http://localhost:3000/ <br/>
Interacts with Flask API for predictions </p>

## 🛠 API Usage
  🔹 Endpoint: POST /predict <br/>
#### Request:
Content-Type: multipart/form-data <br/>
Body:
file: Upload an image (JPG, PNG)<br/>
Response:
json Copy Edit
{
  "class1": "Benign keratosis",
  "prob1": 91.05,
  "class2": "Atopic Dermatitis",
  "prob2": 1.88,
  "class3": "Vascular lesion",
  "prob3": 1.76,
  "class4": "Melanocytic nevus",
  "prob4": 1.62,
  "image_url": "/static/images/filename.jpg"
}


## 📌 Tech Stack
  🔹 Backend: Flask, TensorFlow/Keras<br/>
  🔹  Frontend: React, Axios <br/>
  🔹  Model: DenseNet-based Skin Disease Classification

## 🎯 Future Improvements
   ✅ Deploy using Docker <br/>
   ✅  add more skin disease categories
   <br>
   ✅ Improve model accuracy
   
