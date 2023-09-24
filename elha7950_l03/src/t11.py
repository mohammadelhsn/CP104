"""
-------------------------------------------------------
Lab 3, Task 11

Description: 
    Using the following assignment statements:
        location1 = "left"
        location2 = "middle"
        location3 = "right"
    Write a program to print these values in the following format (each line has a width of 20 characters):
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Define variables

location1 = "left"
location2 = "middle"
location3 = "right"

# Output results

print(f"{location1:-<20s}")
print(f"{location2:-^20s}")
print(f"{location3:->20s}")
