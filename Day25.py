# https://www.codewars.com/kata/valid-braces/train/python?



def validBraces(string):
    print(string, len(string))
    open_bracket = ["(","[","{"]
    closing_bracket =[")","]","}"]
    result = False
    if len(string)%2 == 0:
        mitte = int(len(string)/2)
        for i in range(0, mitte):
            print(string[i],"and ", string[len(string)-i-1])
            if string[i]  in open_bracket:
                position = open_bracket.index(string[i])
                print(position)
                print("closing should be: ", closing_bracket[position])
                print(" closing actual: ", string[len(string)-i-1])
                if closing_bracket[position] == string[len(string)-i-1]:
                    print("yes")
                    result = True
            else:
                result = False
    return result
