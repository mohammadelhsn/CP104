"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants

LOONIE_VALUE = 100
QUARTER_VALUE = 25
DIMES_VALUE = 10
NICKLES_VALUE = 5

# your constants here


def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """

    _cents = cents
    LOONIES = _cents // LOONIE_VALUE
    _cents = _cents % LOONIE_VALUE
    QUARTER = _cents // QUARTER_VALUE
    _cents = _cents % QUARTER_VALUE
    DIMES = _cents // DIMES_VALUE
    _cents = _cents % DIMES_VALUE
    NICKLES = _cents // NICKLES_VALUE
    _cents = _cents % NICKLES_VALUE

    # your code here

    return LOONIES, QUARTER, DIMES, NICKLES
