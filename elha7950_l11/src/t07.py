"""
-------------------------------------------------------
Lab 11, Task 7

Description: 
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import find_position

# Define matrix

matrix = [[-6, 5, 7], [3, -6, -2], [9, -8, -7], [0, -7, -6]]

# Call the function

result = find_position(matrix)

# Output result

print(result)
