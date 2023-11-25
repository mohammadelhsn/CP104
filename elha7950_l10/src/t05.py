"""
-------------------------------------------------------
Lab 10, Task 5

Description: 
    Appends a customer record to a comma-delimited sequential file.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""

# Imports

from functions import customer_append

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\customer.txt", "a")

# Define the data to be appended

data = ['35612', 'David', 'Brown', 237.56, '2008-10-10']

# Call the function

customer_append(fh, data)

# Close the file

fh.close()
