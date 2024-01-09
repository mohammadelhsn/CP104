"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports

# your imports here

from t07_functions import line_lengths

# Your code here

source = open(r"source.txt", "r")
fh_short = open(r"short.txt", "a")
fh_long = open(r"long.txt", 'a')

# Call the function

result = line_lengths(source, fh_short, fh_long, 16)

# Close the files

source.close()
fh_short.close()
fh_long.close()

# Output results

print(result)
