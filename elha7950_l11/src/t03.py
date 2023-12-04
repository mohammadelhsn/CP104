"""
-------------------------------------------------------
Lab 11, Task 3

Description: 
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import print_matrix_num, generate_matrix_num

# Get a matrix

matrix = generate_matrix_num(3, 4, -10, 10, "float")

# Call the function, Output results

result = print_matrix_num(matrix, 'float')

