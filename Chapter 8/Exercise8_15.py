# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:56:21 2021.

Count words in a text

@author: Tindi.Sommers
"""
import re

text = input('Input the text: ')
digits = re.findall(r'\d', text)
nondigits = re.findall(r'\D', text)
white_space = re.findall(r'\s', text)
words = re.findall(r'\w+', text)

print(f'count of digits is {len(digits)}')
print(f'count of nondigits is {len(nondigits)}')
print(f'count of white_space is {len(white_space)}')
print(f'count of words is {len(words)}')

