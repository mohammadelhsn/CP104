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

    matrix = []
    for i in range(rows):
        r = []
        for ii in range(cols):
            if (value_type == "float"):
                r.append(uniform(low, high))
            else:
                r.append(randint(low, high))
        matrix.append(r)

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

    matrix = []

    for i in range(rows):
        r = []
        for ii in range(cols):
            letter = LETTERS[randint(0, len(LETTERS)-1)]
            r.append(letter)
        matrix.append(r)

    return matrix


matrix = generate_matrix_num(3, 4, -10, 10, "float")


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
    col_str = f' '
    row_strs = []

    for i in range(len(matrix[0])):
        col_str += f'{i:7d}'

    for i in range(len(matrix)):
        row = matrix[i]
        row_str = f"{i}"
        for ii in range(len(row)):
            col = matrix[i][ii]
            if (value_type == "int"):
                row_str += f'{col:7d}'
            else:
                row_str += f'{col:7.2f}'
        row_strs.append(row_str)

    print(col_str)

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

    col_str = f''
    row_strs = []

    for i in range(len(matrix[0])):
        col_str += f'{i:1d}'

    for i in range(len(matrix)):
        row = matrix[i]
        row_str = f"{i}"
        for ii in range(len(row)):
            col = matrix[i][ii]
            row_str += f'{col:1s}'
        row_strs.append(row_str)

    print(col_str)

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
    word_length = len(word_list[0])

    # Create the matrix
    matrix = [[word[i] for i in range(word_length)] for word in word_list]

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
    smallest = float('inf')
    largest = float('-inf')
    total = 0

    # Calculate statistics
    num_elements = 0
    for row in matrix:
        for num in row:
            if isinstance(num, (int, float)):
                smallest = min(smallest, num)
                largest = max(largest, num)
                total += num
                num_elements += 1

    # Calculate average
    average = total / num_elements

    return smallest, largest, total, average


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
    smallest = float('inf')
    largest = float('-inf')
    s_loc = None
    l_loc = None

    # Iterate through the matrix to find the positions
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value < smallest:
                smallest = value
                s_loc = [row_index, col_index]
            if value > largest:
                largest = value
                l_loc = [row_index, col_index]

    return s_loc, l_loc


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
    loc = []
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value < n:
                loc = [row_index, col_index]
                break

    # If no such value is found, return an empty list
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
    count = 0

    # Iterate through the matrix to count the appearances of char
    for row in matrix:
        count += row.count(char)

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
    rows = []

    # Iterate through each row of the matrix
    for row_index, row in enumerate(matrix):
        # Convert the row to a string and check if it equals the word
        if ''.join(row) == word:
            rows.append(row_index)

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
    # Number of columns in the matrix
    num_columns = len(matrix[0])

    # List to store column indexes
    cols = []

    # Iterate through each column of the matrix
    for col_index in range(num_columns):
        # Extract the characters from the column
        column_chars = [matrix[row_index][col_index]
                        for row_index in range(len(matrix))]

        # Convert the column to a string and check if it equals the word
        if ''.join(column_chars) == word:
            cols.append(col_index)

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
    found = True
    # Length of the matrix
    matrix_length = len(matrix)

    # Iterate through the main diagonal of the matrix
    for i in range(matrix_length):
        # Check if the diagonal contains the given word
        if matrix[i][i] != word[i]:
            found = False

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
    # Iterate through each row of the matrix
    for i in range(len(matrix)):
        # Iterate through each column of the matrix
        for j in range(len(matrix[i])):
            # Multiply each element by the scalar
            matrix[i][j] *= num

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
    # Determine the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    # Create an empty transposed matrix with swapped dimensions
    transposed = [[0 for _ in range(num_rows)] for _ in range(num_columns)]

    # Iterate through each element of the original matrix and transpose
    for i in range(num_rows):
        for j in range(num_columns):
            transposed[j][i] = matrix[i][j]

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
    equal = True
    for i in range(len(matrix1)):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            equal = False
            break
        for j in range(len(matrix1[0])):
            # Compare corresponding elements
            if matrix1[i][j] != matrix2[i][j]:
                equal = False

    # If all elements are equal, matrices are equal
    return equal
