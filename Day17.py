# https://www.codewars.com/kata/unlucky-days/train/python
# find number of Friday 13 of given year.
# using weekday() return 0 (Mon) to 6 (Sun)


import datetime
def unlucky_days(year):
    result = 0
    for i in range(1, 13):
        if datetime.date(year, i, 13).weekday() == 4:
            result += 1
    return result
