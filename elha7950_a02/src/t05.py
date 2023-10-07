"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""

# Get user input

foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_of_concrete = float(input("Cost of concrete ($/m^3): "))
cost_of_bricks = float(input("Cost of bricks ($/m^2): "))

# Calculations, Define Constants

FOUNDATION_CONCRETE = (foundation_height *
                       foundation_length * foundation_width)
TOTAL_CONCRETE_COST = FOUNDATION_CONCRETE * cost_of_concrete
BRICKS_NEEDED = (wall_height * (foundation_length * 2)) + \
    (wall_height * (foundation_width * 2))
TOTAL_BRICKS_COST = BRICKS_NEEDED * cost_of_bricks
TOTAL_COST = TOTAL_CONCRETE_COST + TOTAL_BRICKS_COST

# Output results

print()
print(f"Concrete needed for foundation (m^3): {FOUNDATION_CONCRETE}")
print(f"Cost of concrete: ${TOTAL_CONCRETE_COST}")
print(f"Bricks needed for walls (m^2): {BRICKS_NEEDED}")
print(f"Cost of bricks: ${TOTAL_BRICKS_COST}")
print(f"Total cost: ${TOTAL_COST}")
