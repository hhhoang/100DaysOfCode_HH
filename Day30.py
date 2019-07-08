# https://www.codewars.com/kata/century-from-year/train/python
# Given a year, return the century it is in.

def century(year):
    return (year // 100) + 1 if year % 100 != 0 else (year // 100)
