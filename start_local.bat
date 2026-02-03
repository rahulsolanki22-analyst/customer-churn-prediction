@echo off
REM Script to start both FastAPI and Streamlit locally on Windows

echo Starting Customer Churn Prediction Application...
echo.

REM Start FastAPI in a new window
echo Starting FastAPI backend on http://127.0.0.1:8000
start "FastAPI Backend" cmd /k "uvicorn api.main:app --reload --port 8000"

REM Wait a moment for API to start
timeout /t 2 /nobreak >nul

REM Start Streamlit
echo Starting Streamlit frontend on http://127.0.0.1:8501
streamlit run app.py
