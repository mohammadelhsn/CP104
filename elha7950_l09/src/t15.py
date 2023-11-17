"""
-------------------------------------------------------
Lab 9, Task 15

Description: 
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
# Imports

from functions import calculate

# Call the function

result = calculate('5 + 4')

# Output results

print(result)
