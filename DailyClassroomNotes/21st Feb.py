import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Load Titanic dataset 

@st.cache  #What is happening here?

def load_data():
    data = pd.read_csv("titanicdataset.csv")
    return data

data = load_data()


#Title and description 

st.title("Exploratory Data Analysis of Titanic Dataset")
st.write("This is an EDA on the Titanic dataset.")
st.write("First frew rows of the dataset")
st.dataframe(data.head())


# Data Cleaning Section 

st.subheader("Missing Values")
missing_data = data.isnull().sum()