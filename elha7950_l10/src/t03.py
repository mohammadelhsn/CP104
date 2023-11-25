"""
-------------------------------------------------------
Lab 10, Task 3

Description: 
    Find the customer with the largest balance.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import customer_best

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\customer.txt", "r")

# Get the user input

print("Find customer by with largest balance:")

# Call the function

result = customer_best(fh)

# Close the file

fh.close()

# Output results

print(result)
