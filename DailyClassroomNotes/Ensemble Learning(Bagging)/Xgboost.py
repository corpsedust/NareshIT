import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Import the data set 

df = pd.read_csv(r"C:\Users\vineet\Desktop\Pyhtonshit\DailyClassroomNotes\Ensemble Learning(Bagging)\Churn_Modelling.csv")
X = df.iloc[:,3:-1].values
y = df.iloc[:-1].values



#Encoding Categorical dataa

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,2] = le.fit_transform(X[:,2])


#Onehot encoding the "Geography" column 

from sklearn.compose import ColumnTransformer
from skelarn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers= [('encoder', OneHotEncoder(), [1]), remainder = 'passthrough'])
X = np.array(ct.fit_transform(X))
print(X)

#Splitiing the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)


# Predicting the Test set results
y_pred = classifier.predict(X_test)



from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)


bias = classifier.score(X_train, y_train)





















