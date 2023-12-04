import second


def one(number):
    return number + 8


def two(number):
    return number - 2


def three(number):
    return one(number) * two(number)


def four(number):
    return second.three(number)
