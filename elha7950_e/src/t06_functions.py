"""
-------------------------------------------------------
Exam Task 6 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""


def multiply_list(values):
    """
    -------------------------------------------------------
    Multiplies the value of each element of values by its index.
    Use: multiply_list(values)
    -------------------------------------------------------
    Parameters:
        values - list of elements to multiply (list of int)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        None
    -------------------------------------------------------
    """

    # Your code here

    for i in range(len(values)):
        values[i] = values[i] * i
    return
