"""
-------------------------------------------------------
Lab 3, Task 6

Description:
    Write a program that asks the user to enter the following values as float and int where appropriate. 
    Print the resulting total. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

cost = float(input("Enter cost: $"))
quantity = int(input("Enter quantity: "))

# Calculations, Define Constants

TOTAL_COST = cost * quantity

# Output results

print()
print(
    f"Given a cost of ${cost:.2f} and a quantity of {quantity:d} the total is ${TOTAL_COST:.2f}")
