# VaakSetu – Intelligent Healthcare Triage System

## Overview
VaakSetu is my **major project (2026)**, a multimodal AI system for early medical triage.  
It builds on my earlier mini project **Medora.AI**, but goes deeper with **Convolutional Neural Networks (CNNs)**, **AI agents**, and **multimodal inputs (voice + image)**.

⚠️ Disclaimer: This is a research project, not medical advice.

---

## Tech Stack
- **AI/ML/DL**
  - PyTorch + Hugging Face (MedGemma/Gemma fine-tuning)
  - CNNs for medical image classification (skin lesions, chest X-rays)
  - Whisper (speech-to-text for voice input)
- **Backend**
  - FastAPI (REST API)
  - LangChain + n8n (agent workflows)
- **Frontend**
  - Next.js (React framework)
  - Tailwind CSS (UI styling)
- **Database**
  - MongoDB Atlas (free tier)
- **Deployment**
  - Docker (containerization)
  - Hugging Face Spaces / Render (free hosting)

---
## ui interface :
<img width="345" height="790" alt="Screenshot 2026-03-29 182449" src="https://github.com/user-attachments/assets/6491f829-c203-4bd3-920a-30db85da1b50" />    <img width="345" height="790" alt="Screenshot 2026-03-29 182514" src="https://github.com/user-attachments/assets/7da8a190-07d1-4008-ab3a-3ca1153e2bb3" />




## Dataset
- **HAM10000** – Skin lesion dataset (dermatology)
- **ISIC** – International Skin Imaging Collaboration dataset
- **NIH Chest X-ray** – Radiology dataset

All datasets are open-source and available on Kaggle/Hugging Face.

---

## Architecture
1. **Data Input**: User uploads image or speaks via voice.
2. **AI Model**: Fine-tuned MedGemma CNN processes medical images.
3. **Agent Layer**: LangChain agent + n8n workflow routes output (triage, nearest clinic).
4. **Backend**: FastAPI serves predictions securely.
5. **Frontend**: Next.js PWA displays results.
6. **Deployment**: Docker container → Hugging Face Spaces.

---

## Deployment (Docker)

**Dockerfile**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Run locally**
```bash
docker build -t vaaksetu-backend .
docker run -p 8000:8000 vaaksetu-backend
```

---

## Impact
- **For users**: Simple triage suggestions, SOS alerts, nearest clinic info.
- **For doctors**: Reduced load, early detection.
- **For society**: Scalable healthcare support in rural India.

---

## Disclaimer
This project is for **research and educational purposes only**.  
It is **not a substitute for professional medical advice**.
```
