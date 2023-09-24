"""
-------------------------------------------------------
Lab 3, Task 7

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

breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))

# Calculations, Define Constants

TOTAL = breakfast + lunch + supper

# Output results

print()
print("Meal         Cost")
print(f"Breakfast    ${breakfast:6.2f}")
print(f"Lunch        ${lunch:6.2f}")
print(f"Supper       ${supper:6.2f}")
print(f"Total        ${TOTAL:6.2f}")
