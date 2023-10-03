"""
-------------------------------------------------------
Assignment 1, Task 4

Description: 
    This program asks the user for the cost of one dosa and the number of dosas they want, in that order, and 
    calculates and prints the total cost of the dosas.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""

# Get the user input

one_dosa_cost = float(input("Cost of 1 dosa: $"))
number_of_dosas = int(input("Number of dosa(s): "))

# Calculations

TOTAL_COST = one_dosa_cost * number_of_dosas

# Output results

print()
print(f"Total cost of {number_of_dosas} dosas: $ {TOTAL_COST}")
