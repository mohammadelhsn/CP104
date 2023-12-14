"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
# Imports

# Constants

# Functions


def list_factors(number):
    """
    -------------------------------------------------------
    list_factors takes an integer greater than 0 as a 
    parameter (number) and returns a list of the factors 
    that make up that number excepting the number itself. 
    An integer's factors are the whole numbers that the 
    integer can be evenly divided by.
    Use: factors = list_factors(9)
    -------------------------------------------------------
    Parameters:
        number - number    
    Returns:
        factors - a list of the factors that make up that number excepting the number itself.
    ------------------------------------------------------
    """
    factors = []

    for i in range(1, int((number ** 0.5) + 1)):
        if (number % i == 0):
            factors.append(i)

            if (i != number // i):
                factors.append(number // i)
    factors.remove(number)
    factors.sort()
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers_list = []

    while True:
        num = int(input("Enter a positive number: "))

        if (num > 0):
            numbers_list.append(num)
            continue
        elif (num == 0):
            break
        elif (num < 0):
            continue

    return numbers_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []

    for i in range(len(numbers)):
        if ((numbers[i]) == target_number):
            index_list.append(i)
        continue

    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for element in subtrahend:
        indexes = get_indexes(minuend, element)
        indexes.reverse()
        for index in indexes:
            del minuend[index]
    return


def verify_sorted(numbers: list):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1

    # based on the hint that an empty list is sorted

    if (len(numbers) == 0):
        in_order = True
        index = -1

    # based on the hint, the first number can never be the number out of place

    for i in range(len(numbers) - 1):
        if (numbers[i] > numbers[i + 1]):
            in_order = False
            index = i + 1

    return in_order, index
