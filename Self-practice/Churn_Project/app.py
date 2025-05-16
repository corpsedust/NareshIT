import streamlit as st
import pandas as pd
import numpy as np
import joblib


#Load trained model 
model = joblib.load("final_gb_classifier.pkl")


data = pd.read_csv("processed_data.csv")


#Streamlit UI

st.title("Customer Churn Predictor")

binary = lambda x : "Yes" if x == 1 else "No"
binary_no = [1,0]

senior_citizen = st.radio(label = "Gender", options = binary_no, format_func= lambda x : "Male" if x == 0 else "Female" )
partner = st.radio("Partner", options = binary_no, format_func = binary)
dependents = st.radio("Dependents", options = binary_no, format_func = binary)
multiple_lines = st.radio("Multiple Lines", options = binary_no, format_func = binary)
online_security = st.radio("Online Security", options = [0,1,2], format_func = lambda x : "No" if x == 0 else "No Internet Service" if x == 1 else "Yes")
online_backup = st.radio("Online Backup", options = [0,1,2], format_func = lambda x : "No" if x == 0 else "No Internet Service" if x == 1 else "Yes")
device_protection = st.radio("Device Protection", options = [0,1,2], format_func = lambda x : "No" if x == 0 else "No Internet Service" if x == 1 else "Yes" )
tech_support = st.radio("Tech Support", options = [0,1,2], format_func = lambda x : "No" if x == 0 else "No Internet Service" if x == 1 else "Yes")
contract = st.radio("Contract", options = [0,1,2], format_func = lambda x : "Month to Month" if x == 0 else "One Year" if x == 1 else "Two Year")
paperless_billing = st.radio("Paperless billing",options = binary_no, format_func = binary )
payment_method = st.radio()
# partner = st.radio("Partner", [0,1])

st.write(senior_citizen, partner, dependents, multiple_lines, online_security, online_backup, device_protection, tech_support,contract, paperless_billing, payment_method)


