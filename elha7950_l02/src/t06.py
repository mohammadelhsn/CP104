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
# Get the information from the user

principal = int(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
yearly_interest_rate = float(input("Yearly interest rate (%): "))

# Convert into months
number_of_payments = years * 12

# Divide so we have a amount / month rate
monthly_interest_rate = yearly_interest_rate / 100 / 12

# trying to find m (the monthly payment)

MONTHLY_PAYMENT = principal * (monthly_interest_rate * (1 + monthly_interest_rate)
                               ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1))
print(f"\nThe monthly payments are: $ {MONTHLY_PAYMENT}")
