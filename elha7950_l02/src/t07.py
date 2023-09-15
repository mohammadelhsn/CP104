"""
-------------------------------------------------------
Lab 2, Task 7

Description:
    A charity asks volunteers to distribute flyers for an event. 
    They want to distribute the flyers evenly amongst the volunteers. 
    Write and test a program that prompts the user to enter the number of flyers 
    and the number of volunteers, and prints the number of flyers per volunteer 
    and the number of flyers left over.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""
# Get the user input

number_of_flyers = int(input("Number of flyers: "))
number_of_volunteers = int(input("Number of volunteers: "))

# Calculations

FLYERS_PER = number_of_flyers // number_of_volunteers
REMAINDER = number_of_flyers % number_of_volunteers

# Output result

print(f"\nFlyers per volunteer: {FLYERS_PER}")
print(f"Flyers left over: {REMAINDER}")
