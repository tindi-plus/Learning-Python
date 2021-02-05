# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:04:16 2021
Phone number generator from words
@author: Tindi.Sommers
"""

# Request for the word you want to generate a phone number from

word = input('Enter a 7 letter word to generate a phone number: ')

# Standard letters on a phone key pad
all_letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'prs', 'tuv', 'wxy']

num_all = '23456789'

new_num = ''  # teh new number to be generated

# Pick a number based on the letter of the supplied word
for letter in word:
    for index, key in enumerate(all_letters):
        if letter in key:
            new_num += num_all[index]

print(new_num)
