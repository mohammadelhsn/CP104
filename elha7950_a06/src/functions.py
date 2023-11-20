"""
-------------------------------------------------------
Assignment 6 - Functions

Description:
    Functions for tasks 1-5
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports

# Constants

# Functions


def total_wins():
    """
    -------------------------------------------------------
    Returns wins for purple and gold. Type enter if you 
    wish to quit.
    Use: wins = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        Tuple - Number of wins for purple and gold
    ------------------------------------------------------
    """

    # Define variables

    asking = True
    purple = 0
    gold = 0

    # While loop

    while (asking == True):
        winner = input("Enter the winning team: ")

        if (winner.lower() == "purple"):

            # if the winner is purple, add one purple

            purple += 1
        elif (winner.lower() == "gold"):

            # if the winner is gold, add one to gold

            gold += 1
        elif (winner == ""):
            # The user would like to exit. Set asking to False and break out of the while loop.

            asking = False
            break
        else:
            continue

    # Return variables.

    return (purple, gold)


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    # Default set it to prime

    prime = False

    # If the number is less than or equal to one
    # It CANNOT be a prime number.

    if (number <= 1):
        prime = False

    # Divide by every number and if it divides evenly into something else
    # Return false, otherwise it is a prime number

    divisor = 2

    while (divisor < number):
        if ((number % divisor) == 0):
            prime = False
            break
        else:
            prime = True
            divisor += 1
            continue

    # Return values.

    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    INTEREST_RATE = (interest_rate / 100) / 12

    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    balance = principal_amount
    month = 1

    while (balance > 0):
        monthly_interest = balance * INTEREST_RATE
        if balance < payment:
            payment = balance + monthly_interest
            balance = 0
            print(f"{month:4d} {monthly_interest:9.2f} {payment:9.2f} {balance:9.2f}")
            break
        balance = max(balance - (payment - monthly_interest), 0)
        print(f"{month:4d} {monthly_interest:9.2f} {payment:9.2f} {balance:9.2f}")

        month += 1

    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    if (number == 0):
        digits = 1

    num = abs(number)
    while num > 0:
        digits += 1
        num //= 10  # Remove the last digit

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1

    while i < number:
        if ((number % i) == 0):
            total += i
        i += 1

    return total
