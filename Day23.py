# https://www.codewars.com/kata/is-a-number-prime/train/python?
# prime number

def is_prime(num):
    """
    define if integer is a prime
    """

    if num <= 1:
         return False
    else:
        for i in range(2, num):
            if num%i == 0:
                return False
                break
        else:
            return True
        
