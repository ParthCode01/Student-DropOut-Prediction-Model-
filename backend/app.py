from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- import CORS here
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)
CORS(app)  # <-- enable CORS for all routes

# Load model, scaler, and label encoder
model = joblib.load("dropout_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

# Prediction route
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
    app.run(debug=True)
