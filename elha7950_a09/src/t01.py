"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from functions import file_top

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_a09\src\students.txt", "r")

# Call the function

file_top(fh, 5)

# Close the file

fh.close()
