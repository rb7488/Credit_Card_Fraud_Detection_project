import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained model and scaler
# -----------------------------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Fraud Detection")
st.write(
    "Machine Learning model for detecting potentially fraudulent "
    "credit card transactions."
)

st.divider()

# -----------------------------
# Input fields
# -----------------------------
st.subheader("Transaction Details")

col1, col2 = st.columns(2)

with col1:
    time = st.number_input(
        "Time",
        value=0.0,
        help="Seconds elapsed between this transaction and the first transaction."
    )

with col2:
    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )

st.subheader("Transaction Features")

# V1 to V28
features = {}

cols = st.columns(4)

for i in range(1, 29):
    with cols[(i - 1) % 4]:
        features[f"V{i}"] = st.number_input(
            f"V{i}",
            value=0.0,
            format="%.6f"
        )

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Detect Fraud", type="primary"):

    # Create dataframe in EXACT training order
    input_data = pd.DataFrame([{
        "Time": time,
        **{f"V{i}": features[f"V{i}"] for i in range(1, 29)},
        "Amount": amount
    }])

    # Scale Time and Amount exactly as during training
    input_data[["Time", "Amount"]] = scaler.transform(
        input_data[["Time", "Amount"]]
    )

    # Prediction
    prediction = model.predict(input_data)[0]

    st.divider()

    if prediction == 1:
        st.error(
            "🚨 FRAUDULENT TRANSACTION DETECTED"
        )
    else:
        st.success(
            "✅ TRANSACTION APPEARS LEGITIMATE"
        )

    st.caption(
        "Prediction generated using Random Forest trained with SMOTE."
    )
