"""
-------------------------------------------------------
Assignment 7, Task 4

Description: 
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
# Imports

from functions import list_subtract

# Call the function

result = list_subtract([5, 5, 4, 5], [5])

# Output results

print(result)
