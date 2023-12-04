"""
-------------------------------------------------------
Assignment 8, Tasks 1-5

Description:
    Functions for all the assignments. 
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports

# Constants

VALID_ISBN_LENGTH = 17

# Functions


def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """

    # Define a list for the words.

    words = []
    word = ""

    for i in range(len(sentence)):
        # If it's the first letter, add it and then keep going.

        if (i == 0):
            word += sentence[i]
            continue

        # If it's the last one, add the word to the list of words.

        if (i == len(sentence)-1):
            word += sentence[i]
            words.append(word)

        # If the letter is uppercase, it means it's a new word.
        # Make it lower case and keep it going.

        elif (sentence[i].isupper()):
            words.append(word)
            word = ""
            word += sentence[i].lower()
            continue

        # Otherwise it's not an important letter.

        else:
            word += sentence[i]

    # Return the spaced sentence.

    spaced = " ".join(words)
    return spaced


def pluralize(string: str):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """

    # Split the entire word into a list

    pluralized = list(string)

    if (string.endswith('y') and not string.endswith('ay') and not string.endswith('oy')):

        # Remove the y and add the suffix 'ies'.

        del pluralized[-1]
        pluralized += "ies"
    elif (string.endswith('s')):

        # Add the 'es'.

        pluralized += "es"
    elif (string.endswith('sh') or string.endswith('ch') or string.endswith('ox')):

        # Remove the last two 'sh' or 'ch' and add the 'es
        pluralized += "es"
    else:

        # By default add an 's'.

        pluralized += "s"

    # Join the word together from a list to a single word.

    pluralized = "".join(pluralized)

    # Return the word, pluralized.

    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    # Convert the words to lists to make manipulation easier.

    str1 = list(str1)
    str2 = list(str2)

    # Reverse the strings to simplify the common ending.

    str1.reverse()
    str2.reverse()

    # Define the suffix variable to store the common ending.

    suffix = ""

    # Initialize the index variable for traversal.

    i = 0

    # Traverse both strings from the end until a difference is found.

    while ((i < len(str2) and i < len(str1)) and str1[i] == str2[i]):
        suffix = str1[i] + suffix
        i += 1

    # Return the common suffix (if it exists).

    return suffix


def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    # Assume the ISBN is valid instantly.

    is_valid = True

    # Check if the length of the ISBN is valid.

    if (len(isbn) == VALID_ISBN_LENGTH):

        # Remove the dashes to facilitate better checks.

        isbn_without_dashes = isbn.replace("-", "")

        # Split the ISBN into groups using dashes.

        isbn_split = isbn.split("-")

        # Check if the ISBN contains only digits and dashes.

        if (not isbn_without_dashes.isdigit()):
            is_valid = False

        # Check if the first group of digits is '978' or '979'

        if (isbn[0:3] != "978" and isbn[0:3] != "979"):
            is_valid = False

        # Check if the last character is a digit.

        if (not isbn[-1].isdigit()):
            is_valid = False

        # Check if there are exactly 5 groups separated by by dashes, and none are empty.

        if (len(isbn_split) != 5 or '' in isbn_split):
            is_valid = False
    else:

        # If the length is not 17, the ISBN is invalid.

        is_valid = False

    # Return whether it is valid or not.

    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a list of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Initialize the variable to store the last character of the previous word.
    last_char = ""

    # Assume the word chain is valid initially.
    word_chain = True

    # Initialize an index variable.
    index = 0

    # Iterate through each word using a while loop.
    while index < len(words):
        word = words[index]

        # For the first word, set the last character and continue.
        if index == 0:
            last_char = word[-1]
            index += 1
            continue
        else:
            # Check if the first character of the current word matches the last character of the previous word.
            if word[0] == last_char:
                last_char = word[-1]
                index += 1
                continue
            # If the condition is not met, the word chain is False.
            else:
                word_chain = False
                break

    # Return validity.
    return word_chain
