"""
-------------------------------------------------------
Lab 11, Task 4

Description: 
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import generate_matrix_char, print_matrix_char

# Generate a matrix

matrix = generate_matrix_char(3, 4)

# Call the function, Output result

print_matrix_char(matrix)