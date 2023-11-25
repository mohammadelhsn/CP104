"""
-------------------------------------------------------
Lab 10, Task 14

Description: 
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import file_copy_n

# Open the files

fh1 = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words.txt", "r")
fh2 = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words2.txt", "w")

# Print to the console

print("Copying 'words.txt' to 'words2.txt'")

# Get the user input

numOfLines = int(input("Number of lines to copy: "))

# Call the function

file_copy_n(fh1, fh2, numOfLines)
