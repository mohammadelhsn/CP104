"""
-------------------------------------------------------
Lab 3, Task 13

Description:
    Write a program that asks the user to enter a number of seconds and calculates the number of hours, 
    minutes, and seconds as int, and prints them to the screen.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

seconds = int(input("Enter number of seconds: "))

# Define Constants

SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MIN = 60

# Define temp variable to keep user entered data intact

_seconds = seconds

# Calculations, Define more Constants

HOURS = _seconds // SECONDS_IN_AN_HOUR
_seconds = _seconds % SECONDS_IN_AN_HOUR
MINUTES = _seconds // SECONDS_IN_A_MIN
_seconds = _seconds % SECONDS_IN_A_MIN
SECONDS = _seconds

# Output results

print(
    f"There are {HOURS:d} hour(s), {MINUTES:d} minute(s), and {SECONDS:d} second(s) in {seconds:d} second(s)")
