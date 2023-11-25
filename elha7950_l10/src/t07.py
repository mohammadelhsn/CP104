"""
-------------------------------------------------------
Lab 10, Task 7

Description: 
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import append_max_num

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\numbers.txt", "r+")

# Call the function

append_max_num(fh)

# Close the file

fh.close()
