import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the Model
model = joblib.load("Stock-Market-Prediction/public/Stock_market_prediction.pkl")

# Custom CSS for sleek design
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #4B8BBE;
        font-family: 'Helvetica', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
    }
    label {
        font-family: 'Arial', sans-serif;
        color: #2E2E2E;
    }
    .css-1cpxqw2 {
        margin-top: -20px;
    }
    .stButton button {
        background-color: #4B8BBE;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #357ABD;
        cursor: pointer;g
    }
    .css-145kmo2 {
        font-size: 1rem;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .alert-high-risk {
        background-color: #ff4d4d;
        color: white;
        padding: 10px;
        border-radius: 10px;
    }
    .alert-medium-risk {
        background-color: #ffcc00;
        color: black;
        padding: 10px;
        border-radius: 10px;
    }
    .alert-low-risk {
        background-color: #66cc66;
        color: white;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app with an icon
st.markdown("<h1>📈 Stock Market Predictor</h1>", unsafe_allow_html=True)

# Input Fields arranged in a grid layout
col1, col2 = st.columns(2)
with col1:
    op = st.number_input("Open Price :")
    high = st.number_input("High Price :")
with col2:
    low = st.number_input("Low Price :")
    volume = st.number_input("Volume :")

# Dataframe
input_data = pd.DataFrame({
    'Open': [op],
    'High': [high],
    'Low': [low],
    'Volume': [volume]
})

# Prediction
if st.button("Predict"):
    stock_prediction = model.predict(input_data)
    st.write(f"### Predicted Price: ${stock_prediction[0]:,.2f}")

    # Define Risk Levels based on prediction
    risk_threshold_high = 1000  # Define a threshold for high risk
    risk_threshold_low = 5000   # Define a threshold for low risk

    # Risk alert logic with custom styles
    if stock_prediction < risk_threshold_high:
        st.markdown('<div class="alert-high-risk">⚠️ High Risk: The predicted price is quite low.</div>', unsafe_allow_html=True)
    elif stock_prediction > risk_threshold_low:
        st.markdown('<div class="alert-low-risk">✅ Low Risk: The predicted price is in a safe range.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="alert-medium-risk">⚠️ Medium Risk: The predicted price is in an uncertain range.</div>', unsafe_allow_html=True)
