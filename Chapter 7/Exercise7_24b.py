# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:38:11 2021.

Knight tour, the updated version with heuristics
@author: Tindi.Sommers
"""

import numpy as np

# the chess board
board = np.full((8, 8), 0)
# horizontal steps to take for each move
horizontal = np.array([2, 1, -1, -2, -2, -1, 1, 2])
# vertical steps for each move
vertical = np.array([-1, -2, -2, -1, 1, 2, 2, 1])

# create and manage an accessibility board
accessibility = np.full((8, 8), 0)


def update_access():
    """Update the accessbility baord."""
    global accessibility, vertical, horizontal, board

    # iterate through all the squares of the accessibility board
    for row in range(8):
        for col in range(8):
            count = 0
            for k in range(8):
                # check that the move is not outside the board
                if row + horizontal[k] in range(8) and col + vertical[k] in range(8):
                    if board[row + horizontal[k], col + vertical[k]] == 0:
                        count += 1
            accessibility[row, col] = count
    print(accessibility)
    print()


# current position on the board
current_row = 3
current_col = 4
# count of moves
count = 0

# update the accessibility board
update_access()


# select the least accessibility
def select_access():
    """Return the least accessibility for a square."""
    global board, current_row, current_col, accessibility
    # a dictionary for holding the moves and accessibility
    access = {}
    # check each possible move
    for i in range(8):
        r = current_row + horizontal[i]
        c = current_col + vertical[i]
        # confirm that the move is not outside the board
        if r in range(8) and c in range(8):
            # confirm the knight has not moved there before
            if board[r, c] == 0:
                access[accessibility[r, c]] = i
    # find the lowest accessibility
    if len(access) != 0:
        lowest_access = min(access.keys())
        # return the move with the lowest accessibility
        return access[lowest_access]
    else:
        return None


for i in range(63):
    # get the move with the least accessibility
    move = select_access()
    if move is not None:
        current_row += horizontal[move]
        current_col += vertical[move]
        board[current_row, current_col] = count + 1
        count += 1
        update_access()


print(board)
print(count)
