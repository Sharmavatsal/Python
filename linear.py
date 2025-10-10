# Linear Regression 

import pandas as pd

df=pd.read_csv("Housing.csv")
new_df=df
new_df['mainroad']=new_df['mainroad'].map({'yes':1,'no':0})
new_df['guestroom']=new_df['guestroom'].map({'yes':1,'no':0})
# same for all other such columns with such data
new_df.drop(['price'],axis="columns")
price=df.price
print(price)

from sklearn import linear_model

model2 = linear_model.LinearRegression()
model2.fit(new_df,price)
model2.predict(new_df)
PREDICT_PRICE=model2.predict(new_df)
new_df['NEW_PRICE']=PREDICT_PRICE
new_df.to_csv('Housing_123.csv')

"""
area_df=df['area'] # area is a dataframe
print(area_df)
price_df=df.price # here price is not dataframe
print(price_df)
area_df.drop('price',axis=1)# axis 1 is for columns

from sklearn import linear_model

model = linear_model.LinearRegression()
model.fit(area_df,price_df)


import pandas as pd

df=pd.read_csv("")
area_df=df.drop('price',axis='columns')
price_df=df.price

from sklearn import linear_model

model=linear_model
"""