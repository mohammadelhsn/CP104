"""
-------------------------------------------------------
Lab 8, Task 15

Description: 
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports

from functions import symmetric_difference

# Call the function

result = symmetric_difference([10, 3, 10, 3, 1], [8, 2, 7, 3, 6, 10, 32, 99])

# Output results

print(result)
