import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import streamlit as st
import statistics

st.title("Central Limit Theorem")
st.write("This is a an attempt to visualize the CLT")

population = [random.randint(1,10000) for _ in range(1000)]


#chooses random numbers from a list of size between 30 and 130 chosen randomly

def sampler(lst):
    size = random.randint(30,130)
    new_lst = [random.choice(lst) for _ in range(size)]
    new_lst_mean = sum(new_lst) / size
    return size, new_lst_mean

def generate_data():
    data = [sampler(population) for _ in range(1000)]
    df = pd.DataFrame(data, columns = ["sample_size", "sample_mean"])
    return df
    
random_data = generate_data()
    
#display this data

st.subheader("Data (generated randomly)")
st.dataframe(random_data)    

population_mean = statistics.mean(population)
population_std = statistics.stdev(population)

st.write(f"Mean of population: {population_mean}")
st.write(f"Standard Deviation of population: {population_std}")


st.subheader("Visualisation")

st.write("Graph of distribution of means for 1000 samples taken with each having sample size in the range (30,130)")
plt.figure(figsize=(10,6))
sns.displot(random_data, x = "sample_mean", kde = True, label = "sample_mean", color = "violet")
plt.legend()
st.pyplot(plt)