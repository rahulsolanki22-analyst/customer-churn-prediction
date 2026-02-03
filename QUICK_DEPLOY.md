# Quick Deployment Guide

## 🚀 Fastest Deployment Options

### Option 1: Render (Recommended - Free Tier)
**Time**: ~10 minutes | **Cost**: Free

1. Push code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Create **two services**:

   **Service 1 - API:**
   - New Web Service → Connect GitHub repo
   - Name: `churn-api`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`

   **Service 2 - Frontend:**
   - New Web Service → Same repo
   - Name: `churn-app`
   - Build: `pip install -r requirements.txt`
   - Start: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
   - Environment Variable: `API_URL` = `https://churn-api.onrender.com`

4. Wait for deployment (~5 min)
5. Done! Your app is live 🎉

---

### Option 2: Railway (Simple)
**Time**: ~5 minutes | **Cost**: Free tier available

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Select your repo
5. Railway auto-detects Python and deploys
6. Add environment variable `API_URL` if deploying frontend separately

---

### Option 3: Docker + Any Platform
**Time**: ~15 minutes | **Cost**: Varies

```bash
# Build
docker build -t churn-prediction .

# Run locally
docker-compose up

# Deploy to:
# - Google Cloud Run (free tier)
# - AWS ECS/Fargate
# - Azure Container Instances
# - DigitalOcean
```

---

## 📋 Pre-Deployment Checklist

- [x] ✅ `requirements.txt` is complete
- [x] ✅ `app.py` uses `API_URL` environment variable
- [x] ✅ FastAPI has CORS enabled
- [x] ✅ Model file (`model/churn_model.pkl`) is in repository
- [ ] Push code to GitHub
- [ ] Choose deployment platform
- [ ] Set environment variables
- [ ] Test deployed application

---

## 🔧 Local Testing

Before deploying, test locally:

**Windows:**
```bash
start_local.bat
```

**Linux/Mac:**
```bash
chmod +x start_local.sh
./start_local.sh
```

**Manual:**
```bash
# Terminal 1
uvicorn api.main:app --reload

# Terminal 2
streamlit run app.py
```

Visit:
- Frontend: http://localhost:8501
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 📚 Full Documentation

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on all platforms.

---

## 🆘 Common Issues

**Issue**: API connection error in Streamlit
- **Fix**: Set `API_URL` environment variable to your deployed API URL

**Issue**: Model file not found
- **Fix**: Ensure `model/churn_model.pkl` is committed to Git

**Issue**: Build fails on platform
- **Fix**: Check `requirements.txt` has all dependencies

**Issue**: CORS errors
- **Fix**: Already fixed! CORS is enabled in `api/main.py`

---

## 💡 Pro Tips

1. **Start with Render** - Easiest free option
2. **Use separate services** - Deploy API and frontend separately for better scaling
3. **Monitor logs** - Check platform logs if something breaks
4. **Test locally first** - Always test before deploying
5. **Use environment variables** - Never hardcode URLs or secrets
