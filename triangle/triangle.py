"""
Functions about triangles
"""

from numbers import Number


def fullfills_triangle_inequality(sides: list[Number]) -> bool:
    """
    Checks triangle inequality

    :param sides: list[Number] - sides of a given triangle
    :return: bool - True if it's a valid triangle
    """
    if len(sides) != 3 or any(map((lambda x: x == 0), sides)):
        return False
    a, b, c = sides

    return a + b >= c and b + c >= a and a + c >= b


def equilateral(sides: list[Number]) -> bool:
    """
    Checks if it's an equilateral triangle

    :param sides: list[Number] - sides of a given triangle
    :return: bool - True if it's  an equilateral triangle
    """
    if not fullfills_triangle_inequality(sides):
        return False
    a, b, c = sides
    return a == b and b == c


def isosceles(sides: list[Number]):
    """
    Checks if it's an isosceles triangle

    :param sides: list[Number] - sides of a given triangle
    :return: bool - True if it's an isosceles triangle
    """
    if not fullfills_triangle_inequality(sides):
        return False
    a, b, c = sides

    return a == b or b == c or a == c


def scalene(sides: list[Number]) -> bool:
    """
    Checks if it's a scalene triangle

    :param sides: list[Number] - sides of a given triangle
    :return: bool - True if it's a scalene triangle
    """
    if not fullfills_triangle_inequality(sides):
        return False
    a, b, c = sides

    return a != b and b != c and a != c
