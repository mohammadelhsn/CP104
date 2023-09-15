"""
-------------------------------------------------------
Lab 2, Task 9 

Description: 
    A manufacturer wishes to determine the cost of producing an open-top 
    cylindrical container. The surface area of the container is the sum of the area 
    of the circular base plus the area of the outside. Write and test a program that 
    prompts the user to enter:
        the diameter of the base (cm)
        the height of the cylinder (cm)
        the cost of the material ($ per square cm)
        number of containers to produce
    Store pi as a constant value of 3.14.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""
# Get the input

diameter = float(input("Diameter of container base (cm): "))
height = float(input("Height of container (cm): "))
cost = float(input("Cost of material ($/cm^2): "))
container_count = int(input("Number of containers: "))

# Define your constants

PI = 3.14
RADIUS = diameter / 2
SURFACE_AREA = (2 * PI * RADIUS * height) + (PI * RADIUS**2)
COST_FOR_ONE = SURFACE_AREA * cost
COST_FOR_ALL = COST_FOR_ONE * container_count

# Output the calculations

print(f"\nThe total cost of one containers is $ {COST_FOR_ONE}")
print(f"The total cost of all containers is $ {COST_FOR_ALL}")
