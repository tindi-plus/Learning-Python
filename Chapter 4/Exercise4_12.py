# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:11:09 2020

The race of the turtoise and the Hare.

@author: Tindi.Sommers
"""

import random

T_pos = 1  # the tortoise should start the race at track 1
H_pos = 1  # the hare should also start the race at track 1


def modifyT(step):
    global T_pos
    T_pos = step


def modifyH(step):
    global H_pos
    H_pos = step


def race_track():
    """race_track displays the race track and the positions of the racers"""
    for i in range(1, 71):
        if i == T_pos and i == H_pos and i == 1:
            print('START', end=' ')
        elif i == T_pos and i == H_pos:
            print('OUCH', end=' ')
        elif i == T_pos:
            print('T', end=' ')
        elif i == H_pos:
            print('H', end=' ')
        else:
            print('*', end=' ')


def move_left(args, step):
    """function for moving a racer to the left"""
    if args - step <= 0:
        args = 1
        return args
    else:
        args -= step
        return args


def move_right(args, step):
    """function for moving the racer to the right"""
    args += step
    return args


def H_move():
    """function for moving the hare"""
    move = random.randrange(1, 11)
    if 1 <= move <= 2: #no movement for the hare
        modifyH(move_right(H_pos, 0))
    elif 3 <= move <= 4:
        modifyH(move_right(H_pos, 9)) #move 9 steps to the right
    elif move == 5:
        modifyH(move_left(H_pos, 12)) #move 12 steps to the left
    elif 6 <= move <= 8:
        modifyH(move_right(H_pos, 1)) #move 1 step right
    else:
        modifyH(move_left(H_pos, 2)) #move 2 steps left

def T_move():
    """function for moving the tortoise"""
    move = random.randrange(1, 11)
    if 1 <= move <= 5:
        modifyT(move_right(T_pos, 3)) #move right 3 steps
    elif 6 <= move <= 7:
        modifyT(move_left(T_pos, 6)) #move left 6 steps
    else:
       modifyT(move_right(T_pos, 1)) #move right 1 step


race = 'ON' # status of the race
print('BANG!!!\nAND THEY ARE OFF!!')


# let the race begin!!

while race == 'ON':  # while game is on
    H_move()
    T_move()
    race_track()
    #check if there is any winner
    if T_pos >= 70:
        print('TORTOISE WINS!!! YAY!!!')
        race = 'END'
    elif H_pos >= 70:
        print('Hare Wins. Yuck!')
        race = 'END'
    elif T_pos >= 70 and H_pos >= 70:
        print('There is a tie!')
        race = 'END'
