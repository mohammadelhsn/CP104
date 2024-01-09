"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # Your code here

    lines = fh_in.readlines()
    matrix = []
    nums = []

    for line in lines:
        for num in line.strip().split(" "):
            nums.append(int(num))

    total = rows * cols

    index = 0

    if (total > len(nums)):
        for i in range(rows):
            row = []
            for i in range(cols):
                if (index > (len(nums) - 1)):
                    row.append(0)
                else:
                    row.append(nums[index])
                index += 1
            matrix.append(row)
    else:
        for i in range(rows):
            row = []
            for i in range(cols):
                if (index > (len(nums) - 1)):
                    row.append(0)
                else:
                    row.append(nums[index])
                index += 1
            matrix.append(row)

    return matrix
