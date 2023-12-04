"""
-------------------------------------------------------
Lab 11, Task 6

Description: 
    Returns statistics on a 2D list.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import matrix_stats

# Define a matrix

matrix = [[2, 0, -1, 1], [10, 4, -5, 9], [-6, 3, 6, 0]]

# Call the function

result = matrix_stats(matrix)

# Output result

print(result)
