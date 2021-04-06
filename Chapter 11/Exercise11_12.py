# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:07:46 2021.

Towers of Hanoi

@author: Tindi.Sommers
"""

def hanoi(number, start, temp, stop):
    """Algorithm for the tower of hanoi,"""
    
    if number == 1:
        print(f'Move from {start} to {stop}')
        return
        
    hanoi(number - 1, start, stop, temp)
    print(f'Move from {start} to {stop}')
    hanoi(number - 1, temp, start, stop)


if __name__ == '__main__':
    
    hanoi(5, 1, 2, 3)