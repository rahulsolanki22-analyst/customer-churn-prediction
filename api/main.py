from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.predict import predict_churn

app = FastAPI(title="Customer Churn Prediction API")

# Add CORS middleware to allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: dict):
    result = predict_churn(data)
    return result
