"""
-------------------------------------------------------
Lab 10, Task 6

Description:
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import number_stats

# Constants

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\numbers.txt", "r")

# Call the function

results = number_stats(fh)

# Close the file

fh.close()

# Output results

things = ["Smallest: ", "Largest: ", "Total: ", "Average: "]

for index in range(4):
    print(f"{things[index]}{results[index]}")
