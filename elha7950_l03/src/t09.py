"""
-------------------------------------------------------
Lab 3, Task 9

Description: 
    Write a program that asks the user to enter the following costs as float. Print the resulting total cost
    with prices lined up.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

sweatband_cost = float(input("Enter sweatband cost: $"))
pants_cost = float(input("Enter pants cost: $"))
jacket_cost = float(input("Enter jacket cost: $"))

# Calculations, Define Constants

TOTAL = sweatband_cost + pants_cost + jacket_cost

# Output results

print()
print("Clothes      Cost")
print(f"Sweatband    ${sweatband_cost:6.2f}")
print(f"Pants        ${pants_cost:6.2f}")
print(f"Jacket       ${jacket_cost:6.2f}")
print(f"Total        ${TOTAL:6.2f}")
