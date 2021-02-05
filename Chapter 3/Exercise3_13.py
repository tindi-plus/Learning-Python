# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:17:19 2020

Calculating factorials

@author: Tindi.Sommers
"""

number = input("""Enter the number you want to find the factorial of.
                   Positive integers only: """)

numval = int(number)

factorial = 1

while numval > 1:
    factorial *= numval
    numval -= 1
print(f'{number}! is {factorial}')
        
