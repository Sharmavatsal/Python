from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler



df = pd.read_csv('data-new.csv')

data2 = df
label_encoder = LabelEncoder()
data2["verification.result1"] = label_encoder.fit_transform(data2["verification.result"])#converrt into 0/1
print(data2)

data3 = data2
sscaler = StandardScaler()
data3[['Averification.timege1']] = sscaler.fit_transform(data3[['verification.time']])#connvert into 0/1 (when colmun is outlier)
print(data3)
 
minmax = MinMaxScaler()
data3[['Salary']] = minmax.fit_transform(data3[['Salary']])


