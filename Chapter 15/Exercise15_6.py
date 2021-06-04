# -*- coding: utf-8 -*-
"""
@create date: 30-05-2021 16:19:57
@modify date: 30-05-2021 16:19:57
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

l_r = LinearRegression()
nyc = pd.read_csv('ave_yearly_temp_nyc_1895-2017.csv')
nyc.Date = nyc.Date.floordiv(100)
nyc.columns = ['Date', 'Temperature', 'Value']
print(nyc.head(5))

# split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1, 1),
    nyc.Temperature.values, random_state=11)

# train the data
l_r.fit(X=X_train, y=y_train)
print('Coefficient: ', l_r.coef_)
print('Intercept: ', l_r.intercept_)
predicted = l_r.predict(X_test)
expected = y_test
print(f'{predicted[3]} : {expected[3]}')

# visualize the data
axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', hue='Temperature',
    palette='winter', legend=False)
