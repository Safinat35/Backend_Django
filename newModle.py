import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi import FastAPI
import os
import json

# تحميل المودل والتوكنايزر مرة واحدة عند بدء الخادم
MODEL_PATH = "C:\Users\safna\fsp\backend\phishing_model"
MODEL_NAME = "google/electra-small-discriminator"

# تحميل المودل فقط عند بدء الخادم
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# التحقق من إذا كان الجهاز يدعم الـ GPU أو لا
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

app = FastAPI()

# دالة التنبؤ
def predict(urls):
    encodings = tokenizer(urls, padding=True, truncation=True, max_length=128, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**encodings).logits
    preds = torch.argmax(logits, axis=-1)
    return preds.cpu().numpy()

@app.post("/predict")
async def predict_urls(urls: list):
    predictions = predict(urls)
    return {"predictions": predictions.tolist()}