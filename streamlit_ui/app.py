import streamlit as st
from PIL import Image

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Inflation Forecast Dashboard",
    page_icon="📈",
    layout="centered",
)

# ---------- HEADER ----------
st.title("📊 US Inflation Forecasting Dashboard")
st.markdown("Compare different time series models to forecast US inflation.")

st.markdown("""
### 🔍 Project Overview
This dashboard visualizes the inflation forecast results using four different machine learning and statistical models:


You can select a model from the sidebar to view its forecast plot.
""")

# ---------- SIDEBAR ----------
st.sidebar.header("Select a Forecasting Model")
model_choice = st.sidebar.radio(
    "Choose a model to display:",
    ('XGBoost', 'LSTM', 'ARIMA', 'Prophet'),
    index=0  # XGBoost selected by default
)

# ---------- IMAGE PATHS ----------
image_paths = {
    "XGBoost": "./images/inflation_forecast_XGB_2025.png",
    "LSTM": "images/inflation_forecast_LSTM_2025.png",
    "ARIMA": "images/inflation_forecast_ARIMA_2025.png",
    "Prophet": "images/inflation_forecast_Prophet_2025.png"
}

# ---------- DISPLAY IMAGE ----------
st.markdown(f"### 📌 Forecast Plot: **{model_choice} Model**")

try:
    image = Image.open(image_paths[model_choice])
    st.image(image, caption=f"{model_choice} Forecast Result", use_container_width=True)
except FileNotFoundError:
    st.warning(f"Image for {model_choice} model not found. Please check the path.")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("✅ Built with Streamlit | 🔗 Forecasts based on historical US inflation data")

