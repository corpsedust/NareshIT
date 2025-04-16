# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 20:01:56 2025

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
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.80, random_state = 0)


#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()

#from sklearn.preprocessing import Normalizer
#sc = Normalizer()


#x_train = sc.fit_transform(x_train)
#x_test = sc.fit_transform(x_test)


dt = DecisionTreeClassifier(criterion="entropy", max_depth=10, random_state=None)
dt.fit(x_train, y_train)


y_pred = dt.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix : \n", cm)

ac = accuracy_score(y_test, y_pred)
print(f"Accuracy Score : {ac}")

variance = dt.score(x_train, y_train)
print(f"Variance : {variance}")


cr = classification_report(y_test, y_pred)
print(cr)