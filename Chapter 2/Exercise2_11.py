# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:07:52 2020
Splitting numbers into digits
@author: Tindi.Sommers
"""

number = input("Input the number you want to split: ")
numberInt = int(number)

numLen = len(number)

count = 0

"""while count < numLen:
    print(number[count], end =' ')
    count = count + 1"""

power = numLen - 1 #the power to which the numbers will be raised
for i in range(numLen - 1):
    if power == 1:
       print(numberInt // 10, end= ' ')
       print(numberInt % 10, end= ' ')
    else:
       print(numberInt // 10**power, end= ' ') 
       numberInt -= (numberInt // 10**power) * 10**power
       power -= 1
