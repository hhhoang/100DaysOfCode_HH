#https://www.codewars.com/kata/did-i-finish-my-sudoku/train/python



# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:17:40 2019

@author: DEHHOAN2
"""

import numpy as np

def done_or_not(board): #board[i][j]
    # your solution here
    board_matrix = np.asmatrix(board)  
    if board_matrix.shape == (9,9):
          # rows
          row_result = check_if_valid(board)
           # columns
          boardTranspose = np.array(board).T.tolist()
          column_result = check_if_valid(boardTranspose)
           # sub matrix
    
          a1, a2, a3 = board_matrix[0:3,0:3], board_matrix[0:3,4:6], board_matrix[0:3,6:9]
          a4, a5, a6 = board_matrix[4:6,0:3], board_matrix[4:6,4:6], board_matrix[4:6,6:9]
          a7, a8, a9 = board_matrix[6:9,0:3], board_matrix[6:9,4:6], board_matrix[6:9,6:9]
          sub_board_array = [a1.A1, a2.A1, a3.A1, a4.A1,a5.A1, a6.A1, a7.A1, a8.A1, a9.A1]
          print(sub_board_array, 'square matrix')
          square_result = check_if_valid(sub_board_array)
          print(square_result)
          # return 'Finished!'
          # or return 'Try again!'
          if row_result == True and column_result == True and square_result == True:
                return "Finished"
          else:
                return "Try again!"
    else:
        return "Try again!"
def check_if_valid(inputList):
    sL = [1,2,3,4,5,6,7,8,9]
    result = 0
    for i in inputList:
        if len(i) != 9:
            result += 1
    else: 
        if all(elem in i  for elem in sL) == False:
            result += 1
    
    if result == 0:
        return True
    else:
        return False
