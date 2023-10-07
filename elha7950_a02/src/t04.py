"""
-------------------------------------------------------
Assignment 2, Task 4

Description: 
    This program divides a number of flyers evenly amongst delivery people for distribution. The program asks 
    the user for the number of flyers and the number of delivery people, in that order. Print the number of 
    flyers each delivery person receives and the number of flyers left over.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

# Get user input

flyers = int(input("Number of flyers: "))
delivery_people = int(input("Number of delivery people: "))

# Calculations, Define Constants

PER_DELIVERY_PERSON = flyers // delivery_people
LEFT_OVER = flyers % delivery_people

# Output results

print()
print(f"Flyers per delivery person: {PER_DELIVERY_PERSON}")
print(f"Flyers left over: {LEFT_OVER}")
