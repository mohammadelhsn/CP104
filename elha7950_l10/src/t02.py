"""
-------------------------------------------------------
Lab 10, Task 2

Description:
    Find the record for a given ID in a sequential file.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import customer_by_id

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\customer.txt", "r")

# Print to the console

print("Find customer by id number")

# Get the user input

row_id = int(input("Enter an ID: "))

# Call the function

result = customer_by_id(fh, row_id)

# Close the file

fh.close()

# Output result

print(result)
