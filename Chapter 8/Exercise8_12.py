# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:35:16 2021.

Creating scrambled text

@author: Tindi.Sommers
"""
import random
import re
word = input('Input the word you want to scramble: ')
first_letter = word[0]
last_letter = word[len(word) - 1]
middle = re.search(r'\w(\w+)\w', word)
middle_letters = middle.group(1)
print(middle_letters)
# shuffle the middle letters and then add the first and last letter to it
shuffled_list = list(middle_letters)
random.shuffle(shuffled_list)
for i in shuffled_list:
    first_letter += i

# append the last letter
first_letter += last_letter
print(first_letter)