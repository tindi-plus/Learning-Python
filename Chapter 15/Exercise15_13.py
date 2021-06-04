# -*- coding: utf-8 -*-
"""
@create date: 31-05-2021 21:21:42
@modify date: 31-05-2021 21:21:42
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

den_helder = pd.read_csv('150-031_meantrend.csv')
tiksi = pd.read_csv('030-447_meantrend.csv')
smogen = pd.read_csv('050-011_meantrend.csv')
olands = pd.read_csv('050-091_meantrend.csv')
helsinki = pd.read_csv('060-351_meantrend.csv')

axes = sns.regplot(data=den_helder, x='Year', y='Monthly_MSL', color='b')
axes = sns.regplot(data=tiksi, x='Year', y='Monthly_MSL', color='k')
axes = sns.regplot(data=smogen, x='Year', y='Monthly_MSL', color='y')
axes = sns.regplot(data=olands, x='Year', y='Monthly_MSL', color='r')
axes = sns.regplot(data=helsinki, x='Year', y='Monthly_MSL', color='m')
