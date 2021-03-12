# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:25:38 2021.

Creating pig latin from English

@author: Tindi.Sommers
"""

import re

sentence = input('Input the phrase you want to change to pig latin: ')
print()

# tokenize the sentence
tokens = re.split(' ', sentence)
# generate the pig English
for word in tokens:
    if word[0] in 'aieou':
        print(word + 'ay', end=' ')
    else:
        first_letter = re.search('[a-zA-Z]', word)
        word = re.sub('[a-zA-Z]', '', word, count=1)
        word = word + first_letter.group() + 'ay'
        print(word, end=' ')
print