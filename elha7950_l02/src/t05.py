"""
-------------------------------------------------------
Lab 2, Task 5

Description:
    Write and test a program that asks the user to input their pay and the number
    of hours they have worked in the last week, and outputs the total pay for the 
    week.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""
# Get the user input

hourly_rate = float(input("Hourly rate of pay: "))
hours_worked = float(input("Hours worked in the week: "))

# Calculations

GROSS_PAY = hourly_rate * hours_worked

# Output results

print(f"\nTotal pay for the week: $ {GROSS_PAY}")
