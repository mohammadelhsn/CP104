"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""

# Imports

from math import floor

# Constants

DRY_DAYS = 4
DAMP_DAYS = 8
EXIT_NUM = -1

# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    # your code here

    dry_days = 0
    damp_days = 0
    wet_days = 0
    total = 0
    count = 0

    gettingInput = True

    while (gettingInput):
        rainfall_amt = int(input('Rainfall mm (-1 to stop): '))

        if (rainfall_amt == EXIT_NUM):
            gettingInput = False
            break
        elif (rainfall_amt < 4):
            dry_days += 1
        elif (rainfall_amt < 8):
            damp_days += 1
        else:
            wet_days += 1

        count += 1
        total += rainfall_amt
        continue

    average = floor(total / count)
    return (dry_days, damp_days, wet_days, average)
