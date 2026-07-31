# 🏥 Medical Insurance Cost Prediction

A Machine Learning project that predicts **medical insurance charges** based on customer information using multiple regression algorithms.

---

## 📌 Project Overview

This project analyzes the Medical Insurance dataset, performs data preprocessing and exploratory data analysis (EDA), trains multiple regression models, compares their performance, and automatically saves the best-performing model for future predictions.

---

## 📂 Dataset Features

### Features
- Age
- Sex
- BMI
- Number of Children
- Smoker Status
- Region

### Target
- Medical Insurance Charges

---

## 🛠 Data Preprocessing

- Removed duplicate records
- Checked for missing values
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- One-Hot Encoding using `pd.get_dummies()`

---

## 📊 Exploratory Data Analysis

The notebook includes:

- Histograms
- Boxplots
- Scatter Plot (Age vs Charges)
- Correlation Heatmaps

### Key Findings

- 🚬 Smoking has the strongest impact on insurance charges.
- 👤 Medical charges generally increase with age.
- ⚖️ Higher BMI tends to increase insurance costs.
- 👨 Gender has little effect.
- 👶 Number of children has a small impact.
- 🌍 Region has little influence on insurance charges.

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model | Purpose |
|-------|---------|
| Linear Regression | Baseline Model |
| Decision Tree Regressor | Non-linear Regression |
| Random Forest Regressor | Ensemble Learning |
| XGBoost Regressor | Gradient Boosting |

### Evaluation Metrics

- R² Score
- MAE
- RMSE

The model with the **highest R² Score** is automatically selected and saved.

---

## 📁 Project Structure

```text
Medical-Insurance-Cost-Prediction/
│
├── APP_INSURANCE.py
├── Medical_Insurance_Coding.ipynb
├── insurance.csv
├── insurance_model.pkl
├── model_name.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Alzahraa-Gamal22/Machine-Learning-NTI_Projects.git
```

Move to the project folder:

```bash
cd Medical-Insurance-Cost-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
python -m streamlit run APP_INSURANCE.py
```

---

## 💡 Example Prediction

**Input**

| Feature | Value |
|---------|------:|
| Age | 30 |
| BMI | 25 |
| Children | 2 |
| Sex | Female |
| Smoker | No |
| Region | Southeast |

**Output**

```text
Predicted Insurance Charge: $7,850.42
```

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Importance Visualization
- SHAP Explainability
- Docker Deployment
- Streamlit Community Cloud Deployment

---

## 👩‍💻 Author

**Alzahraa Gamal**

AI Engineer | Machine Learning Enthusiast

GitHub: **https://github.com/Alzahraa-Gamal22**
