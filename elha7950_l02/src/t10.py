"""
-------------------------------------------------------
Lab 2, Task 10

Description: 
    Write a program that asks a user for the cost of a meal and the percentages for the tax and tip, 
    and prints a bill. All three values should be floats. The tip percentage is applied against the food 
    cost only, not against the tax.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

food_charge = float(input("Food Charge: $"))
sales_tax = float(input("Sales Tax in (%): "))
tip = float(input("Tip in (%): "))

# Calculations

sales_tax = sales_tax / 100
tip = tip / 100

# Define Constants

CALCULATED_TAX = food_charge * sales_tax
CALCULATED_TIP = food_charge * tip
TOTAL = food_charge + CALCULATED_TIP + CALCULATED_TAX

# Output results

print("\nCost of meal:")
print(f"Subtotal: $ {food_charge}")
print(f"     Tax: $ {CALCULATED_TAX}")
print(f"     Tip: $ {CALCULATED_TIP}")
print(f"------------------")
print(f"   Total: $ {TOTAL}")
