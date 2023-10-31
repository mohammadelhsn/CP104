"""
-------------------------------------------------------
Assignment 4, Tasks 1-5

Description: 
    Functions for tasks 1-5. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
# Imports

# Constants

# Functions


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """

    # Define values

    day = ""

    # If / Elif / Else fall through structure

    if (day_num == 1):
        day = "Sunday"
    elif (day_num == 2):
        day = "Monday"
    elif (day_num == 3):
        day = "Tuesday"
    elif (day_num == 4):
        day = "Wednesday"
    elif (day_num == 5):
        day = "Thursday"
    elif (day_num == 6):
        day = "Friday"
    elif (day_num == 7):
        day = "Saturday"
    else:
        day = "Error"

    # Return values

    return day


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """

    # Define variables

    pollution = ""

    if (air_quality_index < 0):
        pollution = "Error"
    elif (air_quality_index <= 50):
        pollution = "Good"
    elif (air_quality_index <= 100):
        pollution = "Moderate"
    elif (air_quality_index <= 150):
        pollution = "Unhealthy for Sensitive Groups"
    elif (air_quality_index <= 200):
        pollution = "Unhealthy"
    elif (air_quality_index <= 299):
        pollution = "Very Unhealthy"
    else:
        pollution = "Hazardous"

    # Return values

    return pollution


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    # Define variables

    average1 = (val1 + val2) / 2
    average2 = (val2 + val3) / 2
    average3 = (val1 + val3) / 2

    average = 0

    if (average1 < average2):
        average = average2
    elif (average1 < average3):
        average = average3
    elif (average2 < average3):
        average = average3
    elif (average1 < average1):
        average = average1
    elif (average3 < average1):
        average = average1
    else:
        average = average2

    # Return values

    return average


def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """

    rgb_colour = ""

    if ((rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "red")):
        rgb_colour = "fuchsia"
    elif ((rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "red")):
        rgb_colour = "yellow"
    elif ((rgb_colour1 == "red" and rgb_colour2 == "red")):
        rgb_colour = "red"
    elif ((rgb_colour1 == "green") and (rgb_colour2 == "blue")):
        rgb_colour = "aqua"
    elif ((rgb_colour1 == "green") and (rgb_colour2 == "green")):
        rgb_colour = "green"
    elif ((rgb_colour1 == "blue") and (rgb_colour2 == "blue")):
        rgb_colour = "blue"
    else:
        rgb_colour = "Error"

    return rgb_colour


def hoo_rah(number):
    """
    -------------------------------------------------------
    Takes in a number and returns one of the following strings: 
        "Hoo" if number is evenly divisible by 2
        "Rah" if number is evenly divisible by 7
        "Hoo Rah" if number is evenly divisible by 2 and 7
        "Zip" if number is divisible by neither.
    Use: hoo_rah(2)
    -------------------------------------------------------
    Parameters:
        number - a number to get a string returned (int) 
    Returns:
        result - one of the strings from above (str)
    -------------------------------------------------------
    """
    result = ""

    if (((number % 7) == 0) and ((number % 2) == 0)):
        result = "Hoo Rah"
    elif (((number % 7) == 0) and ((number % 2) != 0)):
        result = "Rah"
    elif (((number % 7) != 0) and ((number % 2) == 0)):
        result = "Hoo"
    else:
        result = "Zip"

    return result
