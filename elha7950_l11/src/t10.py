"""
-------------------------------------------------------
Lab 11, Task 10

Description: 
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import find_word_horizontal

# Define matrix

matrix = [['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']]

# Call the function

result = find_word_horizontal(matrix, "dog")

# Output result

print(result)
