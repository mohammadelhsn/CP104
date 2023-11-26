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

from functions import common_end

# Test Case 1: Common ending exists
result = common_end("apple", "pineapple")
# Expected Output: "apple"
print(f"Test Case 1 - Expected: 'apple', Actual: '{result}'")

# Test Case 2: No common ending
result = common_end("hello", "world")
# Expected Output: ""
print(f"Test Case 2 - Expected: '', Actual: '{result}'")

# Test Case 3: Empty strings
result = common_end("", "")
# Expected Output: ""
print(f"Test Case 3 - Expected: '', Actual: '{result}'")

# Test Case 4: One empty string
result = common_end("abc", "")
# Expected Output: ""
print(f"Test Case 4 - Expected: '', Actual: '{result}'")

# Test Case 5: Both empty strings
result = common_end("", "")
# Expected Output: ""
print(f"Test Case 5 - Expected: '', Actual: '{result}'")

# Test Case 6: Common ending with different cases
result = common_end("AbC", "aBC")
# Expected Output: "bC"
print(f"Test Case 6 - Expected: 'bC', Actual: '{result}'")
