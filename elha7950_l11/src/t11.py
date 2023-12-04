"""
-------------------------------------------------------
Lab 11, Task 11

Description: 
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all column that are equal to word.
    Returns an empty list if no column is equal to word.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import find_word_vertical

# Define matrix

matrix = [['c', 'd', 'b'], ['a', 'o', 'i'], ['t', 'g', 'g']]

# Call the function

result = find_word_vertical(matrix, "dog")

# Output result

print(result)
