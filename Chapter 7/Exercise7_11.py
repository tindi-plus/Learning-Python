# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:42:46 2021.

Playing Tic Tac Toe against the computer
@author: Tindi.Sommers
"""

import numpy as np

# a board for the tic tac toe
toe_board = np.full((3, 3), '')

# let the player decide who will play first
first_play = input("""You are playing Tic Tac Toe against the computer.
Enter 'y' if you want to go first or 'n' for the computer to go first: """)


def comp_play(first_play):
    global toe_board
    if first_play == 'n':
        # if the center position is open, play there
        if toe_board[1, 1] == '':
            toe_board[1, 1] = 'X'
            print(toe_board)
            print()
            return
        play = True
        while play:
            # generate a position on the board
            x, y = (np.random.randint(0, 3), np.random.randint(0, 3))
            if toe_board[x, y] == '':
                toe_board[x, y] = 'X'
                print(toe_board)
                print()
                play = False
            else:
                continue
    else:
        # if the center position is open, play there
        if toe_board[1, 1] == '':
            toe_board[1, 1] = 'O'
            print(toe_board)
            print()
            return

        play = True
        while play:
            # generate a position on the board
            x, y = (np.random.randint(0, 3), np.random.randint(0, 3))
            if toe_board[x, y] == '':
                toe_board[x, y] = 'O'
                print(toe_board)
                print()
                play = False
            else:
                continue


def play():
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
    global first_play

    move = input('Enter your move in the format a,b  ')
    position = [int(move[0]), int(move[2])]

    if first_play == 'y':
        toe_board[position[0], position[1]] = 'X'
    elif first_play == 'n':
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
            if first_play == 'y':
                print('You are the winner!')
            else:
                print('The computer is the winner!')
            return True
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            if first_play == 'y':
                print('The computer is the winner!')
            else:
                print('You are the winner!')
            return True

    for i in toe_board.T:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            if first_play == 'y':
                print('You are the winner!')
            else:
                print('The computer is the winner!')
            return True
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            if first_play == 'y':
                print('The computer is the winner!')
            else:
                print('You are the winner!')
            return True
    if toe_board[0, 0] == 'X' and toe_board[1, 1] == 'X' and toe_board [2, 2] == 'X':
        if first_play == 'y':
            print('You are the winner!')
        else:
            print('The computer is the winner!')
        return True
    elif toe_board[0, 0] == 'O' and toe_board[1, 1] == 'O' and toe_board [2, 2] == 'O':
        if first_play == 'y':
            print('The computer is the winner!')
        else:
            print('You are the winner!')
        return True
    if toe_board[0, 2] == 'X' and toe_board[1, 1] == 'X' and toe_board [2, 0] == 'X':
        if first_play == 'y':
            print('You are the winner!')
        else:
            print('The computer is the winner!')
        return True
    elif toe_board[0, 2] == 'O' and toe_board[1, 1] == 'O' and toe_board[2, 0] == 'O':
        if first_play == 'y':
            print('The computer is the winner!')
        else:
            print('You are the winner!')
        return True
    return False


game_play = True  # if there is no winner yet

# Play the game
if first_play == 'y':
    while game_play:
        play()
        if check_win():
            game_play = False
            break
        comp_play(first_play)
        if check_win():
            game_play = False
elif first_play == 'n':
    while game_play:
        comp_play(first_play)
        if check_win():
            game_play = False
            break
        play()
        if check_win():
            game_play = False
