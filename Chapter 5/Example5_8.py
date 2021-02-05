# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:48:07 2020

Sieve of Erastosthenes

@author: Tindi.Sommers
"""

# a 1000 element list

primes = [True] * 1000

# set all non-prime numbers to False

for i in range(2, len(primes)):
    if primes[i] is True:
        for j in range(i + 1, len(primes)):
            if primes[j] is True:
                if j % i == 0:
                    primes[j] = False

for i in range(2, len(primes)):
    if primes[i] is True:
        print(i, end=' ')

