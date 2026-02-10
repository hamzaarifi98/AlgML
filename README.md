# Algerian Forest Fires Prediction (Flask + Ridge Regression)

A simple end-to-end Machine Learning project that predicts **fire weather index / fire risk-related target** from the Algerian Forest Fires dataset using a **Ridge Regression** model.  
It includes:
- Data + training notebooks
- Saved model artifacts (`ridge.pkl`, `scaler.pkl`)
- A **Flask web app** with an HTML form for predictions
- AWS Elastic Beanstalk configuration (`.ebextensions/python.config`)



## Project Overview

This project uses the **Algerian Forest Fires** dataset to train a regression model and deploy it as a web application.

**Model**
- Algorithm: **Ridge Regression**
- Preprocessing: **StandardScaler**
- Artifacts saved as pickle files and loaded by the Flask app:
  - `models/ridge.pkl`
  - `models/scaler.pkl`

**Web App**
- `GET /` → landing page
- `GET|POST /predict` → prediction form + result rendering

How It Works (App Flow)
1. User opens /
2. User goes to prediction form
3. On submit (POST /predict):
4. values are read from the HTML form
5. input is scaled using models/scaler.pkl
6. prediction is produced using models/ridge.pkl
7. Result is rendered in templates/home.html




