"""
-------------------------------------------------------
Lab 5, Task 3

Description: 
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports

from functions import gym_cost

# Call the function

results = gym_cost(50, 2)

# Output results

print(results)
