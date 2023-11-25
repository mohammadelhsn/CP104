"""
-------------------------------------------------------
Lab 10, Task 9

Description: 
    Counts the number of appearances of value in fh.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import count_frequency_value

# Open the file

fh = open(r"C:\Users\Techm\eclipse\ws\cp104\elha7950_l10\src\numbers.txt", "r")

# Print to the console

print("File 'numbers.txt' is open for reading.")

# Get the user input

times = int(input("Value to count: "))

# Call the function

result = count_frequency_value(fh, times)

# Close the file

fh.close()

# Output result

print(f'{times} appears {result} time(s)')
