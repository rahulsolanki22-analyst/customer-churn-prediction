# Deployment Guide for Customer Churn Prediction

This guide covers multiple deployment options for your Customer Churn Prediction application.

## Project Architecture

- **Backend API**: FastAPI (`api/main.py`) - Runs on port 8000
- **Frontend**: Streamlit (`app.py`) - Runs on port 8501
- **Model**: Saved scikit-learn model (`model/churn_model.pkl`)

---

## Option 1: Streamlit Cloud (Easiest - Recommended for Quick Demo)

**Best for**: Quick demos, personal projects, free hosting

### Steps:

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Update app.py to use environment variable for API URL**
   - The current app.py uses `http://127.0.0.1:8000` which won't work in production
   - You'll need to either:
     - Deploy the API separately and update the URL
     - Or combine both into a single Streamlit app (see Option 1b)

3. **Go to [streamlit.io/cloud](https://streamlit.io/cloud)**
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

**Note**: Streamlit Cloud only hosts Streamlit apps. You'll need to deploy the FastAPI backend separately (see other options).

---

## Option 2: Render (Free Tier Available)

**Best for**: Free hosting with both API and frontend

### Steps:

1. **Create two services on Render**:

   **Service 1: FastAPI Backend**
   - Go to [render.com](https://render.com)
   - Create new "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name**: churn-api
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
     - **Environment Variables**: None needed initially

   **Service 2: Streamlit Frontend**
   - Create another "Web Service"
   - Settings:
     - **Name**: churn-app
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
     - **Environment Variables**: 
       - `API_URL`: `https://churn-api.onrender.com` (your API service URL)

2. **Update app.py** to use environment variable:
   ```python
   import os
   API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
   # Then use API_URL instead of hardcoded URL
   ```

3. **Create render.yaml** (optional, for infrastructure as code):
   ```yaml
   services:
     - type: web
       name: churn-api
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: uvicorn api.main:app --host 0.0.0.0 --port $PORT
     
     - type: web
       name: churn-app
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
       envVars:
         - key: API_URL
           fromService:
             name: churn-api
             type: web
             property: host
   ```

---

## Option 3: Railway (Simple & Modern)

**Best for**: Easy deployment, good free tier

### Steps:

1. **Install Railway CLI** (optional):
   ```bash
   npm i -g @railway/cli
   railway login
   ```

2. **Deploy via Railway Dashboard**:
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

3. **Create railway.json**:
   ```json
   {
     "$schema": "https://railway.app/railway.schema.json",
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "uvicorn api.main:app --host 0.0.0.0 --port $PORT",
       "restartPolicyType": "ON_FAILURE",
       "restartPolicyMaxRetries": 10
     }
   }
   ```

4. **For Streamlit**, create a separate service or use the same approach.

---

## Option 4: Docker Deployment (Any Platform)

**Best for**: Consistent deployment across platforms, production-ready

### Local Testing:

```bash
# Build the image
docker build -t churn-prediction .

# Run with docker-compose
docker-compose up

# Or run manually
docker run -p 8000:8000 -p 8501:8501 churn-prediction
```

### Deploy Docker to:

- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **DigitalOcean App Platform**
- **Fly.io**

### Example: Google Cloud Run

```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/PROJECT-ID/churn-prediction

# Deploy to Cloud Run
gcloud run deploy churn-prediction \
  --image gcr.io/PROJECT-ID/churn-prediction \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Option 5: AWS/GCP/Azure (Enterprise)

### AWS:
- **Elastic Beanstalk**: Easiest AWS option
- **ECS/Fargate**: Container-based
- **EC2**: Full control, more setup

### Google Cloud:
- **Cloud Run**: Serverless containers (recommended)
- **App Engine**: Managed platform
- **Compute Engine**: VMs

### Azure:
- **App Service**: Managed platform
- **Container Instances**: Serverless containers
- **Virtual Machines**: Full control

---

## Important Considerations

### 1. Update app.py for Production

The current `app.py` hardcodes the API URL. Update it:

```python
import os
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

# In the requests.post call:
response = requests.post(f"{API_URL}/predict", json=payload)
```

### 2. Model File Size

- Ensure `model/churn_model.pkl` is committed to Git (if < 100MB)
- For larger models, use cloud storage (S3, GCS, Azure Blob) and load at runtime

### 3. Environment Variables

Create a `.env` file for local development:
```
API_URL=http://127.0.0.1:8000
```

### 4. Security

- Add CORS middleware to FastAPI if needed
- Use environment variables for sensitive data
- Consider adding authentication for production

### 5. Monitoring

- Add logging
- Set up health checks
- Monitor API response times

---

## Quick Start: Recommended Path

1. **For quick demo**: Use Streamlit Cloud (but deploy API separately on Render)
2. **For production**: Use Docker + Cloud Run / Railway / Render
3. **For enterprise**: Use AWS/GCP/Azure with proper CI/CD

---

## Testing Locally

```bash
# Terminal 1: Start FastAPI
cd api
uvicorn main:app --reload

# Terminal 2: Start Streamlit
streamlit run app.py
```

Then visit:
- Streamlit: http://localhost:8501
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## Need Help?

- Check platform-specific documentation
- Ensure all dependencies are in `requirements.txt`
- Verify model file path is correct
- Check logs for deployment errors
