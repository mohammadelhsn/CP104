"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Mohammad El-Hassan
ID:     169067950
Email:  elha7950@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""

# Constants

VOWELS = ['a', 'e', 'i', 'o', 'u']


def upper_vowels(string: str):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌‌​​​‌​‌‌​‌​‌‌‌​:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    # Your code here

    altered = ""

    for letter in string:
        if ((letter.lower()) in VOWELS):
            altered += letter.upper()
        elif (letter.isdigit()):
            altered += letter
        else:
            altered += letter.lower()

    return altered
