"""
Functions to compute the number of grains in a chess board.

It uses bit shifts and assumes a little endian architecture
"""


def square(number):
    """
    :param number: int - square to consider
    :return: int - number of grain in a given square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)


def total():
    """
    :return: int - number of grain in all squares
    """
    return (1 << 64) - 1
