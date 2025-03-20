import streamlit as st 
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Sales Data Analysis for a Retail Store")
st.write("This application analyzes data for various product categories")

def generate_data():
    np.random.seed(42)
    data = {
        'product_id': range(1, 21),
        'product_name': [f'Product {i}' for i in range(1, 21)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], 20),
        'units_sold': np.random.poisson(lam=20, size=20),
        'sale_date': pd.date_range(start='2023-01-01', periods=20, freq='D')
    }
    return pd.DataFrame(data)

sales_data = generate_data()

#Display shit


st.subheader("Sales Data")
st.dataframe(sales_data)


#Descriptive Stats

st.subheader("Descriptive Statistics")
descriptive_stats = sales_data.units_sold.describe().T
st.datframe(descriptive_stats)


mean_sales = sales_data.units_sold.mean()
median_sales = sales_data.units_sold.median()
mode_sales = sales_data.units_sold.mode()

st.write(f"Mean of units sold: {mean_sales}")
st.write(f"Median of units sold: {median_sales}")
st.write(f"Mode of units sold: {mode_sales}")

#Group statistics by Category

category_stats = sales_data.groupby("category")["units_sold"].agg("sum", "mean", "std").reset_index()
