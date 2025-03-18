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
