"""
-------------------------------------------------------
Lab 2, Task 14

Description: 
    To create six servings of Mac and Cheese, you require the following ingredients:

    milk: 4 cups
    butter: 8 tablespoons
    flour: 0.5 cups
    salt: 2 teaspoons
    Define these values as constants.

    Write a program that asks the user how many servings of Mac and Cheese they 
    want to make, and print out the resulting ingredient list. Print with 2 decimal 
    places.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

servings = int(input("Enter servings of Mac & Cheese: "))

# Define Constants

MILK = 4
BUTTER = 8
FLOUR = 0.5
SALT = 2
DEFAULT_SERVINGS = 6

# Define the ratio

DIFFERENCE_FACTOR = servings / DEFAULT_SERVINGS

# Calculations

MILK = MILK * DIFFERENCE_FACTOR
BUTTER = BUTTER * DIFFERENCE_FACTOR
FLOUR = FLOUR * DIFFERENCE_FACTOR
SALT = SALT * DIFFERENCE_FACTOR

# Output results

print(f"\n{servings} serving(s) of Mac & Cheese requires:")
print(f"milk (cups): {MILK}")
print(f"butter (tablespoons): {BUTTER}")
print(f"flour (cups): {FLOUR}")
print(f"salt (teaspoons): {SALT}")
