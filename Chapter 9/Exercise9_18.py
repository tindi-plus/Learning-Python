# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:42:20 2021.

Analysing the anscombe.csv dataset

@author: Tindi.Sommers
"""
import pandas as pd

df = pd.read_csv('anscombe.csv', index_col=0)

print(df.describe())
# plot the dataframe values to as a scatter plot
df.plot.scatter(x='x1', y='y1', c='DarkRed')
df.plot.scatter(x='x2', y='y2', c='DarkRed')
df.plot.scatter(x='x3', y='y3', c='DarkRed')

