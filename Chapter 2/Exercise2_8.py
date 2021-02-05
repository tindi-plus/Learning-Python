# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:47:17 2020

@author: Tindi.Sommers
"""

#Table of Squares and Numbers
"""Creating a table that will display the squares and cubes of a number displayed in a table"""
#Print a header for the table
print('Number   ','Square   ','Cube')
for i in [0,1,2,3,4,5]:
    print(f'{i:>6}    {i**2:>6}    {i**3:>4}')