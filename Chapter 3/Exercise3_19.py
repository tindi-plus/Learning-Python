# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:57:20 2020
finding the sides of pythagorean tripple
@author: Tindi.Sommers
"""

for side1 in range(1,20):
    for side2 in range(1,20):
        for side3 in range(1,20):
            if(side1 **2 + side2 **2 == side3 **2):
                print('I have found a pythagorean tripple:', side1, side2, side3 )