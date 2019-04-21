# https://www.codewars.com/kata/after-midnight/train/python?
"""
Write a function that takes a negative or positive integer, 
which represents the number of minutes before (-) or after (+) Sunday midnight, 
and returns the current day of the week and the current time in 24hr format ('hh:mm') as a string.
"""

def day_and_time(mins):
    dayspos = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    print(mins)
    minutes, hours_final, days_final = get_min_hour_day(mins)
    return "{} {}:{}".format(dayspos[days_final], str(hours_final).zfill(2),str(minutes).zfill(2))
def get_min_hour_day(mins, clock_wise=True):
    hours, minutes = divmod(mins, 60)
    days, hours_final = divmod(hours, 24)
    days_final = days%7
    print(days_final, days, hours_final, hours, minutes)
    return(minutes, hours_final, days_final)
