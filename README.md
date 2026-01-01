# Customer Churn Prediction System

## Overview
This project predicts whether a customer is likely to churn using machine learning.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Streamlit

## Workflow
1. Data cleaning and EDA
2. Feature engineering
3. Model training and evaluation
4. Model saving
5. FastAPI deployment
6. Streamlit UI

## Model
- Logistic Regression
- Selected based on higher recall for churn prediction

## How to Run
1. Train and save model
2. Start API:
uvicorn api.main:app --reload
3. Start UI:
streamlit run app.py


## Result
The system predicts churn and provides churn probability.
