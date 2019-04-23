# https://www.codewars.com/kata/tribonacci-sequence/train/python?
# tribonacci- brother if fibonacci:)
def tribonacci(signature, n):
    """
    function returns the sequence of tribonacci number which is the sum of the last 3 numbers. Sequence starts with signature, which includes 3 first numbers.
    """
    result =[]
    if 0 < n < 3:
        for i in range(n):
            result.append(signature[i])
    elif n >= 3:
        result[0:2] = signature
        for i in range(3, n):
            result.append(result[i-1] + result[i-2] + result[i-3])
    return result
  
