"""
-------------------------------------------------------
Lab 2, Task 12 

Description:
    Calculate total hours, days, minutes, and seconds given input in seconds.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get user input

seconds = int(input("Number of seconds: "))

# Define Constants

SECONDS_IN_A_DAY = 86400
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MIN = 60

# Setup variables for output

DAYS = 0
HOURS = 0
MINUTES = 0
SECONDS = 0

"""
I'm going to be honest and admit that I didn't think of this initially. I had to do some research in order
to find the solution but now it occurs to me why it works. I was thinking of using the time module
but often the correct solution is the more simpler solution. Lesson learned! 

Floor division to get the amount of times it divides into it and remainder to get the remainder And use it for 
the next ones so it doesn't calculate the time for the previous time that has already been counted for. 
"""

DAYS = seconds // SECONDS_IN_A_DAY
seconds = seconds % SECONDS_IN_A_DAY
HOURS = seconds // SECONDS_IN_AN_HOUR
seconds = seconds % SECONDS_IN_AN_HOUR
MINUTES = seconds // SECONDS_IN_A_MIN
seconds = seconds % SECONDS_IN_A_MIN
SECONDS = seconds

print(f"\nDays: {DAYS} Hours: {HOURS} Minutes: {MINUTES} Seconds: {SECONDS}")
