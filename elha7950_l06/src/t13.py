"""
-------------------------------------------------------
Lab 6, Task 13

Description: 
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
# Imports

from functions import lumber

# Call the function, Output results

lumber(2, 10, 2, 2, 12, 2)
