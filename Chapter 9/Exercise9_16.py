# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:39:21 2021.

Analysing diamonds.csv dataset

@author: Tindi.Sommers
"""

import pandas as pd

df = pd.read_csv('diamonds.csv', index_col=0)
print(df.head(7))
print()
print(df.tail(7))
print()
pd.set_option('Precision', 2)
print(df.describe())
print()
series = pd.Series(df.loc[:, 'cut'])
print()
print(series.describe())
series = pd.Series(df.loc[:, 'color'])
print()
print(series.describe())
series = pd.Series(df.loc[:, 'clarity'])
print()
print(series.describe())
