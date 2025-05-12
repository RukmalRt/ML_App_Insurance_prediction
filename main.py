import streamlit as st

import pandas as pd
from prediction_helper import predict

st.set_page_config(page_title="Insurance Premium Predictor", layout="wide")
st.title("💰 Insurance Premium Predictor")

st.markdown("### Please fill out the form below:")

# Define options for dropdowns
age_options = list(range(18, 101))
genetical_risk_options = [1, 2, 3, 4, 5]

# Create 4-column layout
col1, col2, col3 = st.columns(3)

with col1:
    age = st.selectbox("Age", age_options)
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])

with col2:
    gender = st.selectbox("Gender", ['Male', 'Female'])
    genetical_risk = st.selectbox("Genetical Risk (1=Low, 5=High)", genetical_risk_options)
    smoking_status = st.selectbox(
        "Smoking Status",
        ['No Smoking', 'Regular', 'Occasional']
    )
    income_level = st.selectbox("Income Level", ['<10L', '10L - 25L', '25L - 40L', '> 40L'])

with col3:
    dependants = st.selectbox("Number of Dependants", list(range(0, 11)))
    income_lakhs = st.selectbox("Income (Lakhs)", list(range(0, 101)))
    medical_history = st.selectbox(
        "Medical History",
        [
            'Diabetes', 'High blood pressure', 'No Disease',
            'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
            'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ]
    )
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

#with col4:

    #region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

input_dict = {
        "Age": age,
        "Gender": gender,
        #"Region": region,
        "Marital_status": marital_status,
        "Number Of Dependants": dependants,
        "BMI_Category": bmi_category,
        "Smoking_Status": smoking_status,
        "Employment_Status": employment_status,
        "Income_Level": income_level,
        "Income_Lakhs": income_lakhs,
        "Medical History": medical_history,
        "Insurance_Plan": insurance_plan,
        "Genetical_Risk": genetical_risk
    }
# Submit button
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')