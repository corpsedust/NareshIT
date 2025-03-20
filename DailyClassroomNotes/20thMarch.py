# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 19:41:52 2025

@author: vineet
"""

import numpy as np

import matplotlib.pyplot as plt 

import pandas as pd


dataset = pd.read_csv(r"C:\Users\vineet\Desktop\Pyhtonshit\DailyClassroomNotes\Salary_Data.csv")

x = dataset.iloc[:,0]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y , train_size= 0.8,  random_state=0)


#Converting output from train_test_split which is a series data type to array

x_train = x_train.values.reshape(-1,1)

x_test = x_test.values.reshape(-1,1)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)



plt.scatter(x_test, y_test, color = 'red')

plt.plot(x_train, regressor.predict(x_train), color = "Blue")

plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()