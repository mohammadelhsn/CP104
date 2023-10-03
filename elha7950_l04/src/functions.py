"""
-------------------------------------------------------
Lab 4, Functions Module
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports

from math import pi, sqrt

# Constants

NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25
LOONIE_VALUE = 1.00
TOONIE_VALUE = 2.00
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
SECONDS_PER_DAY = SECONDS_PER_HOUR * 24
SECONDS_PER_WEEK = SECONDS_PER_DAY * 7
SECONDS_PER_MONTH = SECONDS_PER_WEEK * 4
SECONDS_PER_YEAR = 31536000
FREEZE_DIFFERENCE = 32
SECONDS_IN_A_DAY = 86400
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MIN = 60


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """

    # Multiply radius * 2

    diam = radius * 2

    # Return result

    return diam


def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    # 2pir

    circ = pi * radius * 2

    # Return the result

    return circ


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    # pir^^2

    ar = pi * radius ** 2

    # Return the area

    return ar


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """

    # Calculations

    sh = sqrt((base / 2) ** 2 + height ** 2)
    area = base ** 2 + 2 * base * sqrt((base ** 2 / 4) + height ** 2)
    vol = base ** 2 * (height / 3)

    # Return values

    return sh, area, vol


def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, perimeter, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, per, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        per - perimeter of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """

    # Calculations

    ar = (adjacent * opposite) / 2
    hyp = sqrt(adjacent ** 2 + opposite ** 2)
    per = hyp + adjacent + opposite

    # Return hypotenuse, perimeter, area

    return hyp, per, ar


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """

    # Calculations using previous functions

    radius = right_triangle(s1, s2)[0]
    diam = radius * 2
    circ = circumference(radius)
    ar = area(radius)

    # Return results

    return radius, diam, circ, ar


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """

    # Calculations

    total = (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + \
        (quarters * QUARTER_VALUE) + (loonies *
                                      LOONIE_VALUE) + (toonies * TOONIE_VALUE)

    # Return results

    return total


def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    PERCENT = commission_percent / 100
    pre_commission_cost = computer_cost * computers_bought
    total_cost = pre_commission_cost + (pre_commission_cost * PERCENT)
    return pre_commission_cost, total_cost


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """

    # Calculations
    num = num1 * num2
    den = den1 * den2
    product = num / den

    # Return results

    return num, den, product


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
        size - current population (int >= 0)
        births - average seconds between births (int >= 0)
        deaths - average seconds between deaths (int >= 0)
        immigrants - average seconds between immigrations (int >= 0)
        years - years to calculate new population (int > 0)
    Returns:
        new_size - new population size (int)
    -------------------------------------------------------
    """

    # Calculations

    births_per_year = (SECONDS_PER_YEAR // births) * years
    deaths_per_year = (SECONDS_PER_YEAR // deaths) * years
    immigr_per_year = (SECONDS_PER_YEAR // immigrants) * years
    new_size = size + births_per_year + immigr_per_year - deaths_per_year

    # Return results

    return new_size


def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    # Calculations

    slp = (y2 - y1) / (x2 - x1)

    # Return results

    return slp


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    # Calculations

    fahrenheit = (9/5) * celsius + FREEZE_DIFFERENCE

    # Return results

    return fahrenheit


def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    # Calculations

    celsius = (fahrenheit - FREEZE_DIFFERENCE) * (5/9)

    # Return results

    return celsius


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    # Calculations

    days = seconds // SECONDS_IN_A_DAY
    hours = seconds // SECONDS_IN_AN_HOUR
    minutes = seconds // SECONDS_IN_A_MIN

    # Return results

    return days, hours, minutes


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    # Calculations

    _seconds = initial_seconds
    days = _seconds // SECONDS_IN_A_DAY
    _seconds = _seconds % SECONDS_IN_A_DAY
    hours = _seconds // SECONDS_IN_AN_HOUR
    _seconds = _seconds % SECONDS_IN_AN_HOUR
    minutes = _seconds // SECONDS_IN_A_MIN
    _seconds = _seconds % SECONDS_IN_A_MIN
    seconds = _seconds

    # Return results

    return days, hours, minutes, seconds
