#Roman Numerals Encoder
#Create a function taking a positive integer as its parameter and returning a string 
#containing the Roman Numeral representation of that integer.
#Modern Roman numerals are written by expressing each digit separately starting with the left most digit 
#and skipping any digit with a value of zero. 
#In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
#2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#Example: solution(1000) # should return 'M'
#https://www.codewars.com/kata/roman-numerals-encoder/train/python

# credit to https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError ("expected integer")
    if not 0 < input < 4000:
        raise ValueError ("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)
