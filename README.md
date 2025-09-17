# Student Dropout Prediction App

A machine learning web application to predict student dropout risk using demographic, academic, and engagement features.

## 🚀 Features
- Data preprocessing and model training (scikit-learn)
- Flask backend serving predictions
- Simple frontend (HTML, CSS, JS) for user input
- Pre-trained model included (via Git LFS)

## 📂 Project Structure
student_dropout_app/
│── backend/
│ ├── app.py
│ ├── dropout_model.pkl
│ ├── scaler.pkl
│ └── label_encoder.pkl
│── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│── requirements.txt
│── README.md
│── .gitignore



## ⚙️ Installation
1. Clone repo:
   ```bash
   git clone https://github.com/ParthCode01/Student-DropOut-Prediction-Model-.git
   cd Student-DropOut-Prediction-Model-

**Create virtual environment:**

python -m venv venv
venv\Scripts\activate  # Windows


Install dependencies:

pip install -r requirements.txt

**Usage**

Run Flask backend:

python backend/app.py


Open frontend/index.html in browser.

**Data & Privacy**

No raw student data is included in this repo.

Model trained on anonymized/cleaned dataset.

Users can replace data/ with their own CSV files to train or test the model.

**Requirements**

Python libraries used:

pandas

numpy

scikit-learn

Flask

joblib

Install all dependencies using:

# pip install -r requirements.txt


**Future Improvements**

Deploy as a web app (Heroku, Streamlit, or Flask server)

Add user authentication and logging

Incorporate more features for higher prediction accuracy

Add visual analytics/dashboard for student engagement

**Author / Contact**

Parth Sharma

GitHub: ParthCode01

Email: parthcsework@gmail.com

**License**

MIT License

