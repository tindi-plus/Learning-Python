# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:14:06 2020

computer assisted instruction in mathematics

@author: Tindi.Sommers
"""
import random
import math

def single_random():
    """function for generating single digit random numbers"""
    x = random.randrange(10)
    y = random.randrange(10)
    return x, y

def double_random():
    """function for generating double digit random numbers"""
    x = random.randrange(5, 100)
    y = random.randrange(5, 100)
    return x, y

dificulty_level = int(input('Select your dificulty level: 1 or 2? :'))

while dificulty_level not in (1, 2):
    print("""Please choose dificulty level 1 by pressing 1
          Choose dificulty level 2 by pressing 2""")
          
    dificulty_level = int(input('Select your dificulty level: 1 or 2? : '))

if dificulty_level == 1:
    print('Welcome to math practice! You have chosen dificulty level 1.')
    
    proceed = 'yes'
    while proceed == 'yes' or proceed == 'Yes':
        
        numbers = single_random()
        answer = int(input(f'How much is {numbers[0]} times {numbers[1]}? : '))
        if answer == math.prod(numbers):
            print('Very Good!!')
        else:
            while answer != math.prod(numbers):
                print('No. Please, try again')
                answer = int(input(f'How much is {numbers[0]} times {numbers[1]}? : '))
                
        proceed = input('Would you like to proceed? yes / no ? : ')
        
elif dificulty_level == 2:
    print('Welcome to math practice! You have chosen dificulty level 2.')
    
    proceed = 'yes'
    while proceed == 'yes' or proceed == 'Yes':
        
        numbers = double_random()
        answer = int(input(f'How much is {numbers[0]} times {numbers[1]}? : '))
        if answer == math.prod(numbers):
            print('Very Good!!')
        else:
            while answer != math.prod(numbers):
                print('No. Please, try again')
                answer = int(input(f'How much is {numbers[0]} times {numbers[1]}? : '))
                
        proceed = input('Would you like to proceed? yes / no ? : ')
    
        