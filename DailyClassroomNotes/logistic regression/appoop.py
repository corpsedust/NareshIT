# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 19:35:29 2025

@author: vineet
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Importing the dataset

df = pd.read_csv(r"C:\Users\vineet\Desktop\Pyhtonshit\DailyClassroomNotes\logistic regression\logit classification.csv")

x = df.iloc[:,[2,3]].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, random_state = 0)

#Either Normalizer or Standardize the data
#from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#sc = Normalizer()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)


from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression()
classifier.fit(x_train, y_train)



y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix : \n", cm)

from sklearn.metrics import accuracy_score 
ac = accuracy_score(y_test, y_pred)
print(f"Accuracy Score : {ac}")

bias = classifier.score(x_test, y_test)
print(f"Bias : {bias}")

variance = classifier.score(x_train, y_train)
print(f"Variance : {variance}")


from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)

#Case1 : Train_size = 0.8, StandardScaler, Accuracy : 88.75, bias : 0.8875, variance = 0.821875
#Case 2: Train_size = 0.8, Normalizer, Accuracy : 72.5, bias : 0.725, variance = 0.621875

#Case 3: Train_size = 0.75, Normalizer, Accuracy : 68, bias : 0.68, variance = 0.63
#Case 4: Train_size = 0.75, StandardScaler, Accuracy : 87, bias : 0.87, variance = 0.8233333333333334

#Case 5: Train_size = 0.8, No Normalisztion or Standardization, Accuracy : 91.25, bias : 0.9125, variance = 0.81875


#Prediction of unlabelled data (Whether purchase or not) 
#We have a classifier model on historical data


future_data = pd.read_csv("final1.csv")
copy = future_data
x_future = future_data.iloc[:,[3,4]].values
x_future = sc.fit_transform(x_future)
y_future = classifier.predict(x_future)


#new_df = pd.DataFrame({"purchase or not" : y_future})
copy["Purchased or Not"] = y_future
copy["Purchased or Not"] = copy["Purchased or Not"].map({0:"NO", 1:"YES"})
copy.to_csv("Predicted_Data.csv")


#Dependency of random_state and accuracy ?






















