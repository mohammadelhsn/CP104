"""
-------------------------------------------------------
Lab 11, Task 1

Description: 
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import generate_matrix_num

# Call the function

matrix = generate_matrix_num(3, 4, -10, 10, "float")

# Output result

print(matrix)
