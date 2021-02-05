# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:44:25 2021
Counting Duplicate words in a sentence
@author: Tindi.Sommers
"""

from collections import Counter


text = input('Pls type the sentence you want to check for duplicate words: ')

counts = Counter(text.split())

print('Duplicate words include:')

for word, count in sorted(counts.items()):
    if count > 1:
        print(word)
