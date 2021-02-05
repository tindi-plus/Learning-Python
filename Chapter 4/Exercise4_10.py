# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:50:06 2020

@author: Tindi.Sommers
"""

import random
game_status = 'PLAY'
while game_status == 'PLAY':
    number = random.randrange(1, 1000)
    guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
    while guess != number:
        if guess < number:
            print('Guess too low, try again')
        else:
            print('Guess too high, try again')
        guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
    print('Congratulations! You guessed the number.')
    continuation = input('Do you want play again? yes / no : ')
    if continuation == 'no' or continuation == 'No':
        game_status = 'STOP'
print('Thank you for playing my game with me.')