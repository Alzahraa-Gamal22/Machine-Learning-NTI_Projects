# 💰 Loan Approval Prediction

A Machine Learning project that predicts whether a loan application will be **Approved** or **Rejected** using different classification algorithms.

## 📌 Project Overview

This project compares multiple machine learning models for loan approval prediction and automatically saves the best-performing model for deployment in a Streamlit web application.

## 📂 Dataset

The dataset contains applicant information including:

- Number of Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Asset Value

Target:

- Loan Status (Approved / Rejected)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Streamlit
- Joblib

---

## 📊 Exploratory Data Analysis

- Data inspection
- Duplicate checking
- Correlation Heatmap
- Boxplots
- Dataset statistics

---

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The model with the highest accuracy is automatically selected and saved.

---

## 💻 Streamlit Application

The application allows users to:

- Enter applicant information
- Predict loan approval
- Automatically use the best saved model
- Apply feature scaling only when required

---

## 📁 Project Structure

```
Loan-Approval-Prediction/
│
├── APP_LOAN.py
├── Loan_Approval_Coding.ipynb
├── loan_approval_dataset.csv
├── loan_model.pkl
├── model_name.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Alzahraa-Gamal22/Loan-Approval-Prediction.git
```

Install requirements

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run APP_LOAN.py
```

---

## 📈 Results

The project compares all models based on Accuracy and automatically deploys the best-performing model.

---

## 👩‍💻 Author

**Alzahraa Gamal**

AI Engineer