# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:14:33 2021
Survey responses
@author: Tindi.Sommers
"""
import random
import numpy as np
import statistics
import matplotlib as plt
import seaborn as sns

x = [random.randrange(1, 11) for i in range(50)]
values, freq = np.unique(x, return_counts=True)

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, freq = np.unique(responses, return_counts=True)
print(values)
print(freq)
print()
statistics.mean(responses)

print(min(responses))
print(max(responses))
print(max(responses) - min(responses))
print(statistics.stdev(responses))
print(statistics.variance(responses))
print(statistics.median(responses))
print(statistics.mode(responses))

# plot a graph of frequency against the values of responses
title = 'Bar plot of response frequencies'
sns.set_style('whitegrid')
axes = sns.barplot(values, freq, palette='bright')
axes.set_title(title)
axes.set(xlabel='Responses', ylabel='Frequencies')
axes.set_ylim(top=max(freq) * 1.1)
for bar, frequency in zip(axes.patches, freq):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / sum(freq):.2%}'
    axes.text(text_x, text_y, text, fontsize=12, ha='center', va='bottom')
