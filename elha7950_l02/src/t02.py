"""
-------------------------------------------------------
Lab 2, Task 2 

Instructions: 
    Fahrenheit to Celsius
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

fahrenheit = int(input("Temperature (F): "))

# Define constants
FREEZE_DIFFERENCE = 32

# Do some calculations

celsius = (fahrenheit - FREEZE_DIFFERENCE) * (5/9)

# Output results

print(f"\nTemperature (C): {celsius}")
