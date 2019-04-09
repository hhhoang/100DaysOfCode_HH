# Social Golfer Problem Validator
# https://www.codewars.com/kata/social-golfer-problem-validator/train/python
"""
A group of N golfers wants to play in groups of G players for D days in such a way that no golfer plays more than once with any other golfer. For example, for N=20, G=4, D=5, the solution at Wolfram MathWorld is

 Mon:    ABCD    EFGH    IJKL    MNOP    QRST
 Tue:    AEIM    BJOQ    CHNT    DGLS    FKPR
 Wed:    AGKO    BIPT    CFMS    DHJR    ELNQ
 Thu:    AHLP    BKNS    CEOR    DFIQ    GJMT
 Fri:    AFJN    BLMR    CGPQ    DEKT    HIOS
Write a function that validates a proposed solution, a list of list of strings, as being a solution to the social golfer problem. Each character represents a golfer, and each string is a group of players. Rows represent days. The solution above would be encoded as:

 [
  ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
  ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
  ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
  ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
  ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
 ]
You need to make sure (1) that each golfer plays exactly once every day, (2) that the number and size of the groups is the same every day, and (3) that each player plays with every other player at most once.

So although each player must play every day, there can be particular pairs of players that never play together.

It is not necessary to consider the case where the number of golfers is zero; no tests will check for that. If you do wish to consider that case, note that you should accept as valid all possible solutions for zero golfers, who (vacuously) can indeed play in an unlimited number of groups of zero.
"""

def valid(a):
    result = 0
    players_per_day = []
    groups = []
    group_len = []
    groups_len_per_day = []
    for day in a:
        if ''.join(sorted(''.join(day))) not in players_per_day:
            players_per_day.append(''.join(sorted(''.join(day))))
        if len(day) not in groups_len_per_day:
            groups_len_per_day.append(len(day))
        for group in day:
            if len(group) not in group_len:
                group_len.append(len(group))
            groups.append(group)

    # each golfer plays exactly once every day
    if len(players_per_day) != 1:
        result += 1

    # number and size of groups the same every day
    if len(groups_len_per_day) != 1 or len(group_len) != 1:
        result += 1

    # each player plays with every other at most once
    for i in range(len(groups)):
        for j in range(len(groups)):
            if j != i:
                intersection = set(groups[i]).intersection(set(groups[j])) 
                if len(intersection) >= 2:
                    result += 1
    if result == 0:
        return True
    else:
        return False
    


