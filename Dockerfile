# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Create a startup script
RUN echo '#!/bin/bash\n\
# Start FastAPI in background\n\
uvicorn api.main:app --host 0.0.0.0 --port 8000 &\n\
# Start Streamlit in foreground\n\
streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true\n\
' > start.sh && chmod +x start.sh

# Run the startup script
CMD ["./start.sh"]
