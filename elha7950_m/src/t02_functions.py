"""
-------------------------------------------------------
Midterm B Task 2 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""


def categorize(strokes):
    """
    -------------------------------------------------------
    Determines the golf skill rating given number of strokes to complete 18 holes.
        If strokes are 70 or less, the rating is "Grandmaster".
        If strokes are 85 or less, the rating is "Master".
        If strokes are 100 or less, the rating is "Professional".
        If strokes are greater than 100, the rating is "Amateur".
        If points is less than 0, return "Error"
    Must use a fallthrough algorithm.
    Use: rating = categorize(strokes)
    -------------------------------------------------------
    Parameters:
        strokes - strokes to complete 18 holes of golf (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        category - description of skill rating (str)
    -------------------------------------------------------
    """
    category = ""
    if (strokes < 0):
        category = "Error"
    elif (strokes <= 70):
        category = "Grandmaster"
    elif (strokes <= 85):
        category = "Master"
    elif (strokes <= 100):
        category = "Professional"
    else:
        category = "Amateur"

    # your code here

    return category
