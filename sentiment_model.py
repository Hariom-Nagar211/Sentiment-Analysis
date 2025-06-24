# sentiment_model.py

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load tokenizer (saved after training)
import pickle
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load model
model = load_model('sentiment_model.h5')

# Prediction function
def predict_sentiment(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=100)  # Adjust maxlen to match training
    prediction = model.predict(padded)[0][0]
    return "Positive" if prediction > 0.5 else "Negative"
