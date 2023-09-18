"""
-------------------------------------------------------
Lab 2, Task 3

Description: 
    Your dog grooming business charges $75.00 for a large dog and $50.00 dollars 
    for a small dog. Write and test a program to prompt the user to enter the 
    number of large dogs groomed that day and the number of small dogs groomed 
    that day and prints the total amount of money made that day.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

large_dogs = int(input("Number of large dogs groomed: "))
small_dogs = int(input("Number of small dogs groomed: "))

# Define Constants

LARGE_RATE = 75
SMALL_RATE = 50

# Calculations

TOTAL = (small_dogs * SMALL_RATE) + (large_dogs * LARGE_RATE)

# Output results

print(f"\nTotal earned for the day: $ {TOTAL}")
