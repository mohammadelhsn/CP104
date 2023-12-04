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

# Constants

# Functions


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = file_handle.readlines()

    # Initialize a counter variable
    i = 0

    # Iterate using a while loop
    while i < min(count, len(lines)):
        print(lines[i].strip())
        i += 1

    return


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    lines = file_handle.readlines()

    number_list = []

    for line in lines:
        for el in line.split(','):
            if (el.isdigit()):
                number_list.append(int(el))
    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0

    lines = file_handle.readlines()

    for line in lines:
        for char in line:
            if (char.isupper()):
                ucount += 1
            elif (char.islower()):
                lcount += 1
            elif (char.isdigit()):
                dcount += 1
            elif (char.isspace()):
                wcount += 1
            else:
                rcount += 1

    return (ucount, lcount, dcount, wcount, rcount)


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = fh_read.readlines()

    for i in range(len(lines)):
        fh_write.write(f'[{i}] {lines[i]}')

    return


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    lines = file_handle.readlines()
    lowest = 99999999999
    highest = -100000000
    l_id = 0
    h_id = 0
    total = 0

    for line in lines:
        data = line.strip().split(",")
        id = int(data[2])
        grade = int(data[3])
        total += grade
        if (grade < lowest):
            l_id = id
            lowest = grade
        elif (grade > highest):
            h_id = id
            highest = grade

    return (str(l_id), str(h_id), (total/len(lines)))
