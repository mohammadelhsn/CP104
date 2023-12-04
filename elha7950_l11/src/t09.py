"""
-------------------------------------------------------
Lab 11, Task 9

Description: 
    Count the number of appearances of the given character char
    in matrix.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import count_frequency

# Define matrix

matrix = [['g', 'h', 'a', 'd'], ['o', 't', 'n', 'd'], ['w', 'j', 't', 'c']]

# Call the function

result = count_frequency(matrix, "d")

# Output result

print(result)
