# https://www.codewars.com/kata/find-the-unknown-digit/train/python
# much cleaner version of solving the problem

import re
def solve_runes(runes):
    print( "input: ", runes)       
    # ignore all the duplicates which already appear in the runes
    for i in sorted(set('0123456789')-set(runes)):
        new_runes = runes.replace("?", str(i))
        # check for zero trailing
        if re.search(r'([^\d]|\b)0\d+', new_runes):
          continue
        lhs, rhs = new_runes.split("=")
        if eval(lhs) == eval(rhs):
            return int(i)
    return -1
