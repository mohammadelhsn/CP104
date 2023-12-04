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

from functions import line_numbering

# Open file for reading and writing

fh_read = open(
    r"C:\Users\Techm\eclipse\ws\cp104\elha7950_a09\src\wilde.txt", "r")
fh_write = open(
    r"C:\Users\Techm\eclipse\ws\cp104\elha7950_a09\src\new_file.txt", "w")

# Call the function, Output results

line_numbering(fh_read, fh_write)


# Close the files

fh_read.close()
fh_write.close()
