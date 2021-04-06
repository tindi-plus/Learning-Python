# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 20:49:50 2021.

Recursive implementation of greatest common divisor

@author: Tindi.Sommers
"""

def gcd(x, y):
    """find the greatest common divisor for two numbers"""
    if y == 0:
        return x  # if y is zero, the gcd is x
    # return the gcd of y and the remainder of x divide by y. Note that x and
    # y are reversed for each recursive call
    return gcd(y, x % y)


if __name__ == '__main__':
    
    print(gcd(2, 3))
