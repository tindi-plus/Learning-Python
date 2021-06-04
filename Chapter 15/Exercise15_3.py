# -*- coding: utf-8 -*-
"""
@create date: 30-05-2021 14:49:07
@modify date: 30-05-2021 14:49:07
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""
from sklearn.datasets import fetch_california_housing
import seaborn as sns
import pandas as pd

california = fetch_california_housing()

pd.set_option('precision', 4)
pd.set_option('max_columns', 9)
pd.set_option('display.width', None)
sns.set(font_scale=2)
sns.set_style('whitegrid')

cali_df = pd.DataFrame(data=california.data, columns=california.feature_names)
cali_df['MedHouseValue'] = pd.Series(california.target)

pairplot = sns.pairplot(data=cali_df, vars=cali_df.columns[0:8], hue='MedHouseValue')