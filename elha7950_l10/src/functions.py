"""
-------------------------------------------------------
Lab 10, Tasks 1-14

Description: 
    Functions for all the tasks.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# Constants

# Helper functions


def sum_of_list(nums: list):
    """
    -------------------------------------------------------
    Finds the sum of a list of numbers.
    Use: sum([1,2,3,4,5])
    -------------------------------------------------------
    Parameters: 
        nums - A list of integers. (list[int])
    Returns: 
        total - The total (int)
    """

    # Define the total variable

    total = 0

    # For each number add it to the total

    for num in nums:
        total += num

    # Return the total (sum)

    return total


def average(nums: list):
    """
    -------------------------------------------------------
    Finds the average of a list of numbers.
    Use: average([1,2,3,4,5])
    -------------------------------------------------------
    Parameters:
        nums - list of integers.
    Returns:
        average - average of the list of integers (float)
    -------------------------------------------------------
    """
    # Call the total helper function

    total = sum(nums)

    # Return the average

    return (total/len(nums))


def convert_to_nums(nums: list):
    """
    -------------------------------------------------------
    Converts a list of strings into a list of numbers. 
    Use: convert_to_nums(['1','2','3'])
    -------------------------------------------------------
    Parameters: 
        nums - list of strings (list[str])
    Returns: 
        new_nums - list of numbers (list[int])
    -------------------------------------------------------
    """
    # Define a list where the new numbers are going to be appended.

    new_nums = []

    # Convert the number into an int and append it to the list

    for num in nums:
        new_nums.append(int(num.strip()))

    # Return the numbers.

    return new_nums

# Functions


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """

    # Read all the lines

    data = fh.readlines()

    # If the line number is bigger than the number of lines in the whole entire file, return an empty list
    # Else, get the list information, strip the whitespace and split it by comma

    if (n > len(data)):
        result = []
    else:
        result = data[n].strip().split(",")

    # Return whatever result.

    return result


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = fh.readline().strip()

    while (line != ""):
        data = line.strip().split(",")
        ID = data[0]

        if (int(ID) == int(id_number)):
            result = data
            break
        else:
            line = fh.readline()
            continue

    return result


def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """

    customers = fh.readlines()

    highest = float("-infinity")
    result = []

    for customer in customers:
        customer_data = customer.strip().split(",")
        balance = float(customer_data[3])

        if (balance > highest):
            highest = balance
            result = customer_data

    return result


def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """

    # Read each individual line
    # Define result variable and lowest variable to keep track of the lowest date.

    line = fh.readline().strip()
    lowest = "999999"
    result = []

    while line:
        data = line.split(",")
        date = data[4]

        if (date < lowest):
            lowest = date
            result = data

        line = fh.readline().strip()

    return result


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
        None
    -------------------------------------------------------
    """
    COMMA_SEPARATOR = ","

    new_data = []

    for data in fields:
        new_data.append(str(data))

    fh.write(f"\n{COMMA_SEPARATOR.join(new_data)}")
    return


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """

    data = fh.readlines()

    smallest = float("infinity")
    biggest = float("-infinity")
    new_nums = convert_to_nums(data)
    total = sum_of_list(new_nums)
    aver = average(new_nums)

    for num in new_nums:
        if (num < smallest):
            smallest = num
        if (num > biggest):
            biggest = num

    return (smallest, biggest, total, aver)


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """

    data = fh.readlines()
    new_data = []

    for num in data:
        new_data.append(int(num.strip()))

    new_data.sort()

    highest = new_data[-1]
    fh.write(f"\n{highest}")

    return highest


def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    data = fh.readlines()
    new_data = []

    for num in data:
        new_data.append(int(num.strip()))

    highest = new_data[-1]
    fh.write(f"\n{highest + 1}")

    return (highest + 1)


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    data = fh.readlines()
    new_data = []

    for num in data:
        new_data.append(int(num.strip()))

    return new_data.count(int(value))


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    data = fh.readlines()
    new_data = []

    for w in data:
        new_data.append(w.strip())

    return new_data.count(word)


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    data = fh.readlines()

    length = 0
    longest_word = ""

    for word in data:
        if (len(word) >= length):
            length = len(word)
            longest_word = word.strip()

    return longest_word


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    data = fh.readlines()
    length = 10000
    shortest_word = ""

    for word in data:
        if (len(word) < length):
            length = len(word)
            shortest_word = word.strip()

    return shortest_word


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    data = fh_1.readlines()

    for line in data:
        fh_2.write(f"{line}")

    return


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    # Read all the lines

    data = fh_1.readlines()

    # Convert the number into an integer incase?

    number = int(n)

    # While True

    while True:
        # If the length of the list

        if (len(data) > number):
            for i in range(number):
                fh_2.write(data[i])
            break
        else:
            for i in range(len(data)):
                fh_2.write(data[i])
            number -= len(data)
            break
    return
