"""
-------------------------------------------------------
Lab 2, Task 1

Instructions: 
    Celsius to Fahrenheit
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""
# Get the user input

celsius = int(input("Temperature (C): "))

# Define Constants

FREEZE_DIFFERENCE = 32

# Calculations

fahrenheit = (9/5) * celsius + FREEZE_DIFFERENCE

# Output results

print(f"\nTemperature (F): {fahrenheit}")
