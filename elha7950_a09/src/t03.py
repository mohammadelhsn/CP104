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

from functions import file_statistics

# Open the file

fh = open(r'C:\Users\Techm\eclipse\ws\cp104\elha7950_a09\src\addresses.txt', "r")

# Call the function

stats = file_statistics(fh)

# Close the file

fh.close()

# Output results

print(stats)
