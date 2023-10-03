"""
-------------------------------------------------------
Lab 4, Task 7 

Description: 
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports

from functions import total_change

# Call the function

total = total_change(5, 8, 5, 3, 4)

# Output results

print(total)
