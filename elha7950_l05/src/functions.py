"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports


# Constants

ACC_DUE_TO_GRAVITY = 9.8
NO_FRIENDS = 0
ONE_FRIEND = 5 / 100
TWO_FRIENDS = 10 / 100
THREE_FRIENDS = 15 / 100

# Functions


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """

    magic = False

    if ((day * month) == year):
        magic = True
    else:
        magic = False
    return magic


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """

    weight = mass * ACC_DUE_TO_GRAVITY
    message = "average"

    if (weight > 1000):
        message = "heavy"
    elif (weight < 10):
        message = "light"
    else:
        message = "average"

    return weight, message


def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """

    discount = 0

    if (friends == 0):
        discount = 0
    elif (friends == 1):
        discount = cost * ONE_FRIEND
    elif (friends == 2):
        discount = cost * TWO_FRIENDS
    else:
        discount = cost * THREE_FRIENDS

    TOTAL_COST = cost - discount
    return TOTAL_COST


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
            v1 is the value chosen if v1 and v2 are an equal
            distance from target (float)
    -------------------------------------------------------
    """

    diff_1 = abs(target - v1)
    diff_2 = abs(target - v2)
    closest_num = 0.0

    if (diff_1 == diff_2 or diff_2 > diff_1):
        closest_num = v1
    else:
        closest_num = v2
    return closest_num


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    result = False

    if ((year % 100) == 0):
        if ((year % 400) == 0):
            result = True
        else:
            result = False
    elif ((year % 4) == 0):
        result = True
    else:
        result = False
    return result
