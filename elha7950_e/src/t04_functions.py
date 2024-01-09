"""
-------------------------------------------------------
Exam Task 4 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""

from math import ceil

# Constants

SPACE_CHAR = " "
CHAR = "#"


def draw_x(height):
    """
    -------------------------------------------------------
    Prints a X shape height characters high.
    Use: draw_x(height)
    -------------------------------------------------------
    Parameters:
        height - maximum height in characters of X shape (int >= 3)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        None
    -------------------------------------------------------
    """

    # Your code here
    spaces = height
    if ((height % 2) == 0):
        string = ""
        middle_ln = ceil(height / 2) - 1
        second_middle_ln = middle_ln + 1
        spaces_after = 2
        spaces_before = height - 2
        for i in range(height):
            if (i < middle_ln):
                string = (f"{CHAR}{SPACE_CHAR * spaces_before}{CHAR}")
                print(f'{string:^10s}')
                spaces_before -= 2
            elif (i == middle_ln or i == second_middle_ln):
                string = f"{CHAR*2}"
                print(f'{string:^10s}')
            else:
                string = f"{CHAR}{SPACE_CHAR * spaces_after}{CHAR}"
                print(f'{string:^10s}')
                spaces_after += 2
    else:
        string = ""
        middle_ln = ceil(height / 2) - 1
        spaces_after = 1
        spaces_before = height - 2
        for i in range(height):
            if (i < middle_ln):
                string = (f"{CHAR}{SPACE_CHAR * spaces_before}{CHAR}")
                print(f'{string:^11s}')
                spaces_before -= 2
            elif (i == middle_ln):
                string = f"{CHAR}"
                print(f'{string:^11s}')
            else:
                string = f"{CHAR}{SPACE_CHAR * spaces_after}{CHAR}"
                print(f'{string:^11s}')
                spaces_after += 2
    return
