# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:14:54 2020

Palindrome Tester

@author: Tindi.Sommers
"""

text = input("Enter the text you want to test if it is a palindrome: ")

text.lower()

reversed_text = text[::-1]

if reversed_text == text:
    print(f'{text} is a palindrome')
else:
    print(f'{text} is not a palindrome')
