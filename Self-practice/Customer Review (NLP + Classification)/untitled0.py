# -*- coding: utf-8 -*-
"""
Created on Tue May  6 19:22:10 2025

@author: vineet
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\vineet\Desktop\textcleanup\Restaurant_Reviews.tsv", delimiter="\t")


#Cleaning the text 
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(1, 1000):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review = review.lower()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if word not in stopwords]
    review = ''.join(review)
    corpus.append(review)
    
    
    
    


