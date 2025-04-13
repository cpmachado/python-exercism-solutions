"""Functions relating to dart game"""

from numbers import Number


def score(x: Number, y: Number) -> Number:
    """
    Computes the score of a given throw
    :param x: Number - x coordinate
    :param y: Number - y coordinate
    :return: Number - score
    """
    d = x**2 + y**2
    if d > 100:
        return 0
    if d > 25:
        return 1
    if d > 1:
        return 5
    return 10
