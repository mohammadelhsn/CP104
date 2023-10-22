"""
-------------------------------------------------------
Lab 5, Tasks 1-15

Description: 
    Functions file for the lab.
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
TAX_RATE = 3.625 / 100
I = "I"
V = "V"
X = "X"
UNKNOWN = 0
BREEZE = 39
STRONG_WIND = 62
GALE_WIND = 89
WHOLE_GALE = 118
LITTLE_DAMAGE = 5
SOME_DAMAGE = 5.5
SERIOUS_DAMAGE = 6.5
DISASTER = 7.5
FULL_TIME_LONG = 5 / 100
FULL_TIME_SHORT = 1.5 / 100
PART_TIME_LONG = 3 / 100
PART_TIME_SHORT = 1 / 100
OTHERS = 2 / 100
LOAN_MIN_YEARS = 5
LOAN_MIN_SALARY = 30000
INFANT = 3
SENIOR = 65
STUDENT_MIN = 10
STUDENT_MAX = 18
ADULT_MIN = STUDENT_MAX
ADULT_MAX = SENIOR
KID_MIN = INFANT
KID_MAX = STUDENT_MIN
INFANT_PRICE = 0
SENIOR_PRICE = 4.00
STUDENT_PRICE_IN = 1.00
STUDENT_PRICE_OUT = 3.00
ADULT_PRICE = 5.00
KID_PRICE = 2.00
BURGER_PRICE = 6.00
WINGS = 8.00
FRIES = 1.50
SALAD = 2.00

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

    # Initiate the variable

    magic = False

    # Process some conditions

    if ((day * month) == year):
        magic = True
    else:
        magic = False

    # Return the value

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
    # Define variables

    weight = mass * ACC_DUE_TO_GRAVITY
    message = "average"

    # Process some conditions

    if (weight > 1000):
        message = "heavy"
    elif (weight < 10):
        message = "light"
    else:
        message = "average"

    # Return the values

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

    # Define variables

    discount = 0

    # Process some conditions

    if (friends == 0):
        discount = 0
    elif (friends == 1):
        discount = cost * ONE_FRIEND
    elif (friends == 2):
        discount = cost * TWO_FRIENDS
    else:
        discount = cost * THREE_FRIENDS

    # Define constant

    TOTAL_COST = cost - discount

    # Return values

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
    # Define variables

    diff_1 = abs(target - v1)
    diff_2 = abs(target - v2)
    closest_num = 0.0

    # Process some conditions

    if (diff_1 == diff_2 or diff_2 > diff_1):
        closest_num = v1
    else:
        closest_num = v2

    # Return values

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
    # Define some variables

    result = False

    # Process some conditions

    if ((year % 100) == 0):
        if ((year % 400) == 0):
            result = True
        else:
            result = False
    elif ((year % 4) == 0):
        result = True
    else:
        result = False

    # Return values

    return result


def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i, j)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (boolean)
    ------------------------------------------------------
    """
    # Define variables

    result = False

    # Process some conditions

    if ((n % i == 0) and (n % j == 0)):
        result = True
    else:
        result = False

    # Return values

    return result


def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """

    # Define variables

    difference = hours_worked - 40
    net_payment = 0

    # Process some conditions

    if (difference >= 0):
        GROSS_PAY = (hourly_rate * 40) + ((hourly_rate * 1.5) * difference)
        net_payment = GROSS_PAY - (GROSS_PAY * TAX_RATE)
    else:
        GROSS_PAY = (hourly_rate * hours_worked)
        net_payment = GROSS_PAY - (GROSS_PAY * TAX_RATE)

    # Return values

    return round(net_payment, 2)


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
        between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """

    # Define variables

    numeral = " "

    # Process some conditions

    if (n > 10):
        numeral = None
    elif (n <= 3):
        numeral = I * n
    elif (n == 4):
        numeral = f"{I}{V}"
    elif (n <= 8):
        difference = n - 5
        numeral = f"{V}{I * difference}"
    elif (n == 9):
        numeral = f"{I}{X}"
    else:
        numeral = f"{X}"

    # Return values

    return numeral


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    # Define variables

    category = ""

    # Process some conditions

    if (speed < UNKNOWN):
        category = "Unknown"
    elif (speed < BREEZE):
        category = "Breeze"
    elif (speed < STRONG_WIND):
        category = "Strong Wind"
    elif (speed < GALE_WIND):
        category = "Gale Winds"
    elif (speed < WHOLE_GALE):
        category = "Whole Gale"
    else:
        category = "Hurricane"

    # Return values

    return category


def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    # Define variables

    result = ""

    # Process some conditions

    if (intensity < LITTLE_DAMAGE):
        result = "Little or no damage"
    elif (intensity < SOME_DAMAGE):
        result = "Some damage"
    elif (intensity < SERIOUS_DAMAGE):
        result = "Serious damage: walls may crack or fall"
    elif (intensity < DISASTER):
        result = "Disaster: buildings may collapse"
    else:
        result = "Catastrophe: most buildings destroyed"

    # Return values

    return result


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
        'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    # Define variables

    location = ""

    # Process some conditions

    if ((x == 0) and (y == x)):
        location = "Origin"
    elif ((x == 0) and (y != x)):
        location = "Y-Axis"
    elif ((x != 0) and (y == 0)):
        location = "X-Axis"
    elif ((x > 0) and (y > 0)):
        location = "Quadrant 1"
    elif ((x > 0) and (y < 0)):
        location = "Quadrant 4"
    elif ((x < 0) and (y > 0)):
        location = "Quadrant 2"
    else:
        location = "Quadrant 3"

    # Return values

    return location


def pay_raise(status: str, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    # Define variables
    new_salary = 0

    # Process some conditions

    if (status.lower() == "f" and years >= 10):
        new_salary = salary + (salary * FULL_TIME_LONG)
    elif (status.lower() == "f" and years < 4):
        new_salary = salary + (salary * FULL_TIME_SHORT)
    elif (status.lower() == "p" and years > 10):
        new_salary = salary + (salary * PART_TIME_LONG)
    elif (status.lower() == "p" and years < 4):
        new_salary = salary + (salary * PART_TIME_SHORT)
    else:
        new_salary = salary + (salary * OTHERS)

    # Return values

    return new_salary


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    # Define variables

    years_employed = int(input("Years employed: "))
    qualified = False

    # Process some conditions

    if (years_employed >= LOAN_MIN_YEARS):
        annual_salary = int(input("Annual salary: "))
        if (annual_salary >= LOAN_MIN_SALARY):
            qualified = True
        else:
            qualified = False
    else:
        qualified = False

    # Return values

    print()
    return qualified


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    # Define variables

    age = int(input("How old are you? "))
    price = 0

    # Process some conditions

    if (age < INFANT):
        price = INFANT_PRICE
    elif (age >= SENIOR):
        price = SENIOR_PRICE
    elif (STUDENT_MIN <= age and age < STUDENT_MAX):
        is_student = input("Are you a student at this school? (Y/N) ")

        if (is_student.lower() == "y"):
            price = STUDENT_PRICE_IN
        else:
            price = STUDENT_PRICE_OUT
    elif (ADULT_MIN <= age and age < ADULT_MAX):
        price = ADULT_PRICE
    else:
        price = KID_PRICE

    # Return values

    print()
    return price


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """

    # Define variables and get user input

    price = 0
    main = input("Order B - burger or W - wings: ")

    # Process some conditions

    if (main == "B"):
        price = BURGER_PRICE
    else:
        price = WINGS

    # Get user input

    combo = input("Make it a combo? (Y/N): ")

    # Process some conditions

    if (combo == "Y"):
        side = input("Add F - fries or S - salad: ")

        if (side == "F"):
            price = price + FRIES
        else:
            price = price + SALAD
    else:
        price = price

    # Return values

    print()
    return price
