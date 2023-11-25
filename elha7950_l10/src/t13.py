"""
-------------------------------------------------------
Lab 10, Task 13

Description: 
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import file_copy

# Open the files

fh1 = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words.txt", "r")
fh2 = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words2.txt", "w")

# Print to the console

print("Copying 'words.txt' to 'words2.txt'")

# Call the function

file_copy(fh1, fh2)
