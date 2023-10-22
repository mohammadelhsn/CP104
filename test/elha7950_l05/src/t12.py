"""
-------------------------------------------------------
Lab 5, Task 12

Description: 
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports

from functions import pay_raise

# Call the function

results = pay_raise('F', 2, 25000)

# Output results

print(results)
