"""
-------------------------------------------------------
Lab 3, Task 14

Description: 
    Write a program that asks the user to enter a number of minutes as int and calculates the number of days, 
    hours, and minutes and prints them to the screen.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Get the user input

minutes = int(input("Enter number of minute(s): "))

# Define Constants

MINUTES_IN_A_DAY = 1440
MINUTES_IN_AN_HOUR = 60

# Define temp variable to keep user entered data intact

_minutes = minutes

# Calculations

DAYS = _minutes // MINUTES_IN_A_DAY
_minutes = _minutes % MINUTES_IN_A_DAY
HOURS = _minutes // MINUTES_IN_AN_HOUR
_minutes = _minutes % MINUTES_IN_AN_HOUR
MINUTES = _minutes

# Output results

print(
    f"There are {DAYS:d} day(s), {HOURS:d} hour(s), and {MINUTES:d} minute(s) in {minutes:d} minute(s)")
