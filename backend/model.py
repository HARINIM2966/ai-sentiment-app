from transformers import pipeline

# Load the AI sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")


def analyze_sentiment(text: str):
    result = sentiment_pipeline(text)[0]

    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }