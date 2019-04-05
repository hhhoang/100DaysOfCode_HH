# Tic-Tac-Toe Checker
# https://www.codewars.com/kata/tic-tac-toe-checker/train/python
"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""
import numpy as np

def isSolved(board):
    check_list = []
    board_listing = []
    # horizontal
    for i in list(board):
        check_list.append(i)
        for j in i:
            board_listing.append(j)
    # vertical
    for i in np.matrix(board).T.tolist():
        check_list.append(i)
    # diagonals
    check_list.append([r[i] for i, r in enumerate(board)])
    check_list.append([r[-i-1] for i, r in enumerate(board)])
    print(board_listing)
    result = 0

    if [1, 1, 1] in check_list:
        print('yes')
        result = 1
    elif [2, 2, 2] in check_list:
        result = 2
    elif 0 in board_listing:
        result = -1
    return result
