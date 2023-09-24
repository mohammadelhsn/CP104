"""
-------------------------------------------------------
Lab 3, Task 10

Description: 
    Write a program that asks the user to enter a year, day, and month as separate int. Print the resulting 
    date out in year/month/day format with leading zeros where appropriate. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

# Output results

print()
print(f"The date: {year:4d}/{month:02d}/{day:02d}")
