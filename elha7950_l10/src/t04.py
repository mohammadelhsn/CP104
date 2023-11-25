"""
-------------------------------------------------------
Lab 10, Task 4

Description:
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""

# Imports

from functions import customer_first

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\customer.txt", "r")

# Call the function

result = customer_first(fh)

# Close the file

fh.close()

# Output results

print(result)
