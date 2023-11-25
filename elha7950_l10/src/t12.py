"""
-------------------------------------------------------
Lab 10, Task 12

Description: 
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import find_shortest

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words.txt", "r")

# Print to the console

print("File 'words.txt' open for reading.")

# Call the function

shortest = find_shortest(fh)

# Output result

print(f"'{shortest}' is the shortest word.'")
