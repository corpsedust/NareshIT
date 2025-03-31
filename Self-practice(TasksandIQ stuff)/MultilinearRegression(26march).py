import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Investment.csv")

x = df.iloc[:,:-2]
y = df.iloc[:,-2]


x = pd.get_dummies(x,dtype = int)


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size= 0.2, random_state=0)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

comparison = pd.DataFrame({"Actual" : y_test, "Predicted" : y_pred})


#Coefficient and intercept
slope = model.coef_
constant = model.intercept_


#training score 
bias = model.score(x_train, y_train)

#testing score 
variance = model.score(x_test, y_test)



x = np.append(arr = constant * np.ones((50,1)).astype(int), values = x, axis = 1)

import statsmodels.api as sm

X_opt = x[:,[0,1,2,3,4,5,6]]


#Ordinary Least Squares

model_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(model_OLS.summary())


#from ols regression result, acceptable p-values that are <0.05 are only 
#for constant and x1
#step by step  we remove each feature which has p-value > 0.05
#start with highest that is x4


X_opt = x[:,[0,1,2,3,4,6]]
model_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(model_OLS.summary())


X_opt = x[:,[0,1,2,3,6]]
model_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(model_OLS.summary())



X_opt = x[:,[0,1,3]]
model_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(model_OLS.summary())




X_opt = x[:,[0,1,3]]
model_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(model_OLS.summary())





X_opt = x[:,[0,1]]
model_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(model_OLS.summary())




bias = model.score(x_train, y_train)
variance = model.score(x_test, y_test)

print(bias, variance)

























