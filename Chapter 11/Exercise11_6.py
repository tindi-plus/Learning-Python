# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:36:54 2021.

Recursive Fibonacci numbers implementation

@author: Tindi.Sommers
"""

calls = 0 # keep track of the number of calls to the fibonacci function

def fibonacci(n):
    """A function for generating the nth fibonacci number"""
    global calls
    calls += 1
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
   for i in range(10):
       print(i, fibonacci(i))
       print('The number of calls to fibonacci function is:', calls)