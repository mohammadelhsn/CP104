"""
-------------------------------------------------------
Lab 10, Task 8

Description: 
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import append_increment

# Open the file for reading and writing

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\numbers.txt", "r+")

# Print to the console

print("File 'numbers.txt' open for reading and writing.")

# Call the function

result = append_increment(fh)

# Close the file

fh.close()

# Output result

print(f"{result} is appended.")
