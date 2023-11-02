"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants

# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """
    services = int(input("How many extra services are you purchasing? "))

    BASE_COST = 125
    COST_PER_EXTRA = 25

    cost = (BASE_COST + (COST_PER_EXTRA * services))

    if (services > 1):
        VIP = input("Are you a VIP member (Y/N)? ")

        if (VIP == "Y"):
            DISCOUNT = 0.1
            cost = cost - (cost * DISCOUNT)
        else:
            cost = (BASE_COST + (COST_PER_EXTRA * services))

    return cost
