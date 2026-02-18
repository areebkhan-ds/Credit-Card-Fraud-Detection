import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/rf_fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details:")

# User inputs
amt = st.number_input("Transaction Amount", min_value=0.0)
lat = st.number_input("Customer Latitude")
long = st.number_input("Customer Longitude")
city_pop = st.number_input("City Population", min_value=0)
unix_time = st.number_input("Transaction Unix Time", min_value=0)
merch_lat = st.number_input("Merchant Latitude")
merch_long = st.number_input("Merchant Longitude")

if st.button("Predict Fraud"):
    input_data = pd.DataFrame([[amt, lat, long, city_pop, unix_time, merch_lat, merch_long]],
                              columns=["amt", "lat", "long", "city_pop",
                                       "unix_time", "merch_lat", "merch_long"])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Safe")
