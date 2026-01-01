import joblib
import pandas as pd

MODEL_PATH = "model/churn_model.pkl"

def predict_churn(input_data: dict):
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 3)
    }
