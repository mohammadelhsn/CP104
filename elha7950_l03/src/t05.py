"""
-------------------------------------------------------
Lab 3, Task 5:

Description: 
    Write a program that asks the user to enter the following values as int. Print the resulting difference. 
    Format all values with integer formatting.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

minimum = int(input("Enter minimum: "))
maximum = int(input("Enter maximum: "))

# Calculations, Define Constants

DIFFERENCE = maximum - minimum

# Output results

print()
print(
    f"The difference between {maximum:d} and {minimum:d} is {DIFFERENCE:d}")
