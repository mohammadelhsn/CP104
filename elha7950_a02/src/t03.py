"""
-------------------------------------------------------
Assignment 2, Task 3 

Description: 
    This program asks the user for an integer that represent a date in the format YYYYMMDD and then prints 
    the date in the format YYYY/MM/DD. Assume that the user always enters a valid date. The program must use
    integer division and modulus, not strings, to extract the date parts.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""

# Get user input

date = int(input("Enter a date in the format YYYYMMDD: "))

# Calculations, Define Constants

YEAR = date // 10000
DAY = date % 100
MONTH = (date % (((YEAR * 10000) + DAY))) / 100

# Output results

print()
print(f"The reformatted date: {YEAR}/{int(MONTH):02d}/{DAY:02d}")
