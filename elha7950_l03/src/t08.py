"""
-------------------------------------------------------
Lab 3, Task 8

Description: 
    Write a program that asks the user to enter the following amounts as float. Print the resulting total 
    cubic metres with amounts lined up.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Get the user input

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

# Calculations, Define Constants

TOTAL = dirt + gravel + sand

# Output results

print()
print("Material   Cubic Metres")
print(f"Dirt       {dirt:5.1f}")
print(f"Gravel     {gravel:5.1f}")
print(f"Sand       {sand:5.1f}")
print(f"Total      {TOTAL:5.1f}")
