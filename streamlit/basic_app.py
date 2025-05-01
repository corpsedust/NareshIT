

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("First App")


date_column = 'date/time'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv("uber-raw-data-sep14.csv", nrows = nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis = 'columns', inplace = True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data

data = load_data(10000)

data_load_state = st.subheader( "Rawdata")
if st.checkbox('Show Raw Data'):
    data_load_state = st.text( "Rawdata")
    st.dataframe(data)
# data_load_state.text('Done! (using st.cache_data)')


# st.subheader("Raw data")
# st.write(data)


# st.subheader("A plot for something : ")
# plt.figure(figsize=(10,8))
# fig = sns.countplot(data, x = "churn", hue = "paymentmethod")
# st.pyplot(plt.gcf())


st.subheader("Map of all pickups")
st.map(data)


st.subheader("Filter data by hour")
hour_to_filter = st.slider('hour', 0,23,17)
filtered_data = data[data["date/time"].dt.hour == hour_to_filter]
st.subheader(f"Map of all pickups at {hour_to_filter}:00")
# st.dataframe(data['date/time'].dt.hour)
st.map(filtered_data)



