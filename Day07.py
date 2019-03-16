# https://www.codewars.com/kata/two-joggers/python
# Bob and Charles are meeting for their weekly jogging tour.
# They both start at the same spot called "Start" and they each run a different lap,
# which may (or may not) vary in length.
# Since they know each other for a long time already, they both run at the exact same speed.
# Your job is to complete the function nbrOfLaps(x, y) that, given the length of the laps for Bob and Charles,
# finds the number of laps that each jogger has to complete before they meet each other again, at the same time,
# at the start.


def nbr_of_laps(x, y):
    gcd = computeGCD(x,y)
    return (y/gcd, x/gcd)


def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd