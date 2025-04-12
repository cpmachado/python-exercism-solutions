"""Module containing solution to leap exercise"""


def leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year

    :param year: int - The year being checked
    :return: bool -  True if the year is a leap year
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
