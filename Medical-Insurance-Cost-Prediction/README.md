\# Medical Insurance Cost Prediction



A Machine Learning project that predicts medical insurance charges based on customer information using multiple regression algorithms.



\---



\## Project Overview



This project analyzes the Medical Insurance dataset, performs data preprocessing and exploratory data analysis (EDA), trains multiple regression models, compares their performance, and automatically saves the best-performing model for future predictions.



\---



\## Dataset Features



The dataset contains the following features:



\- Age

\- Sex

\- BMI

\- Number of Children

\- Smoker Status

\- Region



Target Variable:



\- Medical Insurance Charges



\---



\## Data Preprocessing



The following preprocessing steps were performed:



\- Removed duplicate records

\- Checked for missing values

\- Exploratory Data Analysis (EDA)

\- Correlation analysis

\- One-Hot Encoding for categorical variables using `pd.get\_dummies()`



\---



\## Exploratory Data Analysis



The notebook includes:



\- Histograms

\- Boxplots

\- Scatter Plot (Age vs Charges)

\- Correlation Heatmaps

\- Category Distribution



Key Findings:



\- Smoking has the strongest impact on medical insurance charges.

\- Medical charges generally increase with age.

\- Higher BMI tends to increase insurance costs.

\- Gender has a relatively small effect.

\- Number of children has a minor influence.

\- Region has little impact on insurance charges.



\---



\## Machine Learning Models



The following regression models were trained and compared:



\- Linear Regression

\- Decision Tree Regressor

\- Random Forest Regressor

\- XGBoost Regressor



Evaluation Metrics:



\- R² Score

\- MAE

\- RMSE



The best-performing model is automatically selected based on the highest \*\*R² Score\*\* and saved for deployment.



\---



\## Project Structure



```

Medical-Insurance-Cost-Prediction/

│

├── Medical\_Insurance\_Coding.ipynb

├── APP\_INSURANCE.py

├── insurance.csv

├── insurance\_model.pkl

├── model\_name.pkl

├── columns.pkl

├── README.md

└── requirements.txt

```



\---



\## Installation



Clone the repository:



```bash

git clone https://github.com/Alzahraa-Gamal22/Machine-Learning-NTI\_Projects.git

```



Move to the project folder:



```bash

cd Medical-Insurance-Cost-Prediction

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## Run the Streamlit App



```bash

streamlit run APP\_INSURANCE.py

```



or



```bash

python -m streamlit run APP\_INSURANCE.py

```



\---



\## Example Prediction



Input:



\- Age: 30

\- BMI: 25

\- Children: 2

\- Sex: Female

\- Smoker: No

\- Region: Southeast



Output:



```

Predicted Insurance Charge: $7,850.42

```



\---



\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- XGBoost

\- Joblib

\- Streamlit



\---



\## Future Improvements



\- Hyperparameter Tuning

\- Cross Validation

\- Feature Importance Visualization

\- Model Explainability using SHAP

\- Docker Deployment

\- Cloud Deployment (Streamlit Community Cloud)



\---



\## Author



\*\*Alzahraa Gamal\*\*



AI Engineer



GitHub:

https://github.com/Alzahraa-Gamal22



