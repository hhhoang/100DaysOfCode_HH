# Find the unknown digit
# https://www.codewars.com/kata/find-the-unknown-digit/train/python

import re

def solve_runes(runes):
    print( "input: ", runes)
    if "--" in runes:
        runes = runes.replace("--", "+")        
    result = []
    for i in range(10):
        new_runes = runes.replace("?", str(i))
        lhs, rhs = new_runes.split("=")
        
        if "+" in lhs:
            lhs_1, lhs_2 = lhs.split("+")
            if check_trailing_zero(lhs_1) == True or check_trailing_zero(lhs_2) == True or check_trailing_zero(rhs) == True:
                pass
            elif int(lhs_1) + int(lhs_2) == int(rhs):
                result.append(i)
        elif "*" in lhs:
            lhs_1, lhs_2 = lhs.split("*")
            if check_trailing_zero(lhs_1) == True or check_trailing_zero(lhs_2) == True or check_trailing_zero(rhs) == True:
                pass             
            elif int(lhs_1) * int(lhs_2) == int(rhs):
                result.append(i)            
        # TODO: issue with negative number as "-" in split
        elif "-" in lhs and "-" != list(lhs)[0]:
            lhs_1, lhs_2 = lhs.split("-")            
            if check_trailing_zero(lhs_1) == True or check_trailing_zero(lhs_2) == True or check_trailing_zero(rhs) == True:
                pass             
            elif int(lhs_1) - int(lhs_2) == int(rhs):
                result.append(i)            
        elif "-" in lhs and "-" == list(lhs)[0]:
            occurence = [m.start() for m in re.finditer('-',lhs)]
            lhs_1, lhs_2 = lhs[:occurence[1]], lhs[occurence[1]+1:]
            if check_trailing_zero(lhs_1) == True or check_trailing_zero(lhs_2) == True or check_trailing_zero(rhs) == True:
                pass
            elif int(lhs_1) - int(lhs_2) == int(rhs):
                result.append(i) 
                
    print("initial results are: ", result)
    # Result cannot be identical to elements in the original runes
    final_result = []
    for i in result:
        print("loop:", i)
        if str(i) not in runes:
            print("is not in rune: ", i)
            final_result.append(i)
    
    if len(final_result) == 0:
        result = -1
    else:
        result = final_result[0]
    print("final result is: ", result)
    return result


def check_trailing_zero(inp):
    if inp.startswith("-"):
        inp = inp[1:]
    else:
        inp = inp
    if len(inp) > 1 and inp.startswith("0"):
        return True
    else:
        return False
