# Diabetes-Prediction-System
Overview

The Diabetes Prediction System is a machine learning-powered tool built using Django that predicts the likelihood of diabetes based on user-provided health metrics. This project demonstrates the integration of a Logistic Regression model into a web-based interface, providing real-time predictions in a user-friendly manner.

Features
User-Friendly Interface: Simple and intuitive web forms for inputting health metrics.
Real-Time Predictions: Uses a trained Logistic Regression model to instantly classify diabetes risk.
Scalable Design: Modular Django framework supports easy updates and scalability.
Dataset Integration: Leverages a publicly available diabetes dataset to train the model.

Technologies Used
Backend Framework: Django
Programming Language: Python
Machine Learning:
Logistic Regression using scikit-learn
Dataset handling with pandas

Visualization:
matplotlib and seaborn for exploratory data analysis
Frontend: HTML templates with Django template engine

How It Works

Input:
The user enters various health metrics, such as glucose level, BMI, blood pressure, etc., through an interactive form.

Model Processing:
The application uses a Logistic Regression model trained on the diabetes.csv dataset.

Prediction:
The model processes the input and predicts whether the user is at risk of diabetes (Positive) or not (Negative).

Output:
The prediction result is displayed on the web page
