"""
-------------------------------------------------------
Lab 9, Task 4

Description:
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports

from functions import validate_code

# Call the function

result = validate_code('BFG9000x7')

# Output results

print(result)
