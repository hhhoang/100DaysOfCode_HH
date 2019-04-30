# https://www.codewars.com/kata/valid-braces/train/python?


def validBraces(string):
    print(string, len(string))
    result = False
    if len(string)%2 == 0:
        mitte = int(len(string)/2)
        for i in range(0, mitte):
            print(string[i],"and ", string[len(string)-i-1])
            if string[i] == string[len(string)-i-1]:
                result = True
    return result
