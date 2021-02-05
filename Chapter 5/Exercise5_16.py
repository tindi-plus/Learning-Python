# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:59:06 2021
Sorting letters and removing duplicates
@author: Tindi.Sommers
"""
import numpy as np

letters = ['c', 'd', 'e', 'a', 'c', 'b', 'e', 'f', 'f', 'e',
           'd', 'a', 'c', 'a', 'b', 'b', 'f', 'a', 'e', 'b']
letters_a = sorted(letters)
letters_b = sorted(letters, reverse=True)
letters_c = np.unique(letters)
print(letters_a, end='\n\n')
print(letters_b, end='\n\n')
print(letters_c, end='\n')
