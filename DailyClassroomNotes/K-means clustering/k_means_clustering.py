import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Mall_Customers.csv")
X = df.iloc[:, [3,4]].values


from sklearn.cluster import KMeans   