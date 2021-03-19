# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:49:02 2021.

Solving mathematical word problems

@author: Tindi.Sommers
"""
import re

numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

operators = ['times', 'plus', 'minus', 'divide by']

problem = input('Input your math problem in words: ')
# convert all the inputs to lower case
problem_lower = problem.lower()
# split the problem into words and evaluate them
words = re.split(r'\s', problem_lower)

print(words)
# perform the math
if re.fullmatch('time[s]*', words[1]):
    ans = numbers[words[0]] * numbers[words[2]]
elif re.fullmatch('plus', words[1]):
    ans = numbers[words[0]] + numbers[words[2]]
elif re.fullmatch('minus', words[1]):
    ans = numbers[words[0]] - numbers[words[2]]
elif re.fullmatch(r'divideby', words[1] + words[2]):
    ans = numbers[words[0]] / numbers[words[3]]

print(f'{problem} is {ans}.')