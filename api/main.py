from fastapi import FastAPI
from src.predict import predict_churn

app = FastAPI(title="Customer Churn Prediction API")
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}
@app.post("/predict")
def predict(data: dict):
    result = predict_churn(data)
    return result
