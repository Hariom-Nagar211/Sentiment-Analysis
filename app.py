# app.py

import streamlit as st
from sentiment_model import predict_sentiment

st.set_page_config(page_title="Sentiment Classifier", layout="centered")

st.title("🧠 Sentiment Analysis")
st.write("Enter a sentence to classify its sentiment:")

user_input = st.text_area("Your Text:", "")

if st.button("Predict"):
    if user_input.strip():
        result = predict_sentiment(user_input)
        
        if result == "Positive":
            st.success(f"✅ Sentiment: {result}")
        else:
            st.error(f"❌ Sentiment: {result}")
    else:
        st.warning("⚠️ Please enter some text.")
