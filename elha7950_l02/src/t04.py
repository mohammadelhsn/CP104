"""
-------------------------------------------------------
Lab 2, Task 4 

Forumlua: r = n1/d1 * n2/d2
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

first_numerator = int(input("First numerator: "))
first_denominator = int(input("First denominator: "))
second_numerator = int(input("Second numerator: "))
second_denominator = int(input("Second denominator: "))

# Calculations

RESULT = (first_numerator / first_denominator) * \
    (second_numerator / second_denominator)

# Output results

print(f"\nProduct: {RESULT}")
