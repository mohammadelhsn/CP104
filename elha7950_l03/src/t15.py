"""
-------------------------------------------------------
Lab 3, Task 15

Description: 
    Write a program to show what happens when you attempt to:
        print integer as an integer
        print integer as a floating point (real number) value
        print integer as a string
        print decimal as an integer
        print decimal as a floating point (real number) value
        print decimal as a string
        print phrase as a floating point (real number) value
        print phrase as an integer
        print phrase as a string
        using output formatting techniques.
    To make it easy to mark by the IAs, please comment out (put a # character in front of the line) the lines that do not work. Do not remove these lines!
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Define variables

integer = 654321
decimal = 654.32
phrase = "Hello World"

# Output results, except the ones that will cause the program to error

print(f"{integer:d}")
print(f"{integer:f}")
# print(f"{integer:s}")
# print(f"{decimal:d}")
print(f"{decimal:f}")
# print(f"{decimal:s}")
# print(f"{phrase:d}")
# print(f"{phrase:f}")
print(f"{phrase:s}")
