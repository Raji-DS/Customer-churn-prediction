# Customer Churn Prediction Project

## Overview

This project predicts customer churn using machine learning models.  
The goal is to identify customers who are likely to leave the company so that the business can take preventive actions.

The project includes data preprocessing, feature selection, model training, hyperparameter tuning, and deployment using Streamlit.

---

## Dataset

The dataset contains customer information such as:

- tenure
- MonthlyCharges
- Contract type
- InternetService
- PaperlessBilling
- and other customer features

Target variable: Churn (0 = No, 1 = Yes)

Dataset stored in:data/Telco_customer_churn.csv

---

## Project Steps

1. Data preprocessing
2. Handling missing values
3. Correlation heatmap analysis
4. Feature selection using Lasso regularization
5. Handling imbalanced data using SMOTE and class_weight
6. Model training:
   - Logistic Regression
   - Random forest classifer
   - XGBoost
7. Hyperparameter tuning using GridSearchCV
8. Model evaluation using:
   - Classification_report
   - Confusion matrix
   - ROC-AUC

9. Model deployment using Streamlit
10. Model saved using Pickle

---

## Models Used

- Logistic Regression
- Logistic Regression with SMOTE
- Logistic Regression with class_weight
- XGBoost
- Tuned XGBoost

Final model saved as:
lr_smote_pipeline.pkl

---

## Evaluation Metrics

Metrics used:

- Classification_report
- ROC-AUC
- Confusion Matrix

These metrics are important because the dataset is imbalanced.

---

## Project Structure

```
churn_prediction_project/
│
├── app.py
├── README.md
├── requirements.txt
├── lr_smote_pipeline.pkl
├── feature_names.pkl
├── data/
│   └── churn.csv
```

---

## How to run the project

Install libraries:

```
pip install -r requirements.txt
```

Run Streamlit app: streamlit run app.py
```

---

## Deployment

The model is deployed using Streamlit.

The user enters customer details and the app predicts whether the customer will churn.

---

## Author

Rajeswari Puliyadi Subramanian
