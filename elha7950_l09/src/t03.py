"""
-------------------------------------------------------
Lab 9, Task 3

Description:
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports

from functions import parse_code

# Call the function

result = parse_code('ATV3482S14')

# Output results

print(result)
