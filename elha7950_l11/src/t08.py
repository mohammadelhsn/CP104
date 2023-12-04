"""
-------------------------------------------------------
Lab 11, Task 8

Description: 
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import find_less

# Define matrix

matrix = [[8, 2, -3], [7, 4, 4], [-2, -1, 0], [-1, -6, 2]]

# Call the function

result = find_less(matrix, 100)

# Output result

print(result)
