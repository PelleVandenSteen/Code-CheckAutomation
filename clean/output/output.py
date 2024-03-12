Sure, here's a Python function that checks if a year is a leap year:

def is_leap_year(year):
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


This function takes a year as input and returns True if it is a leap year, and False otherwise. It uses the standard rules for determining leap years: a year is a leap year if it is divisible by 4, unless it is also divisible by 100, in which case it is only a leap year if it is also divisible by 400.