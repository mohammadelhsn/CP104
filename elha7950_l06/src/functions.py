"""
-------------------------------------------------------
Lab 6, Task 1-15

Description: 
    Functions for tasks 1-15. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
# Imports

import math

# Constants

SPACE_CHAR = " "

# Functions


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """

    # Define variables

    total = 0

    # Add one because programming starts counting from 0.

    for n in range(2, (num + 1), 2):

        # Add the number and continue

        total += n
        continue

    # Return values

    return total


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """

    # Define variables

    total = 0

    # Add one because programming starts counting from 0.

    for n in range(1, (num + 1), 2):

        # Add the number and continue

        total += n
        continue

    # Return values

    return total


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    # Define variables

    total = 0

    for n in range(start, (finish+1), increment):

        # Add the number and continue

        total += n
        continue

    # Return values

    return total


def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive)
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """

    # Define variables

    total = 0

    # Add one because programming starts counting from 0

    for n in range(1, (n+1), 1):

        # Add to the total and continue

        total += 1/n
        continue

    # Return values

    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(height):

        # Output row

        print(char * width)

    # Return nothing

    return


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    times = 1
    space = (height - 1)

    for i in range(height):
        print(f"{SPACE_CHAR * space}{char * times}")

        # To determine the amount of the character to include

        times += 2

        # To determine the amount of space to include

        space -= 1

    # Return nothing

    return


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    times = 1

    for i in range(width):
        print(char * times)
        times += 1

    # Get the numbers right

    times -= 2

    # Now to do the other half of the triangle
    for i in range(width):

        # Output values and take away from the times variable

        print(char * times)
        times -= 1

    # Return none
    return


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    # Print the first 2 rows outside of the loop
    print(char)
    print(char * 2)

    space = 1

    for i in range(width - 3):
        print(f"{char}{SPACE_CHAR * space}{char}")

        # Space variable

        space += 1

    # Print the last row outside of the loop and return

    print(char * width)
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n, 0, -1):
        BOTTLES_TOP = "bottle" if ((i) == 1) else "bottles"
        BOTTLES_BOTTOM = "bottle" if ((i - 1) == 1) else "bottles"
        NONE = "no more" if ((i - 1) == 0) else f"{i-1}"
        print(f"{i} {BOTTLES_TOP} of beer on the wall, {i} {BOTTLES_TOP} of beer.")
        print(
            f"Take one down, pass it around, {NONE} {BOTTLES_BOTTOM} of beer on the wall.")
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(start, (end+1), inc):
        CALORIES_BURNT = round(burnt_per_minute * i, 1)
        print(f"Calories burned after {i} minutes: {CALORIES_BURNT}")
    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("Age          Salary")
    print("-------------------")
    SALARY = salary
    for i in range(age, 66, 1):
        print(f"{i}       {SALARY:10,.2f}")
        SALARY = SALARY + (SALARY * (increase/100))
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """

    # Print the things that don't need to be repeated.

    print("Year            Value $")
    print("-----------------------")

    # Define our own value variable so as to not manipulate user input.

    VALUE = value

    # For later use.

    LAST_RATE = 0

    for i in range(0, years+1, 1):
        print(f" {i:2d}          {VALUE:10,.2f}")

        LAST_RATE = (VALUE * rate/100)
        VALUE = VALUE + LAST_RATE

    # Take away the last rate because the for loop automatically
    # adds it one more time after the last one

    final_value = (VALUE - LAST_RATE)

    # Return the final value

    return final_value


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    # Print things that don't need to be repeated.
    print("                         Cross-Sectional  Moment of  Section")
    print("Base   Height            Area             Inertia    Modulus")
    print("------------------------------------------------------------")

    for base in range(b_min, b_max+1, b_inc):
        for height in range(h_min, h_max+1, h_inc):

            # Cross Sectional Area

            CSA = base * height

            # Moment of Inertia

            MoI = (base * height ** 3) / 12

            # Section Modulus

            SM = (base * height ** 2) / 6

            # Output values
            print(
                f"   {base:2d}  x    {height:2d}             {CSA:7.2f}       {MoI:7.2f}     {SM:7.2f}")

    # Return nothing

    return


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    # Define variable to add to.

    total_hours = 0
    for i in range(1, 7):
        print(f"Week {i}")
        for i in range(ia_count):
            total_hours += float(input(f"  Marking hours for IA {i+1}: "))

    # Return total hours

    return total_hours


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    maximum = float('-inf')
    minimum = float('inf')
    total = 0
    count = 0

    for i in range(n):
        # Ternary Operator because I'm too lazy to do a whole if statement.

        FIRST_NEXT = "First" if (i == 0) else "Next"

        # Get the user input

        num = float(input(f"{FIRST_NEXT} value: "))

        # If num is greater than the previous max, make num the new max

        if (num > maximum):
            maximum = num

        # If num is less than the previous min, make num the new min.

        if (num < minimum):
            minimum = num

        # Total for total and average

        total += num

        # Count of numbers to divide by to get average

        count += 1

    return (float(minimum), float(maximum), float(total), (total/count))
