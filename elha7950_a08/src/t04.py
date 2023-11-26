"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

from functions import valid_isbn

# Test Case 1: Valid ISBN
result = valid_isbn("978-3-16-148410-0")
# Expected Output: True
print(f"Test Case 1 - Expected: True, Actual: {result}")

# Test Case 2: Invalid ISBN (non-digit character 'X')
result = valid_isbn("978-3-16-1484X0-0")
# Expected Output: False
print(f"Test Case 2 - Expected: False, Actual: {result}")

# Test Case 3: Invalid ISBN (missing last digit)
result = valid_isbn("978-3-16-148410")
# Expected Output: False
print(f"Test Case 3 - Expected: False, Actual: {result}")

# Test Case 5: Invalid ISBN (length not 17)
result = valid_isbn("978-3-16-148410-01")
# Expected Output: False
print(f"Test Case 5 - Expected: False, Actual: {result}")
