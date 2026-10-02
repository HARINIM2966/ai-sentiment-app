from fastapi import FastAPI
from pydantic import BaseModel

from backend.model import analyze_sentiment


app = FastAPI(
    title="AI Sentiment Analyzer API",
    description="AI-powered sentiment analysis API"
)


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "AI Sentiment Analyzer API is running!"
    }


@app.post("/predict")
def predict(request: TextRequest):

    result = analyze_sentiment(request.text)

    return {
        "text": request.text,
        "sentiment": result["label"],
        "confidence": result["score"]
    }