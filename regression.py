 # Logistic Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression

# read file

df = pd.read_csv("house.csv")
print("df")
df.info()

# Extract parameters

x = df[['Age','Income','CreditScore']] # independent variable
Y = df['Purchased'] # dependent variable (only one in any data)

print(x)
print(Y)

# Create instance of model from the class

logModel = LogisticRegression()

# train the model 

logModel.fit(x,Y)

age = int(input("Enter Age : "))
income = int(input("Enter Income : "))
Score = int(input("Enter CreditScore : "))

d=np.array([[age,income,Score]])

# Predict for the unknown data

yp = logModel.predict(d)# values for x i.e age,income,creditscore
print(yp)

# White box approach 

b1 = logModel.coef_
b0 = logModel.intercept_

print(b1)
print(b0)

#Yp = b0 + np.dot(x,b1.ravel())

#print(Yp)
Yp=
SYp = 1/(1+np.exp(-Yp))

print(SYp)

Ytmp = [Y,np.round(SYp)]
print(Ytmp)