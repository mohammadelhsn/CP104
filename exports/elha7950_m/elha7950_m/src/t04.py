"""
-------------------------------------------------------
Midterm B Task 4 Testing
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports
# your imports here

from t04_functions import get_it

# your code here

# Yes response

response_yes = get_it('Y')
print(response_yes)

# Print space

print()

# No response

response_no = get_it('N')
print(response_no)

# Print space

print()

# Random string to get the error

response_fjkldjfklsdjfad = get_it('fjkldjfklsdjfad')
print(response_fjkldjfklsdjfad)
