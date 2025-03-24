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

dx_train = x_train.values.reshape(-1,1)

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




plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = "Blue")
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()



coeff = regressor.coef_  #m of y = mx + c
intercept = regressor.intercept_# c  of y = mx + c


comparison = pd.DataFrame({"Actual" : y_test, "Predicted":y_pred})
print(comparison)



# Salary of someone who has 12 years of experience

exp_12_yrs = coeff*12 + intercept
print(exp_12_yrs)

#Answer = 139100.52677552



#Training Score 

bias = regressor.score(x_train, y_train)
print(bias)


#Test Score 
variance = regressor.score(x_test, y_test)
print(variance)


# Bias = 0.9423777652193379
# Variance = 0.9740993407213511
# Both should approach 1, so better the model 




#Statistical Analysis
average = dataset.mean()
average_salary = dataset.Salary.mean()

median = dataset.median()
median_salary = dataset.Salary.median()

mode = dataset.mode()
mode_salary = dataset.Salary.mode()


#Variance 
variance = dataset.var()
variance_salary = dataset.Salary.var()


#Standard Deviation 
std = dataset.std()
std_salary = dataset.Salary.std()


#coefficient of Variation 
import scipy.stats as stats
from scipy.stats import variation

var = variation(dataset.values)
var_salary = variation(dataset.Salary.values)


#correlation 
corr = dataset.corr()
corr_salary = dataset.Salary.corr(dataset.YearsExperience)


#skewness
skew = dataset.skew()
skew_salary = dataset.Salary.skew()


#Standard Error

standard_error = dataset.sem() 
standard_error_salary = dataset.Salary.sem()


#Z_score

z_score = dataset.apply(stats.zscore)
z_score

#Degree of Freedom

a = dataset.shape[0]
b = dataset.shape[1]

degree_of_freedom = a - b
print(degree_of_freedom)



#Sum of Squares Regression (SSR)

y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean) ** 2)
print(f"SSR : {SSR}")


#SSE

y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(f"SSE{SSE}")


#SST

mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values - mean_total)**2)
print(f"SST:{SST}")


#Quality of model
r_square = 1 - (SSR/SST)
r_square
print(f"r_square : {r_square}")








































