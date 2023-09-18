"""
-------------------------------------------------------
Lab 2, Task 11

Description: 
    A company has determined that its annual profit is typically 18 percent of total 
    sales. Write and test a program that asks the user to enter the projected amount 
    of total sales and then displays the profit that is made from that amount. 
    Do not ask the user for the profit percentage, store it as a constant.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

projected_annual_sales = float(input("Enter projected annual sales: $"))

# Define Constants

PROFIT_PERCENTAGE = 0.18
PROJECTED_PROFIT = projected_annual_sales * PROFIT_PERCENTAGE

# Output results

print(
    f"\nThe projected profit on sales of $ {projected_annual_sales} is $ {PROJECTED_PROFIT}")
