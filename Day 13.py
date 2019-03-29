# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:16:32 2019

@author: DEHHOAN2
"""

# https://www.codewars.com/kata/greed-is-good/train/python


"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450

"""
import numpy as np

def score(dice):
    num = (1,2,3,4,5,6)
    points_if_three = (1000, 200, 300, 400, 500, 600)
    points_if_one = (100, 0, 0 , 0, 50, 0)
    result = 0
    if len(dice) == 5:
        # count occurences of item
        dice_dict = dict((x,dice.count(x)) for x in set(dice))
        for k, v in dice_dict.items():
            if k in num:
                if v >= 3:
                    result += points_if_three[num.index(k)] + points_if_one[num.index(k)]*(v-3)
                elif 0 < v < 3:
                    result += points_if_one[num.index(k)]*v
            else:
                print("out of bound")        
    else:
        print("not a five dice")
    return result
#score([2, 3, 4, 6, 2]) # 0
#score([1, 1, 1, 3, 3]) # 1000
#score([2, 2, 2, 3, 3]) # 200
score([1, 1, 1, 1, 3]) # 1100
score([1, 1, 1, 1, 5]) # 1150
score([3, 5, 5, 5, 5]) # 550