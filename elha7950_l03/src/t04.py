"""
-------------------------------------------------------
Lab 3, Task 4

Description:
    Write a program that asks the user to enter the following values as float. Print the resulting discount. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

number = float(input("Enter number: "))
percent = float(input("Enter percent: "))

# Calculations, Define Constants

PERCENT = percent / 100
CALCULATED = number * PERCENT

# Output results

print()
print(f"A {percent} discount on {number} is {CALCULATED:.1f}")
