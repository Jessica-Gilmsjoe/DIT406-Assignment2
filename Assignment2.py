#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:14:38 2021

@author: jessicagilmsjoe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, ConfusionMatrixDisplay

#%%
houses = pd.read_csv("data_assignment2.csv")

#%%
### Question 1
# a)

# Model linear regression area and price
model = LinearRegression().fit(houses[['Living_area']], houses[['Selling_price']])

# b)

# slope
slope = model.coef_

# intersection
intersection = model.intercept_

# c)

pred_100 = model.predict([[100]])
pred_150 = model.predict([[150]])
pred_200 = model.predict([[200]])

# d)

# residual plot
pred_price = model.predict(houses[['Living_area']])
residuals = pred_price - houses[['Selling_price']]
plt.scatter(pred_price, residuals, c = 'b', s = 50, alpha = 0.4)
plt.hlines(y = 0, xmin = 3400000, xmax = 6500000)
plt.title('Residual plot')
plt.ylabel('Residuals')

#%%
### Question 2

# a)
# load iris data and create dataframe
from sklearn.datasets import load_iris
iris_raw = load_iris()

iris = pd.DataFrame(iris_raw.data , columns = iris_raw.feature_names)
iris['species'] = iris_raw.target 
iris['species'] = iris['species'].replace(to_replace= [0, 1, 2], 
    value = ['setosa', 'versicolor', 'virginica'])

x_train, x_test, y_train, y_test = train_test_split(iris[iris.columns[0:4]], 
                                                    iris[['species']], 
                                                    test_size=0.25, random_state=0)

model = LogisticRegression().fit(x_train, y_train)
plot_confusion_matrix(model,x_test,y_test)

#%%
## knn
k = 3
neigh = KNeighborsClassifier(n_neighbors=k)
neigh.fit(iris[iris.columns[0:4]], iris[['species']])

