"""
-------------------------------------------------------
Lab 5, Task 9

Description:
        Wind speeds are categorized as:

        Wind speed (km/h)	Category
                < 39	          Breeze
                39 -    61   Strong Wind
                62 -    88    Gale Winds
                89 -    117   Whole Gale
                > 117	       Hurricane
        The function should return 'unknown' for a negative wind speed.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports

from functions import wind_speed

# Call the function

result = wind_speed(88)

# Output results

print(result)
