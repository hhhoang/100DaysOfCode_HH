# https://www.codewars.com/kata/meeting/train/python
# string manipulation, sort alphabetic

import pandas as pd
def meeting(s):
    meet = pd.DataFrame(columns=['lastName', 'firstName'])
    for i in s.split(';'):
        x = i.split(':')
        meet = meet.append({'lastName': x[1].upper(), 'firstName': x[0].upper()}, ignore_index=True)
    meet = meet.sort(['lastName', 'firstName'])
    result = ""
    for index, row in meet.iterrows():
        result += str("(" + row[0] + ", " + row[1] + ")")
    return result
