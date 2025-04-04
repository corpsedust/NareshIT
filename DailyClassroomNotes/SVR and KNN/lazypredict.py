# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 16:00:36 2025

@author: vineet
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("emp_sal.csv")


x = df.iloc[:,1:2].values
y = df.iloc[:,-1].values


from lazypredict.Supervised