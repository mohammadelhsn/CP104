"""
-------------------------------------------------------
Lab 10, Task 11

Description: 
    Finds the last word with longest length in fh.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import find_longest

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words.txt", "r")

# Call the function

result = find_longest(fh)

# Close the file

fh.close()

# Output results

print(result)
