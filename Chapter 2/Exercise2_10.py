# -*- coding: utf-8 -*-
#Exercise 2.10
"""
Created on Tue Nov 24 12:02:02 2020
Receiving input from users and computing averages and maximum and minimum

@author: Tindi.Sommers
"""

#Get numbers from the users
value1 = float(input("Input your first Number: "))
value2 = float(input("Input your second Number: "))
value3 = float(input("Input your third Number: "))
value4 = float(input("Input your fourth Number: "))
print()

total = value1 + value2 + value3 + value4
average = total / 4
maximum = max(value1, value2, value3, value4) 
minimum = min(value1, value2, value3, value4)

print("The sum of the numbers is", total)
print("The average of the numbers is", average)
print("The largest number is", maximum)
print("The smallest number is", minimum)