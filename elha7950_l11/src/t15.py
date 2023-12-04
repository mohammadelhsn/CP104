"""
-------------------------------------------------------
Lab 11, Task 15

Description: 
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import matrix_equal

# Define matrices

matrix1 = [['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']]
matrix2 = [['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']]

# Call the function

result = matrix_equal(matrix1, matrix2)

# Output result

print(result)
