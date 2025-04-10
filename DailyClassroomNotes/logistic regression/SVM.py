#Import the library


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Importing the dataset

df = pd.read_csv(r"C:\Users\vineet\Desktop\Pyhtonshit\DailyClassroomNotes\logistic regression\logit classification.csv")

x = df.iloc[:,[2,3]].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, random_state = 0)


