import streamlit as st
import pandas as pd
import joblib

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="💰",
    layout="centered"
)

# ==========================
# Load Model
# ==========================

model = joblib.load("insurance_model.pkl")
columns = joblib.load("columns.pkl")
model_name = joblib.load("model_name.pkl")

# ==========================
# Sidebar
# ==========================

st.sidebar.title("About")

st.sidebar.info("""
This application predicts the medical insurance cost
using Machine Learning.

Dataset Features:
- Age
- BMI
- Children
- Sex
- Smoking Status
- Region
""")

st.sidebar.success(f"Model Used:\n\n**{model_name}**")

# ==========================
# Title
# ==========================

st.title(" Medical Insurance Cost Prediction")

st.write(
    "Enter the customer's information to estimate the expected medical insurance cost."
)

# ==========================
# Inputs
# ==========================

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    children = st.number_input(
        "Children",
        min_value=0,
        max_value=10,
        value=0
    )

with col2:

    sex = st.selectbox(
        "Sex",
        ["female", "male"]
    )

    smoker = st.selectbox(
        "Smoker",
        ["no", "yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]
    )

# ==========================
# Prediction
# ==========================

if st.button("Predict Insurance Cost"):

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

    prediction = model.predict(input_df)[0]

    # ==========================
    # Show Input
    # ==========================

    st.subheader("Entered Information")

    st.dataframe(input_df)

    # ==========================
    # Model Used
    # ==========================

    st.info(f"Using Model: {model_name}")

    # ==========================
    # Prediction
    # ==========================

    st.metric(
        label="Estimated Insurance Cost",
        value=f"${prediction:,.2f}"
    )

    # ==========================
    # Cost Category
    # ==========================

    if prediction < 10000:
        st.success(" Low Insurance Cost")

    elif prediction < 25000:
        st.warning(" Medium Insurance Cost")

    else:
        st.error(" High Insurance Cost")

# ==========================
# Footer
# ==========================

st.markdown("---")

st.caption("Developed by Alzahraa Gamal")