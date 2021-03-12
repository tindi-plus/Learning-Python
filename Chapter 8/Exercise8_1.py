# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:45:21 2021.

Printing a check amount

@author: Tindi.Sommers
"""

check_amount = input('Input the check amount you want to print: ')
float_amount = float(check_amount)
print(f'{float_amount:*>10,.2f}')
print(f'{"-" * 10}')
print('0123456789')
