# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:34:32 2021
fliping a coin
@author: Tindi.Sommers
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [random.randrange(1, 3) for i in range(2000)]
values, freq = np.unique(x, return_counts=True)
coin = ['Head', 'Tail']

# plot a graph of frequency against the values of the coin flip
title = 'Bar plot of coin flips'
sns.set_style('whitegrid')
axes = sns.barplot(x=coin, y=freq, palette='bright')
axes.set_title(title)
axes.set(xlabel='Coin', ylabel='Frequencies')
axes.set_ylim(top=max(freq) * 1.1)
for bar, frequency in zip(axes.patches, freq):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / sum(freq):.2%}'
    axes.text(text_x, text_y, text, fontsize=12, ha='center', va='bottom')
plt.show()
