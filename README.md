# 🧠 Sentiment Analysis Web App

This is an end-to-end Sentiment Analysis project that classifies user input as **Positive** or **Negative** using a Recurrent Neural Network (RNN) built with TensorFlow/Keras. The model is deployed with a user-friendly web interface using **Streamlit**.

---

## 🚀 Demo

Enter any sentence in the app, and it predicts the sentiment:

> “I love this movie!” → ✅ Positive  
> “This is the worst app ever.” → ❌ Negative

---

## 📁 Project Structure

```
Sentiment Analysis Project/
├── app.py                   # Streamlit web app
├── sentiment_model.py       # Helper functions for prediction
├── sentiment_model.h5       # Trained Keras RNN model
├── tokenizer.pkl            # Tokenizer used during training
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Features

- Trained on custom labeled IMDB Sentiment Analysis Data
- Text preprocessing (tokenization, padding)
- Deep learning (Embedding + RNN)
- Real-time predictions via Streamlit UI
- Deployable on Streamlit Cloud

---

## 🧪 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push the entire project to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub account.
3. Select the repository and deploy.

---

## 📦 Requirements

```
tensorflow
numpy
streamlit
```

## 📚 Acknowledgements

- TensorFlow / Keras for model building
- Streamlit for the web UI
- IMDb for labeled dataset

---
## ✨ Author

**Hariom Nagar**  
Student at IIIT Ranchi | AI/ML Enthusiast  
Connect on [LinkedIn](https://www.linkedin.com/in/hari-om-nagar/)
