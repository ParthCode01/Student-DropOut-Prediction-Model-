from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load model, scaler, encoder
model = joblib.load("dropout_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

# Serve frontend
@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    admission = data["admission_grade"]
    semester = data["semester_grade"]
    attendance = data["attendance"]

    X = np.array([[admission, semester, attendance]])
    X_scaled = scaler.transform(X)
    y_pred = model.predict(X_scaled)
    y_pred_label = le.inverse_transform(y_pred)[0]

    return jsonify({"prediction": y_pred_label})

if __name__ == "__main__":
    # Use debug=False for stability
    app.run(debug=False)
