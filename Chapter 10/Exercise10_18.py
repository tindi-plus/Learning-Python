# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:37:00 2021.

Analysis of temperatures in Los Angeles

@author: Tindi.Sommers
"""
import pandas as pd
import seaborn as sns
from scipy import stats

temps = pd.read_csv('ave_hi_la_jan_1895-2018.csv')
temps.columns = ['Date', 'Temperature', 'Anomaly']
temps.Date = temps.Date.floordiv(100)

print(temps.head(3))

line_regress = stats.linregress(x=temps.Date, y=temps.Temperature)
print()
print('Slope: ', line_regress.slope)
print('Intercept: ', line_regress.intercept)

axes = temps.plot.scatter(x='Date', y='Temperature')

axes.set_ylim(10, 70)
axes.set_ylabel('Temperature')

sns.set_style('whitegrid')

axes2 = sns.regplot(x=temps.Date, y=temps.Temperature)

# make the points more clustered together so that the partern can be visible
axes2.set_ylim(10, 70)