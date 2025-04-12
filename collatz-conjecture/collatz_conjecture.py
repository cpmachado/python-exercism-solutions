"""
Functions on the Collatz Conjecture

"""


def steps(number):
    """
    :param number: int - Number used as starting point
    :return: int - Number of steps until it reaches 1
    """
    count = 0

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        count += 1

    return count
