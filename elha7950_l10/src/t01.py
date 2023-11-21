"""
-------------------------------------------------------
Lab 10, Task 1

Description:
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import customer_record

# Define File Handle

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\customer.txt", "r")

print("Find record n")
row_num = int(input("Enter a record number: "))

# Get row data

row_data = customer_record(fh, row_num)

# Close file

fh.close()

# Output data.

print(row_data)
