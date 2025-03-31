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


st.subheader("Comparing Graphs based on sample size")
fig2 = plt.figure()
small_sample_mean = [sampler(population)[1] for _ in range(1000) if sampler(population)[0]<50]
large_sample_mean = [sampler(population)[1] for _ in range(1000) if sampler(population)[0] >100]
sns.histplot(small_sample_mean, kde = True, label = "Small Sample Mean", color = "blue")
sns.histplot(large_sample_mean, kde = True, label = "Large Sample Mean", color = "red")
plt.legend()
plt.show()
st.pyplot(fig2)
st.write("As sample size increases, the graph goes towards normal distribution")

st.subheader("Normal Distribution")
fig3 = plt.figure()
mean = random_data["sample_mean"].mean()
std = random_data["sample_mean"].std()
x = np.linspace(mean -3*std, mean+ 3*std, 100)
plt.plot(x, norm.pdf(x,mean,std,), label = "Normal Curve")
sns.histplot(random_data["sample_mean"], kde = "True", label = "SampleMeans")
plt.legend()
plt.show()
st.pyplot(fig3)