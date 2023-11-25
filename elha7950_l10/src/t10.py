"""
-------------------------------------------------------
Lab 10, Task 10

Description:
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import count_frequency_word

# Open the file 

fh = open(r'C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\words.txt', "r")

# Print to the console

print("File 'words.txt' is open for reading.")

# Get the user input

word = input("Word to count: ")

# Call the function

result = count_frequency_word(fh, word)

# Close the file

fh.close()

# Output result

print(f"'{word}' appears {result} time(s)")