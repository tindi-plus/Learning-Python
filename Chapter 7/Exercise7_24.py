# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:15:43 2021
The knight tour on a chess board
@author: Tindi.Sommers
"""

import numpy as np

# the chess board
board = np.full((8, 8), 0)
# horizontal steps to take for each move
horizontal = np.array([2, 1, -1, -2, -2, -1, 1, 2])
# vertical steps for each move
vertical = np.array([-1, -2, -2, -1, 1, 2, 2, 1])


# current position on the board
current_row = 0
current_col = 0
# count of moves
count = 0

for i in range(64):
    # attempt to play each knight move
    for j in range(8):
        # check that the move wont take the knight off the board
        if current_row + horizontal[j] in range(8) and current_col + vertical[j] in range(8):
            if board[current_row + horizontal[j], current_col + vertical[j]] == 0:
                current_row += horizontal[j]
                current_col += vertical[j]
                count += 1
                board[current_row, current_col] = count
                print(board)
                print()
                # break

print(count)
