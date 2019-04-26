# https://www.codewars.com/kata/array-dot-diff/train/python?

def array_diff(a, b):
    """
    remove duplicat of a in b
    """
    result =[]
    for i in a:
        if i not in b:
            result.append(i)      
    return result
