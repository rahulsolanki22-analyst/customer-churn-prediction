#!/bin/bash

# Script to start both FastAPI and Streamlit locally

echo "Starting Customer Churn Prediction Application..."
echo ""

# Start FastAPI in background
echo "Starting FastAPI backend on http://127.0.0.1:8000"
uvicorn api.main:app --reload --port 8000 &
API_PID=$!

# Wait a moment for API to start
sleep 2

# Start Streamlit
echo "Starting Streamlit frontend on http://127.0.0.1:8501"
streamlit run app.py

# When Streamlit exits, kill the API process
kill $API_PID
