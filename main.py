import streamlit as st
import numpy as np
import joblib

with open("house_price_predictor_lr.pkl", "rb") as f:
    model = joblib.load(f)

with open("columns.txt", "r") as f:
    data_columns = f.read().splitlines()

locations = data_columns[3:]

st.title("Bengaluru House Price Prediction")

bhk = st.number_input("BHK", min_value=1, max_value=20, value=2)
area = st.number_input("Total area (sqft)", min_value=300, value=1000)
bath = st.number_input("Number of bathrooms", min_value=1, max_value=20, value=2)

location = st.selectbox("Select location", locations)

if st.button("Predict", type="primary"):

    x = np.zeros(len(data_columns)-1)
    x[0] = area
    x[1] = bath
    x[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    price = model.predict([x])[0]
    st.success(f"Estimated Price: ₹ {price:,.2f} Lakhs")
