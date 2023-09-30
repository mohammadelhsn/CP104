"""
-------------------------------------------------------
Assignment 1, Task 5

Description: 
    This program calculates and prints compound interest. Compound interest is calculated by:

    The equation: A = P(1+r/n)^(nt)
    Where: 
        P is the principal amount, 
        r is the annual rate of interest (as a decimal), 
        t is the number of years the amount is deposited or borrowed for, 
        n is the number of times the interest is compounded per year, and the result 
        A is the amount of money accumulated after t years.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""

# Get the user input

principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
years = int(input("Number of years: "))
compounded_per_year = int(
    input("Number of times interest compounded per year: "))

# Calculations

ANNUAL_INTEREST = interest / 100.0
TOTAL_ACCUMULATED = principal * \
    (1 + (ANNUAL_INTEREST / compounded_per_year)
     )**(compounded_per_year * years)

# Output results

print()
print(f"Balance: $ {TOTAL_ACCUMULATED}")
