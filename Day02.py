#A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. 
#Each book has a code c of 3, 4, 5 or more capitals letters. 
#The 1st letter of a code is the capital letter of the book category. 
#In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.
#For example an extract of one of the stocklists could be:
#L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
#You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
#M = {"A", "B", "C", "W"} 
#and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.
#For the lists L and M of example you have to return the string (in Haskell/Clojure a list of pairs):
#(A : 20) - (B : 114) - (C : 50) - (W : 0)
#where A, B, C, W are the categories, 20 is the sum of the unique book of category A, etc.
#If L or M are empty return string is "" (Clojure should return an empty array instead).
#Note:In the result codes and their values are in the same order as in M.
#https://www.codewars.com/kata/help-the-bookseller/train/python

def stock_list(listOfArt, listOfCat):
    if len(listOfArt) == 0:
        return ""
    elif len(listOfCat) == 0:
        return ""
    else:
        resultString = "" 
        for i in listOfCat:
            value = 0
            for j in listOfArt:
                if j.startswith(i):
                    value += int(j.split(" ")[1])
            resultString += "(" + i + " : " + str(value) + ") - "
        resultString = resultString[:-3]
        return resultString

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print("Actual:   " + stock_list(b, c))
print("Expected: (A : 200) - (B : 1140)")
