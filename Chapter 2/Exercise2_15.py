# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:28:31 2020
Sort numbers in descending order
@author: Tindi.Sommers
"""

#Get input from the user
value1 = int(input("Input the first number "))
value2 = int(input("Input the second number "))
value3 = int(input("Input the third number "))

myList = {} # a list for holding sone variabes

f = min(value1,value2,value3)
b = max(value1,value2,value3)

if f < value1 < b:
    myList = [f, value1, b]

elif f < value2 < b:
    myList = [f, value2, b]
    
elif f < value3 < b:
    myList = [f, value3, b]
    
print(myList)

