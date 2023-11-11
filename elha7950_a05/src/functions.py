"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants


CHAR = "#"
SPACE_CHAR = " "

# Functions


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1

    for i in range(1, number+1):
        product = product * i

    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Running on a treadmill burns a certain number of 
    calories. calories_treadmill prints a table of the 
    number of calories burned every five minutes given 
    the number of calories burned per minute (per_min) an 
    the total number of minutes run (minutes). Align the 
    results and print with 1 decimal accuracy for the 
    calories burned as shown in the example execution.
    Use: calories_treadmill(4.1, 20)
    -------------------------------------------------------
    Parameters:
        per_min - calories per minute (float)
        minutes - max minutes (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(5, minutes+1, 5):
        CALORIES = i * per_min
        print(f"  {i:2d} {CALORIES:.1f}")

    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Takes an integer parameter and prints a arrow of # characters pointing up.
    Use: arrow_up(4)
    -------------------------------------------------------
    Parameters:
        rows - number of rows (int) 
    Returns:
        None
    ------------------------------------------------------
    """

    spaces_middle = 1
    row_count = rows-1

    for i in range(1, rows+1, 1):
        if (i == 1):
            print(f"{SPACE_CHAR * row_count}{CHAR}")
            row_count -= 1
        else:
            print(f"{SPACE_CHAR * row_count}{CHAR}{spaces_middle * SPACE_CHAR}{CHAR}")
            row_count -= 1
            spaces_middle += 2
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    width = len(str(stop_num * stop_num)) + 1

    # Print the header row

    print(" " * width, end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:>{width}}", end="")
    print("\n" + " " * width + "-" * width * (stop_num - start_num + 2))

    # Print the table

    for i in range(start_num, stop_num + 1):
        print(f"{i:>{width - 1}} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:>{width}}", end="")
        print()

    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    -------------
    """

    total = 0
    current_value = start

    for i in range(count):
        total += current_value
        current_value += increment

    return total
