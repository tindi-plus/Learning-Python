# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:36:54 2021.

Recursive Fibonacci numbers implementation with memoization

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

# create a memoize function to memoize the fibonacci function
def memoize(f):
    """wrap the f fuction in the helper function."""
    cache = {}  # a dictionary for storing the cache for the help function
    
    def helper(*args):
        """Check if information is in cache, and return the information, else
        call function f and store the information in the cache"""
        
        if args in cache:
            return cache[args]
        cache[args] = f(*args)
        return cache[args]
    
    return helper


if __name__ == '__main__':  # if this is executed as a script
   fibonacci = memoize(fibonacci) # create a memoized version of fibonacci
   
   
   for i in range(100):
       print(i, fibonacci(i))
       print('The number of calls to fibonacci function is:', calls)