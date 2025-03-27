import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Investment.csv")

x = df.iloc[:,:-2]
y = df.iloc[:,-2]


x = pd.get_dummies(x,dtype = int)


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size= 0.2, random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)