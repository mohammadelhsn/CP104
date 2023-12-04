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

from functions import read_integers

# Open the file

fh = open(r'C:\Users\Techm\eclipse\ws\cp104\elha7950_a09\src\numbers.txt', 'r')

# Call the function

result = read_integers(fh)

# Close the file

fh.close()

# Output result

print(result)
