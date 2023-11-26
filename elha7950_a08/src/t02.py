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

from functions import pluralize

# Call the function

# Output result

test_cases = [
    ("cat", "cats"),
    ("dog", "dogs"),
    ("city", "cities"),
    ("baby", "babies"),
    ("toy", "toys"),
    ("bus", "buses"),
    ("dish", "dishes"),
    ("fox", "foxes"),
    ("church", "churches"),
    ("piano", "pianos"),
]

for input_str, expected_output in test_cases:
    result = pluralize(input_str)
    print(
        f"Input: {input_str}, Expected Output: {expected_output}, Actual Output: {result}")
    assert result == expected_output, f"Test case failed: {input_str}"
