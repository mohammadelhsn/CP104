"""
-------------------------------------------------------
Assignment 2, Task 2

Description: 

-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

# Get user input

digit = int(input("Enter a positive digit number: "))

# Calculations, Define Constants

TENS = digit // 10
ONES = digit % 10
DIFFERENCE = TENS - ONES

# Output results

print()
print(f"The difference of the digits of {digit} is {DIFFERENCE}")
