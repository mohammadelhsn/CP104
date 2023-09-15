"""
-------------------------------------------------------
Lab 2, Task 8

Description:
    Write a program to calculate the BMI (Body Mass Index) and BMI' (BMI Prime) 
    for a user. The BMI and 
    
        BMI ' are calculated by:
        BMI: user mass (kg) / user height (m)^2
        BMI': user BMI / user BMI upper limit
        
    The BMI upper limit depends on where the user is from. Users from South East 
    Asian and Southern China have a BMI upper limit of 23, and everyone else has 
    an upper limit of 25.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))
UPPER_LIMIT = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

# Calculations

BMI = weight / height**2
BMI_PRIME = BMI / UPPER_LIMIT

# Output the result

print(f"\nBody Mass Index (kg/m^2) = {round(BMI, 2)}")
print(f"BMI Prime = {round(BMI_PRIME, 2)}")
