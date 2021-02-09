# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:52:21 2021.

Two human players, Two dimensional Tic tac toe
@author: Tindi.Sommers
"""

import numpy as np

# a board for the tic tac toe
toe_board = np.full((3, 3), '')


def play(player):
    """
    Obtain player input from the player.

    Stores the input in the tic tac toe board.

    Parameters
    ----------
    player : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    move = input('Enter your move in the format a,b  ')
    position = [int(move[0]), int(move[2])]

    if player == 1:
        toe_board[position[0], position[1]] = 'X'
    elif player == 2:
        toe_board[position[0], position[1]] = 'O'

    print(toe_board)
    print()


def check_win():
    """
    Check if a player has won the game.

    Returns
    -------
    True if a player wins else returns False

    """
    for i in toe_board:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            print('The winner is Player One!')
            return True
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            print('The winner is Player Two!')
            return True

    for i in toe_board.T:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            print('The winner is Player One!')
            return True
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            print('The winner is Player Two!')
            return True
    if toe_board[0, 0] == 'X' and toe_board[1, 1] == 'X' and toe_board [2, 2] == 'X':
        print('The winner is Player One!')
        return True
    elif toe_board[0, 0] == 'O' and toe_board[1, 1] == 'O' and toe_board [2, 2] == 'O':
        print('The winner is Player Two!')
        return True
    if toe_board[0, 2] == 'X' and toe_board[1, 1] == 'X' and toe_board [2, 0] == 'X':
        print('The winner is Player One!')
        return True
    elif toe_board[0, 2] == 'O' and toe_board[1, 1] == 'O' and toe_board [2, 0] == 'O':
        print('The winner is Player Two!')
        return True
    return False


game_play = True  # if there is no winner yet

# Play the game
while game_play:
    player = 1
    play(player)
    if check_win():
        game_play = False
        break
    player = 2
    play(player)
    if check_win():
        game_play = False




