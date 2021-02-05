# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:24:14 2020

A graphical representation of rolling a die

@author: Tindi.Sommers
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

rolls = [random.randrange(1, 7) + random.randrange(1, 7) for i in range(360000)]
values, frequencies = np.unique(rolls, return_counts=True)

title = f'Rolling a six-sided die twice {len(rolls):,} times' # set the tile text

axes = sns.barplot(x=frequencies, y=values, palette='bright', orient='h')
sns.set_style('whitegrid')
axes.set_title(title)
axes.set(xlabel='Sum of Dies', ylabel='Frequency')

# set the data labels
axes.set_xlim(0, max(frequencies) * 1.1)

for bar, frequency in zip(axes.patches, frequencies):
    text_y = bar.get_y() + bar.get_height() / 2
    text_x = bar.get_width()
    text = f'{frequency:,}\n{frequency / len(rolls):.2%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='left', va='center')

plt.show()
