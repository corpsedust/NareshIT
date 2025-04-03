# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:37:52 2025

@author: vineet
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


#WHAT IS HAPPENING HERE, WHY DO WE NEED LINEAR REGRESSION AGAIN ????
poly_reg.fit(x_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

#Polynomial Visualisation

plt.scatter(x,y,color = "red")
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color = "Blue")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

lin_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
lin_model_pred
#The answer is 189498.10606061



#Support Vector Regression

from sklearn import svm
svr_reg = svm.SVR()

svr_reg.fit(x,y)

plt.scatter(x,y,color = "red")
plt.plot(x, svr_reg.predict(x), color = "Blue")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()



lin_model_pred = svr_reg.predict([[6.5]])
lin_model_pred

#Hyperparameter tuning


from sklearn import svm
svr_reg = svm.SVR(kernel = "poly", degree=4, gamma = "auto", C = 2.0)

svr_reg.fit(x,y)

plt.scatter(x,y,color = "red")
plt.plot(x, svr_reg.predict(x), color = "Blue")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()



svr_model_pred = svr_reg.predict([[6.5]])
svr_model_pred


#Predicted salary is not 175K




#Decision tree Regressor

from sklearn.tree import DecisionTreeRegressor 

dt_reg = DecisionTreeRegressor(criterion="absolute_error",splitter = "random", random_state=0, max_depth=6)
dt_reg.fit(x,y)


plt.scatter(x,y,color = "red")
plt.plot(x, dt_reg.predict(x), color = "Blue")
plt.xlabel("DT Position Level")
plt.ylabel("Salary")
plt.show()

dt_model_pred = dt_reg.predict([[6.5]])
dt_model_pred


#Salary comes out to be 150K



#Random Forest

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(random_state=0, criterion="poisson", max_depth = 6)

rf_reg.fit(x,y)

plt.scatter(x,y,color = "red")
plt.plot(x, rf_reg.predict(x), color = "Blue")
plt.xlabel("RF Position Level")
plt.ylabel("Salary")
plt.show()

rf_model_pred = rf_reg.predict([[6.5]])
rf_model_pred


#This will give random values everytime it is executed unitl you set random_state to 0 (fixed number)
