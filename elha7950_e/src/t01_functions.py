"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""

# Imports

from math import floor

# Function


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """

    # Define variables

    count = 0
    ea = 0

    # your code here

    for num in values:
        if ((num % 2) == 0):
            count += 1
            ea += num
        else:
            continue

    if (count == 0):
        count = 1

    # Round down

    return floor(ea / count)
