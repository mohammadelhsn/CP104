"""
-------------------------------------------------------
Midterm B Task 1 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports
from t01_functions import minimal_change

cents = int(input("Cents: "))
loonies, quarters, dimes, nickels = minimal_change(cents)
print(
    f"minimal_change({cents}) -> ({loonies}, {quarters}, {dimes}, {nickels})")
