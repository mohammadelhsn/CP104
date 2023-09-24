"""
-------------------------------------------------------
Lab 3, Task 12

Description: 
    Using the following assignment statements:
        first = 100
        second = 34
        third = 933
    Write a program to calculate their total and print these values in the following format:
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Define variables
first = 100
second = 34
third = 933

# Define Constants

TOTAL = first + second + third

# Output results

print("Values")
print(f"First:  {first:_>6d}")
print(f"Second: {second:_>6d}")
print(f"Third:  {third:_>6d}")
print(f"Total:  {TOTAL:_>6d}")
