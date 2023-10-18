"""
-------------------------------------------------------
Lab 5, Task 2

Description:
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports

from functions import get_weight

# Constants


result = get_weight(5)
print(result[1])
