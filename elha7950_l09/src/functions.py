"""
-------------------------------------------------------
Lab 9, Tasks 1-15

Description: 
    Functions for tasks 1-15
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
# Imports

# Constants

VOWELS = ["a", "e", "i", "o", "u"]
SPECIAL_CHARS = ["#", "@", "$", "%", "&", "!"]
ADDITION_CHAR = "+"
SUBTRACTION_CHAR = "-"
MULTIPLICATION_CHAR = "*"
MODULUS = "%"

# Functions


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Define variable

    hydroxide = False

    # Check if the last 2 letters OH
    # Else is not needed, because by default, it is False

    if ((chemical[-2] == "O") and (chemical[-1] == "H")):
        hydroxide = True

    # Return value

    return hydroxide


def url_categorize(url: str):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """

    # Define variable

    url_type = ""

    # If the string ends with com, it is a business
    # If the string ends with org, it is a non-profit
    # Otherwise it is other

    if (url.endswith("com")):
        url_type = "business"
    elif (url.endswith("org")):
        url_type = "non-profit"
    else:
        url_type = "other"

    # Return value

    return url_type


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """

    # Define variables

    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:len(product_code)]

    # Return values

    return pc, pi, pq


def validate_code(product_code: str):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """

    # Define variables

    category = False
    digits = False
    qualifiers = False
    LENGTH = len(product_code)

    # If the length is bigger than 7, that means each exists.

    if (LENGTH > 7):
        _category = product_code[0:3]
        _digits = product_code[3:7]
        _qualifiers = product_code[7:LENGTH]

        # Check to make sure each is valid.

        if (_category.isupper()):
            category = True
        if (_digits.isdigit()):
            digits = True
        if (_qualifiers[0].isupper()):
            qualifiers = True
    elif (LENGTH > 2):

        # The product code is definitely there, we aren't sure if it's valid yet, but it is long enough
        # The digits may or may not be there.

        if (LENGTH > 3):

            # Define variables.

            _category = product_code[0:3]
            _digits = product_code[3:LENGTH]

            # Validate according to assignment instructions.

            if (_category.isupper()):
                category = True
            if ((len(_digits) == 4) and (_digits.isdigit())):
                digits = True

        elif ((LENGTH == 3) and (product_code[0:3].isupper())):
            category = True

    # Return values.

    return (category, digits, qualifiers)


def password_strength(password: str):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """

    # Define variables

    no_digits = True
    no_upper_case = True
    no_lower_case = True
    LENGTH = len(password)

    for char in password:

        # Check if there are digits

        if (char.isdigit()):
            no_digits = False
            continue

        # Check if there is upper case

        elif (char.isupper()):
            no_upper_case = False
            continue

        # Check if there is a lower case

        elif (char.islower()):
            no_lower_case = False
            continue

        # Else continue.

        else:
            continue

    # Check length

    if (LENGTH < 8):
        print("not long enough")

    # Check if no digits is still true.

    if (no_digits):
        print("no digits")

    # Check if no upper case still true.

    if (no_upper_case):
        print("no upper case")

    # Check if no lower case.

    if (no_lower_case):
        print("no lower case")

    # Return.

    return


def is_palindrome(s: str):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """

    # Put each character into the list.

    string_list = list(s)

    # Reverse the list

    string_list.reverse()

    # Make the new word.

    new_str = "".join(string_list)

    # Define the variable

    palindrome = False

    # If they're still the same, then it is a palindrome.

    if (new_str.lower() == s.lower()):
        palindrome = True

    # Return value.

    return palindrome


def vowel_count(s: str):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """

    # Define variable.

    count = 0

    for char in s:

        # If the character is a vowel, add a count.
        # Else, pass and don't add.

        if (char.lower() in VOWELS):
            count += 1
        else:
            pass

    # Return the count.

    return count


def digit_count(s: str):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """

    # Define variable

    count = 0

    # If the character is a digit, add one.
    # Else, continue.

    for char in s:
        if (char.isdigit()):
            count += 1

    # Return count of digits.

    return count


def count_special_chars(s: str):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """

    # Define count variable.

    count = 0

    # If character is a special character, add one to the counter.
    # Else, pass.

    for char in s:
        if (char in SPECIAL_CHARS):
            count += 1

    # Return the count.

    return count


def text_analyze(txt: str):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """

    # Define counter variables.

    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for char in txt:

        # Check if the character is upper case and add to the count.

        if (char.isupper()):
            uppr += 1
            pass

        # Check if the character is lower case and add to the count.

        if (char.islower()):
            lowr += 1
            pass

        # Check if the character is a digit.

        if (char.isdigit()):
            dgts += 1
            pass

        # Check if it's a space.

        if (char.isspace()):
            whtspc += 1
            pass

    # Return values.

    return (uppr, lowr, dgts, whtspc)


def dsmvwl(string: str):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(sstring)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with its vowels removed (str)
    -------------------------------------------------------
    """

    # Split each word into a list.

    words = string.split(" ")
    new_sentence = []

    # For each word in list of words, go over each character in that word and if it is
    # Not a vowel, add it to the new_word. If it is don't.
    # Append the new word to the list

    for word in words:
        new_word = ""
        for char in word:
            if (char.lower() not in VOWELS):
                new_word += char
            else:
                pass
        new_sentence.append(new_word)

    # Re-make the sentence

    out = " ".join(new_sentence)

    # Return value.

    return out


def comma_period_replace(string: str): """-------------------------------------------------------Replaces all the commas with a period in s.Use: out = comma_period_replace(string)-------------------------------------------------------Parameters:string - a string (str)Returns:out - string with all commas replaced by a period (str)------------------------------------------------------"""; out = string.replace(",", "."); return out


def total_digits(string: str):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(string)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in string (int)
    ------------------------------------------------------
    """

    # Define total variable.

    total = 0

    # For letter, if it's a digit, add the digit to the total.

    for char in string:
        if (char.isdigit()):
            total += int(char)
        pass

    # Return total.

    return total


def str_distance(s1: str, s2: str):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """

    # Define the variable for distance

    d = 0

    # If the length of the two strings are different, then as per instructions
    # The distance is -1

    if (len(s1) != len(s2)):
        d = -1
    else:

        # Define index variable.

        index = 0

        # Check if they're the same at the same index.
        # If they're not, add one to distance, add 1 to the index and continue.

        for i in range(len(s1)):
            if (s1[index] != s2[index]):
                d += 1
            index += 1
            pass

    # Return distance.

    return d


def calculate(expr: str):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """

    # Define total and digits variables.

    result = 0
    digits = []

    # Find the digits and append them to the list.

    for char in expr:
        if (char.isdigit()):
            digits.append(int(char))
        pass

    # Define variables for our digits.

    digit1 = digits[0]
    digit2 = digits[1]

    # Find out which operation is being used, and perform the operation.
    # If the operation is division or modulus, make sure it's not dividing by 0.

    if (ADDITION_CHAR in expr):
        result = digit1 + digit2
    elif (SUBTRACTION_CHAR in expr):
        result = digit1 - digit2
    elif (MULTIPLICATION_CHAR in expr):
        result = digit1 * digit2
    elif (MODULUS in expr):
        if (digit2 == 0):
            result = 0
        else:
            result = digit1 % digit2
    else:
        if (digit2 == 0):
            result = 0
        else:
            result = digit1 / digit2

    # Return result.

    return result
