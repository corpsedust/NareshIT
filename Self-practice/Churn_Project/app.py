import streamlit as st
import pandas as pd
import numpy as np
import joblib



def stream_service(x):
    return  "No" if x == 0 else "Yes" if x == 1 else "No Internet Service"

def no_service(x):
    return  "No" if x == 0 else "No Internet Service" if x == 1 else "Yes"


def payment(x):
    return "Bank Transfer" if x == 0 else "Credit Card" if x == 1 else "Electronic Check" if x == 2 else "Mailed Check"

def tenure(x):
    return "1-12" if x == 0 else "13-24" if x == 1 else "25-36" if x == 2 else "37-48" if x == 3 else "49-60" if x == 4 else "61-72"


def binary(x): 
    return "Yes" if x == 1 else "No"
    
#Load trained model 
model = joblib.load("final_gb_classifier.pkl")


data = pd.read_csv("processed_data.csv")



#Streamlit UI

st.title("Customer Churn Predictor")




binary_no = [1,0]


col1,col2,col3 = st.columns(3)


with col1:
    senior_citizen = st.selectbox(label = "Senior Citizen", options = binary_no, format_func = binary)
    partner = st.selectbox("Partner", options = binary_no, format_func = binary)
    dependents = st.selectbox("Dependents", options = binary_no, format_func = binary)
    multiple_lines = st.selectbox("Multiple Lines", options = binary_no, format_func = binary)
    online_security = st.selectbox("Online Security", options = [0,1,2], format_func = no_service)
    
with col2:
    online_backup = st.selectbox("Online Backup", options = [0,1,2], format_func = no_service)
    device_protection = st.selectbox("Device Protection", options = [0,1,2], format_func = no_service)
    tech_support = st.selectbox("Tech Support", options = [0,1,2], format_func = no_service)
    streaming_service = st.selectbox("Streaming Service", options = [0,1,2], format_func = stream_service)
    contract = st.selectbox("Contract", options = [0,1,2], format_func = no_service)
with col3:
    paperless_billing = st.selectbox("Paperless billing",options = binary_no, format_func = binary )
    payment_method = st.selectbox("Payment Method", options = [0,1,2,3], format_func = payment)
    monthly_charges = st.number_input("Monthly Charges", min_value = 18, max_value = 120)
    total_charges = st.number_input("Total Charges", min_value = 18, max_value = 8685)
    tenure_group = st.selectbox("Tenure Group", options = [0,1,2,3,4], format_func = tenure)


user_data = {'SeniorCitizen': senior_citizen,
                'Partner': partner,
                'Dependents': dependents,
                'MultipleLines': multiple_lines,
                'OnlineSecurity': online_security,
                'OnlineBackup': online_backup,
                'DeviceProtection': device_protection,
                'TechSupport': tech_support,
                'Contract': contract,
                'PaperlessBilling': paperless_billing,
                'PaymentMethod': payment_method,
                'MonthlyCharges': monthly_charges,
                'TotalCharges': total_charges,
                'tenure_group': tenure_group,
                'Streaming Service': streaming_service}


# X = pd.DataFrame(user_data, index = [0])
# st.write(X)


if st.button("Predict"):
    X = pd.DataFrame(user_data, index = [0])
    # st.write(X)
    y = model.predict(X)    
    st.write(f"Customer Churn : {binary(y)}")