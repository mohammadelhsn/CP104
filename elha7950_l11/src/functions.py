"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports

from random import uniform, randint
from string import ascii_lowercase

# Constants

LETTERS = list(ascii_lowercase)
SPACE_CHAR = " "

# Functions


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    # Initialize an empty 2D list to store the generated numbers.

    matrix = []

    # Iterate over the rows
    for i in range(rows):

        # Initialize an empty list for each row

        r = []

        # Iterate over the columns

        for ii in range(cols):

            # Append a random number based on the specified type, with the specified lows and highs.

            if (value_type == "float"):
                r.append(uniform(low, high))
            else:
                r.append(randint(low, high))

        # Append the row to the matrix.

        matrix.append(r)

    # Return the generated matrix.

    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """

    # Initialize an empty list for each row

    matrix = []

    # Iterate over the rows

    for i in range(rows):

        # Initialize an empty list for each row

        r = []

        # Iterate over the columns

        for ii in range(cols):

            # Choose a random letter from the ascii lowercase module
            # See definition on line 18.

            letter = LETTERS[randint(0, len(LETTERS)-1)]

            # Append the letter to the row

            r.append(letter)

        # Append the row to the matrix

        matrix.append(r)

    # Return the generated matrix of letters

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    # Initialize column string and row strings

    col_str = f' '
    row_strs = []

    # Create column headings

    for i in range(len(matrix[0])):
        col_str += f'{i:7d}'

    # Create row headings and matrix values

    for i in range(len(matrix)):
        row = matrix[i]
        row_str = f"{i}"
        for ii in range(len(row)):
            col = matrix[i][ii]

            # Format values based on the specified type

            if (value_type == "int"):
                row_str += f'{col:7d}'
            else:
                row_str += f'{col:7.2f}'
        row_strs.append(row_str)

    # Print column header

    print(col_str)

    # Print row headings and matrix values

    for s in row_strs:
        print(s)

    return


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """

    # Initialize column string and row strings

    col_str = ''
    row_strs = []

    # Create column headings with specified spacing

    for i in range(len(matrix[0])):
        col_str += f'{SPACE_CHAR * 3}{i}'

    # Create row headings and matrix values with specified spacing

    for i in range(len(matrix)):
        row = matrix[i]
        row_str = f"{i}"
        for ii in range(len(row)):
            col = row[ii]

            # Adjust spacing for the first column

            if (ii == 0):
                row_str += f'{SPACE_CHAR * 2}{col}'
            else:
                row_str += f'{SPACE_CHAR * 3}{col}'

        row_strs.append(row_str)

    # Print column headings

    print(col_str)

    # Print row headings and matrix values

    for s in row_strs:
        print(s)

    return


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
        in word_list (2D list of string).
    -------------------------------------------------------
    """

    # Initialize an empty 2D list to store the character value.

    matrix = []

    # Iterate through each word in the word_list

    for word in word_list:

        # Initialize an empty list for each word

        word_list = []

        # Iterate through each letter, appending it to the word list

        for letter in word:
            word_list.append(letter)

        # Append the list of characters to the matrix

        matrix.append(word_list)

    # Return the generated matrix.

    return matrix


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
                Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """

    # Initialize variables to store results

    smallest = float("infinity")
    largest = float("-infinity")
    total = 0
    nums = 0
    average = 0

    # Iterate through each element in the matrix

    for row in matrix:
        for col in row:

            # Convert the element into a float for comparison

            current_value = float(col)

            # Set current value to largest if it is greater

            if (current_value > largest):
                largest = current_value

            # Set current value to smallest if it is smaller

            if (current_value < smallest):
                smallest = current_value

            # Add the current value to the total regardless

            total += current_value

            # Add 1 to the total for average calculation

            nums += 1

    # Calculate the average

    average = total / nums

    # Return the results as a tuple

    return (smallest, largest, total, average)


def find_position(matrix):
    """
    Determines the first locations [row, column] of the smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)

    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of the row and column location of
            the largest value in matrix (list of int)
    """

    # Initialize variables to store smallest and largest values

    smallest = float('infinity')
    largest = float('-infinity')

    # Initialize variables to store locations of smallest and largest values

    s_loc = []
    l_loc = []

    # Iterate through each element in the matrix

    for i in range(len(matrix)):
        row = matrix[i]
        for ii in range(len(row)):
            col = row[ii]
            current_value = float(col)

            # Update the smallest value and its location

            if (current_value < smallest):
                smallest = current_value
                s_loc = [i, ii]

            # Update the largest value and its location

            if (current_value > largest):
                largest = current_value
                l_loc = [i, ii]

    # Return the two lits containing the locations of the smallest and largest values.

    return (s_loc, l_loc)


def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """

    # Initialize a list to store the location of the first value smaller than n

    loc = []

    # Iterate through each element in the matrix.

    for i in range(len(matrix)):
        row = matrix[i]

        # If the location is already found, exit the outer loop.

        if (len(loc) > 0):
            break

        for ii in range(len(row)):
            col = row[ii]

            # If the current value is smaller than n, update the location and exit the inner loop.

            if (float(col) < n):
                loc = [i, ii]
                break

    # Return the list containing the location or an empty list if no such value is found

    return loc


def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """

    # Initialize a variable to store the count of the given character

    count = 0

    # Iterate through each element in the matrix

    for row in matrix:
        for col in row:

            # If the current element matches the given character, increase the count

            if (col == char):
                count += 1

    # Return the count of appearances of the given character in the matrix.

    return count


def find_word_horizontal(matrix, word):
    """
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)

    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    """

    # Initialize a list to store row indexes where the word is found

    rows = []

    # Iterate through each row is in the matrix.

    for i in range(len(matrix)):
        row = matrix[i]

        # Convert the row to a string and check if it equals the target word

        joined_word = "".join(row)
        if (joined_word == word):
            rows.append(i)

    # Return the list of row indexes where the word is found.

    return rows


def find_word_vertical(matrix, word):
    """
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all columns that are equal to word.
    Returns an empty list if no column is equal to word.
    Use: cols = find_word_vertical(matrix, word)

    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        cols - a list of column indexes (list of int)
    """

    # Initialize a list to store column indexes where the word is found

    cols = []

    # Initialize a list to store vertical words

    words = []

    # Iterate through each row in the matrix

    for i in range(len(matrix)):
        row = matrix[i]
        for ii in range(len(row)):
            col = row[ii]

            # Initialize an empty string for each column if words list is not ready

            if (len(words) != len(row)):
                for _ in range(len(row)):
                    words.append("")

            # If the words list is ready, append the current character to the corresponding vertical word.

            if (len(words) == len(row)):
                words[ii] += col

    # Iterate through the vertical words and check if they equal the target word

    for i in range(len(words)):
        new_word = words[i]

        if (new_word == word):
            cols.append(i)

    # Return the list of column indexes where the word is found.

    return cols


def find_word_diagonal(matrix, word):
    """
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)

    Parameters:
        matrix - a 2D list of characters (2D list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    """

    # Initialize a variable to store whether the word is found on the diagonal.

    found = True

    # Length of the matrix

    matrix_length = len(matrix)

    # Iterate through the main diagonal of the matrix

    for i in range(matrix_length):

        # Check if the diagonal contains the given word
        # This works because as the row goes down, it goes across.
        # It starts at 0,0 and  moves to 1,1 and so on.

        if (matrix[i][i] != word[i]):
            found = False

    # Return whether the word is found on the diagonal.

    return found


def matrix_scalar_multiply(matrix, num):
    """
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)

    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    """

    # Iterate through each element in the matrix.

    for i in range(len(matrix)):
        row = matrix[i]
        for ii in range(len(row)):

            # Multiply each element by the given number.

            row[ii] *= num

    # The function modifies the matrix in place, so it returns None.

    return


def matrix_transpose(matrix):
    """
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix)

    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    """

    # Initialize a list to store the transposed matrix

    transposed = []

    # Iterate through each column in the original matrix.

    for i in range(len(matrix[0])):
        transposed.append([])

    # Iterate through each element in the original matrix.

    for i in range(len(matrix)):
        row = matrix[i]
        for ii in range(len(row)):

            # Append the element to the corresponding column in the transposed list.

            transposed[ii].append(row[ii])

    # Return the transposed matrix.

    return transposed


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of *)
        matrix2 - the second matrix (2D list of *)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    # Initializes a variable to store whether the matrices are equal

    equal = True

    for i in range(len(matrix1)):

        # Check if the matrices have the same dimensions

        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            equal = False
            break

        # Iterate through each element in the matrices

        for j in range(len(matrix1[0])):

            # Compare corresponding elements

            if matrix1[i][j] != matrix2[i][j]:
                equal = False

    # Return whether the matrices are equal

    return equal
