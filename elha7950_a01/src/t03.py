"""
-------------------------------------------------------
Assignment 1, Task 3

Description: 
    This program asks the user for a length in miles and prints the equivalent length in kilometres. Use 1.61 
    as the conversion factor from miles to km.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

miles = float(input("Length in miles: "))

# Define Constants

CONVERSION_FACTOR = 1.61

# Calculations

KM = miles * CONVERSION_FACTOR

# Output the result

print(f"Length in km: {KM}")
