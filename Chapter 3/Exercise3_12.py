# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:45:30 2020

Palindromes (characters that read the same forward and backward)

@author: Tindi.Sommers
"""

num1 = input('Input the number you want to check for palindrome: ')
num = int(num1)
item = [] #an empty list to hold the separated digits
power = len(num1) - 1

for i in range(len(num1) - 1):
    if power == 1:
        firstDigit = num // 10 ** power
        item.append(firstDigit)
        item.append(num % 10)
    else:
        firstDigit = num // 10 ** power
        item.append(firstDigit)
        num = num - (num // 10 ** power) * 10 ** power
        power -= 1
    
print(item)

for i in range(1, len(item) + 1):
    if item[i - 1] == item[len(item) - i]:
        print('check')
    else:
        print(num1,'is not a palindrome')
        break
        
    
    if i == len(item) // 2:
        print(num1,'is a palindrome.')
        break
        
    
    