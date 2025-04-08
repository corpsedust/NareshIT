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

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


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

