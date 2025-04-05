
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("emp_sal.csv")


x = df.iloc[:,1:2].values
y = df.iloc[:,-1].values

from lazypredict.Supervised import  LazyRegressor

from sklearn.model_selection import train_test_split

x_train, y_train, x_test, y_test = train_test_split(x,y, train_size= 0.8)

reg = LazyRegressor(verbose = 0, ignore_warnings = False, custom_metric = None)
models, prediction = reg.fit(x_train, x_test, y_train, y_test)
