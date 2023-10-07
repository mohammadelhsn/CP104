"""
-------------------------------------------------------
Assignment 2, Task 1

Description: 
    This program calculates the annual tax paid by a company. The company's annual tax is 18.5 percent of 
    total billing. The program asks the user to enter the projected total sales and prints the tax that is 
    to be paid on that amount. The program must not ask the user for the tax rate, it should be defined as a 
    constant.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

# Get user input

total_sales = int(input("Enter the total sales: $"))

# Calculations, Define Constants

TAX_RATE = 18.5 / 100
TAX = total_sales * TAX_RATE

# Output results

print("Projected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {total_sales}")
print(f"Annual tax:    % {TAX_RATE * 100}")
print("--------------------------")
print(f"Tax:           $  {TAX}")
