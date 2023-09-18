"""
-------------------------------------------------------
Lab 2, Task 6

Description:
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""
# Get the user input

principal = int(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
yearly_interest_rate = float(input("Yearly interest rate (%): "))

# Calculations

number_of_payments = years * 12
monthly_interest_rate = yearly_interest_rate / 100 / 12

# Define Constants

MONTHLY_PAYMENT = principal * (monthly_interest_rate * (1 + monthly_interest_rate)
                               ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1))

# Output results

print(f"\nThe monthly payments are: $ {MONTHLY_PAYMENT}")
