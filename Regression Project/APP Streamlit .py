import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("insurance_model.pkl")
columns = joblib.load("columns.pkl")

st.title("Medical Insurance Cost Prediction")

st.write("Enter the customer's information")

# Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input("Children", min_value=0, max_value=10, value=0)

sex = st.selectbox("Sex", ["female", "male"])

smoker = st.selectbox("Smoker", ["no", "yes"])

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# Prediction
if st.button("Predict"):

    data = {
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex_male": sex == "male",
        "smoker_yes": smoker == "yes",
        "region_northwest": region == "northwest",
        "region_southeast": region == "southeast",
        "region_southwest": region == "southwest"
    }

    input_df = pd.DataFrame([data])

    input_df = input_df[columns]

    prediction = model.predict(input_df)

    st.success(f"Predicted Insurance Charge: ${prediction[0]:,.2f}")