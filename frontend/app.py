import streamlit as st
import requests

st.title("🤖 AI Sentiment Analyzer")

st.write("Enter some text and let the AI analyze its sentiment.")

text = st.text_area(
    "Enter your text:",
    placeholder="Example: I really love this application!"
)

if st.button("Analyze Sentiment"):
    if text.strip():
        response = requests.post(
            "http://backend:8000/predict",
            json={"text": text}
        )

        if response.status_code == 200:
            result = response.json()

            st.success(f"Sentiment: {result['sentiment']}")
            st.write(f"Confidence: {result['confidence']}")
        else:
            st.error("Something went wrong with the API.")
    else:
        st.warning("Please enter some text.")