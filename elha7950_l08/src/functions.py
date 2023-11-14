"""
-------------------------------------------------------
Lab 8, Functions

Description: 
    Functions for tasks 1-15
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports

from random import randint

# Constants

WEEKDAYS = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
DIGITS = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]

# Functions


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """

    # Get the name

    name = WEEKDAYS[d-1]

    # Return the value

    return name


def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    # Get the name

    name = MONTHS[m-1]

    # Return the value

    return name


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    # Get the name

    name = DIGITS[n]

    # Return the value

    return name


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    # Define the list

    values = []

    # Loop

    for i in range(n):

        # Generate a random number

        num = randint(low, high)

        # Add the random number to the values list

        values.append(num)

    # Return the list

    return values


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    # Define the numbers list

    numbers = []

    # Basically a for loop

    while (len(numbers) != n):

        # Generate the random number

        num = randint(low, high)

        # Check for duplicates, if it exists continue, otherwise add it to the list

        if (num in numbers):
            continue
        else:
            numbers.append(num)

    # Sort them from smallest to highest

    numbers.sort()

    # Return the list

    return numbers


def list_stats(values: list):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    # By sorting it, the largest is always going to be at the end
    # And the smallest is going to be the first

    values.sort()

    # Define variables

    largest = values[-1]
    smallest = values[0]
    total = 0

    # Get the total

    for num in values:
        total += num

    # Calculate average

    average = total / len(values)

    # Return values

    return (smallest, largest, total, average)


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """

    # Define variables

    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0

    for val in values:
        # If the value is zero, add to zeroes and evens

        if (val == 0):
            zeroes += 1
            evens += 1
        elif (val > 0):

            # If value is greater than zero, add to positive then check if it's even or odd.

            positives += 1

            if ((val % 2) == 0):
                evens += 1
            else:
                odds += 1
        else:
            # Else the value is guaranteed to be negative, therefore add to negative and check for even / odd.

            negatives += 1

            if ((val % 2) == 0):
                evens += 1
            else:
                odds += 1

    # Return all values

    return (negatives, positives, zeroes, evens, odds)


def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1

    # While loop requirement???

    while True:

        # Checks for only 1 value

        for i in range(len(values)):
            if (values[i] == value):
                index = i
                break
        break

    return index


def many_search(values: list, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    # Define list of indexes

    indexes = []

    # Add all occurrences to the indexes list

    for i in range(len(values)):
        if (values[i] == value):
            indexes.append(i)

    # Return list

    return indexes


def min_search(values: list):
    """
    -------------------------------------------------------
    Searches through values for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes values has at least
    one element.)
    User: indexes = min_search(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
    Returns:
        indexes - a list of indexes of the minimum values in
            values (list of int).
    -------------------------------------------------------
    """
    indexes = []

    # Copy the list so as to not modify the original and mess up the indexes.

    values2: list = values.copy()

    # Sorts from smallest to highest, so index at 0 is always going to be the smallest number.

    values2.sort()

    minimum = values2[0]

    # Check all numbers that are the same as the minimum

    for i in range(len(values)):
        if (values[i] == minimum):
            indexes.append(i)

    # Return list

    return indexes


def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: product = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        product - source1 • source2 (float)
    -------------------------------------------------------
    """
    # Define product total

    product = 0

    # Add the product to the total

    for index in range(len(source1)):
        product += ((source1[index]) * (source2[index]))

    # Return the total (dot product)

    return product


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    # Define list

    target = []

    # Append the sum of both values at the same index

    for index in range(len(source1)):
        target.append((source1[index])+(source2[index]))

    # Return the list

    return target


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the union of source1 and source2 (list of *)
    -------------------------------------------------------
    """

    # Define the list

    target = []

    # If the element is not in target append it, else continue

    for i in range((len(source1))):
        if (source1[i] not in target):
            target.append(source1[i])
        else:
            continue

    # If the element is not in target append it, else continue

    for i in range((len(source2))):
        if (source2[i] not in target):
            target.append(source2[i])
        else:
            continue

    # Return values

    return target


def intersection(source1, source2: list):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    # Define the list

    target = []

    # Add things to the list that are only found once in the other list and not already in the list

    for el in source1:
        if ((el not in target) and (source2.count(el) == 1)):
            target.append(el)
        else:
            continue

    # Return list

    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    # Define the list

    target = []

    # Check if the element is not in source2 and append them.

    for el in source1:
        if (el not in source2):
            target.append(el)
        else:
            continue

    # Check if the element is not in source1 and append them as well.

    for el in source2:
        if (el not in source1):
            target.append(el)
        else:
            continue

    # Return values.

    return target
