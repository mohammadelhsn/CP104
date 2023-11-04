"""
-------------------------------------------------------
Lab 7, Tasks 1-10

Description: 
    Functions for tasks 1-10. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports

from random import randint

# Constants

TAX_AMOUNT = 3.625 / 100

# Functions


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """

    # Define the random number

    ranNum = randint(1, high)

    # Define the variable to keep track
    # of the number of attempts made.

    count = 0

    # Let the user guess.

    guess = int(input("Guess: "))

    # Keeps going until they get the right number

    while (guess != ranNum):

        # Self-Explanatory

        if (guess > ranNum):
            print("Too high, try again!")
        else:
            print("Too low, try again!")

        # Adds to the count of guesses

        count += 1

        # Keeps asking so that the loop can continue.

        guess = int(input("Guess: "))

    # Even when they guess it right, you
    # still have to add to the count since
    # it's an attempt.

    count += 1

    # Output

    print("Congratulations! You got it!")
    print(f"You made {count} guesses.")

    # Return the amount of guesses made.

    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    # Define variables

    power = 0

    while ((2 ** power) < target):
        power += 1

    power = 2 ** power

    # Return the values

    return power


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """

    # Define variables and Constants

    years = 0
    population = current
    RATE = rate / 100

    while (target > (population)):
        population += (population * RATE)
        years += 1

    # Return values

    return years


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """

    # Define variables

    final = 0
    current = 0

    # Wouldn't work with the number 0 otherwise.

    if (target == 0):
        final = 1

    while (final < target):
        final += (current ** 2)
        current += 1

    # Return the final value.

    return final


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """

    # Define variables needed.

    maximum = float('-inf')
    minimum = float('inf')
    keep_input = True
    average = 0
    total = 0
    count = 0

    # Get the user input

    value = float(input("First positive value "))

    # Do the first one outside of the loop.

    maximum = value
    minimum = value
    count += 1
    total += value

    while keep_input:

        # Do the remainder inside the loop.

        value = float(input(f'Next positive value: '))

        # Break out of the loop and set the setnil value to false so that the loop
        # doesn't keep going.

        if (value < 0):
            keep_input = False
            average = total / count
        else:
            if (value < minimum):
                minimum = value
            elif (value > maximum):
                maximum = value

            count += 1
            total += value

    # Return the values

    return (float(minimum), float(maximum), float(total), float(average))


def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """

    # Define variables

    keep_input = True
    positives = 0
    negatives = 0
    zeros = 0

    # Get the user input

    value = float(input("First value: "))

    # Do the first one outside of the loop, do the remainder inside the loop

    if (value == 0):
        zeros += 1
    elif (value == -999):
        keep_input = False
    elif (value > 0):
        positives += 1
    else:
        negatives += 1

    while (keep_input):
        value = float(input("Next value: "))

        if (value == 0):
            zeros += 1
        elif (value == -999):
            keep_input = False
            break
        elif (value > 0):
            positives += 1
        else:
            negatives += 1

    # Return values.

    return (negatives, zeros, positives)


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """

    # Define variables

    total_breakfast = 0
    total_supper = 0
    keep_going = "Y"
    total_lunch = 0
    total_total = 0
    day = 1

    while (keep_going.lower() == "y"):

        print(f"For day {day}")
        print()

        # Get the user input

        breakfast = float(input("How much was breakfast? $"))
        lunch = float(input("How much was lunch? $"))
        supper = float(input("How much was supper? $"))
        day_total = breakfast + lunch + supper

        # Output the cost for the day

        print(f"Your total for the day was ${day_total}")

        # Add to the totals for the end.
        # Add 1 to the day to make it consistent.

        total_breakfast += breakfast
        total_lunch += lunch
        total_supper += supper
        total_total += day_total
        day += 1

        keep_going = input("Were you away another day (Y/N)? ")

    return (round(total_breakfast, 2), round(total_lunch, 2), round(total_supper, 2), round(total_total, 2))


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    # Define variables

    balance = available
    expenses = 0
    status = ""
    string = "Enter an expense (0 to quit): $"
    keep_going = True

    while (keep_going == True):

        # Get the user input

        expense = float(input(string))

        if (expense == 0):

            # The user has decided to quit.
            # Get the data ready for the return.

            keep_going = False

            if (balance < 0):
                status = "Deficit"
            elif (balance == 0):
                status = "Balanced"
            else:
                status = "Surplus"
            break
        else:
            expenses += expense
            balance -= expense

    # Return values

    return (expenses, balance, status)


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the highest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """

    # Define variables.

    keep_asking = True
    value = 0

    while (keep_asking):

        # Get the user input

        value = int(input(f"Enter a value between {low} and {high}"))

        # Self-Explanatory

        if (value > high):
            print("Value entered is too high!")
        elif (value < low):
            print("Value entered is too low.")
        else:

            # The user has decided to quit.

            print()

            # Switch to false to stop the loop.

            keep_asking = False
            break

    # Return values.

    return value


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    # Define variables.

    keep_going = True
    total = 0
    average = 0
    count = 0

    while (keep_going):

        # Get the user input

        employee_id = int(input("Employee ID: "))

        if (employee_id == 0):
            # The user has decided to quit.

            # Switch the variable to false so that the loop stops.
            # Get the data ready to return.

            keep_going = False
            average = total / count
            break
        else:

            # Add one for the average.

            count += 1

            # Get the user input.
            hourly_wage_rate = int(input("Hourly wage rate: "))
            hours_worked = int(input("Hours worked: "))
            GROSS_PAY = 0
            if (hours_worked > 40):
                GROSS_PAY = (hourly_wage_rate * 40) + \
                    ((hourly_wage_rate * 1.5) * (hours_worked - 40))
            else:
                GROSS_PAY = hourly_wage_rate * hours_worked
            NET_PAY = GROSS_PAY - (GROSS_PAY * TAX_AMOUNT)
            total += NET_PAY
            print(f"Net payment for employee {employee_id} is ${NET_PAY:,.2f}")
            print()
            continue

    # Return the values.

    return (round(total, 2), round(average, 2))
