import streamlit as st
import pickle
import pandas as pd

# load model
with open("lr_smote_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

# load feature names
with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)

st.title("Customer Churn Prediction")

tenure = st.number_input("tenure", 0, 100, 5)
monthly = st.number_input("MonthlyCharges", 0.0, 200.0, 50.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])


internet = st.selectbox("InternetService", ["DSL", "Fiber optic", "No"])


paperless = st.selectbox("PaperlessBilling", ["Yes", "No"])


if st.button("Predict"):

    # create empty dataframe with correct columns
    input_df = pd.DataFrame([[0]*len(feature_names)], columns=feature_names)

    # numeric
    if "tenure" in input_df.columns:
        input_df["tenure"] = tenure

    if "MonthlyCharges" in input_df.columns:
        input_df["MonthlyCharges"] = monthly

    # set dummy columns ONLY if they exist
    col = f"Contract_{contract}"
    if col in input_df.columns:
        input_df[col] = 1

    col = f"InternetService_{internet}"
    if col in input_df.columns:
        input_df[col] = 1

    col = f"PaperlessBilling_{paperless}"
    if col in input_df.columns:
        input_df[col] = 1

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Churn")
    else:
        st.success("No Churn")