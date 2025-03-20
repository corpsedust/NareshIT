# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 19:41:40 2025

@author: vineet
"""


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


#Import the dataset
df = pd.read_csv(r"C:\Users\vineet\Desktop\Pyhtonshit\DailyClassroomNotes\Data_18March.csv")


#Split the dataset;
x = df.iloc[:,:-1].values
y = df.iloc[:,3].values


#filling missing values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="most_frequent")
#imputer = SimpleImputer() #by default mean strategy
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

# impute categorical value for independent variable 


from sklearn.preprocessing import LabelEncoder 

labelencoder_x = LabelEncoder()
labelencoder_x.fit_transform(x[:,0])
x[:,0] = labelencoder_x.fit_transform(x[:,0])

#impute categorical value for dependent variable



labelencoder_y = LabelEncoder()
labelencoder_y.fit_transform(y)
y = labelencoder_y.fit_transform(y)


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state=0)

#Random state need to be zero other wise every time you run the code you will pick random 
#records for train and test 
