"""
-------------------------------------------------------
Lab 5, Task 5

Description:
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports

from functions import is_leap

# Call the function

result = is_leap(1999)

# Output results

print(result)
