# https://www.codewars.com/kata/complementary-dna/train/python
def DNA_strand(dna):
    result = ""
    for elem in dna:
        print(elem)
        if elem == "A":
            result += "T"
        elif elem == "T":
            result += "A"
        elif elem == "G":
            result += "C"
        elif elem == "C":
            result += "G"
    return result
