"""
-------------------------------------------------------
Lab 11, Task 12

Description: 
    Returns whether word is on the diagonal of a square matrix
    of characters.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import find_word_diagonal

# Define matrix

matrix = [['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']]

# Call the function

result = find_word_diagonal(matrix, "cog")

# Output result

print(result)
