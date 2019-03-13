#https://www.codewars.com/kata/did-i-finish-my-sudoku/train/python



import numpy as np

def done_or_not(board): #board[i][j]
  # your solution here
  if len(board) == 9:
      sL = [1,2,3,4,5,6,7,8,9]
      # rows
      row_result = check_if_valid(board)
       # columns
      boardTranspose = np.array(board).T.tolist()
      column_result = check_if_valid(boardTranspose)
       # sub matrix
      square_result = True 
      # return 'Finished!'
      # or return 'Try again!'
      if row_result == True and column_result == True and square_result == True:
            return "Finished!"
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
