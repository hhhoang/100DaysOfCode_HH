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
        #print("iterate value in input: ", new_runes)
        lhs, rhs = new_runes.split("=")
        
        if "+" in lhs:
            lhs_1, lhs_2 = lhs.split("+")
            if len(list(lhs_1)) > 1 and lhs_1.startswith("0"):
                print("zero trailing: ", lhs_1)
                pass
            elif len(list(lhs_2)) > 1 and lhs_2.startswith("0"):
                print("zero trailing: ", lhs_2)
                pass   
            elif len(list(rhs)) > 1 and rhs.startswith("0"):
                print("zero trailing: ", rhs)
                pass                
            elif int(lhs_1) + int(lhs_2) == int(rhs):
                result.append(i)
        elif "*" in lhs:
            lhs_1, lhs_2 = lhs.split("*")
            if len(list(lhs_1)) > 1 and lhs_1.startswith("0"):
                print("zero trailing: ", lhs_1)
                pass
            elif len(list(lhs_2)) > 1 and lhs_2.startswith("0"):
                print("zero trailing: ", lhs_2)
                pass   
            elif len(list(rhs)) > 1 and rhs.startswith("0"):
                print("zero trailing: ", rhs)
                pass             
            elif int(lhs_1) * int(lhs_2) == int(rhs):
                result.append(i)            
        # TODO: issue with negative number as "-" in split
        elif "-" in lhs:
            occurence = [m.start() for m in re.finditer('-',lhs)]
            if len(occurence) == 2:
                lhs_1, lhs_2 = lhs[:occerence[1], lhs[occerence[1]+1:]
            else:
                lhs_1, lhs_2 = lhs.split("-")            
            if len(list(lhs_1)) > 1 and lhs_1.startswith("0"):
                print("zero trailing: ", lhs_1)
                pass
            elif len(list(lhs_2)) > 1 and lhs_2.startswith("0"):
                print("zero trailing: ", lhs_2)
                pass   
            elif len(list(rhs)) > 1 and rhs.startswith("0"):
                print("zero trailing: ", rhs)
                pass             
            elif int(lhs_1) - int(lhs_2) == int(rhs):
                result.append(i)            
    
    print("results are: ", result)
    # Result cannot be identical to elements in the original runes
    for i in result:
        if str(i) in runes:
            print(result)
            result.remove(i)
    if len(result) == 0:
        result = -1
    else:
        result = result[0]
    print("final result is: ", result)
    return result
