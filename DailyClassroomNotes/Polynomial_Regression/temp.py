# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("emp_sal.csv")


x = df.iloc[:,1:2].values
y = df.iloc[:,-1].values

#from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x,y, color = "Cyan")
plt.plot(x, lin_reg.predict(x))
plt.title("Linear Rregression model")
plt.xlabel("Position Number")
plt.ylabel("Salary")
plt.show()

#intercept 
c = lin_reg.intercept_
#
m = lin_reg.coef_
#Salary of someone at level 6.5

lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred

#This gives out output as 330378.78787879
#The salaray of someone at level 6.5 should be between 150000 and 200000
#Clearly our model is shite, and prediction is not apt


#Polynomial Regression 

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures()
x_poly = poly_reg.fit_transform(x)