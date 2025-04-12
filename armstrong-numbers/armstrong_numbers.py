"""
Functions relating to Armstrong numbers
"""


def is_armstrong_number(number):
    """
    :param number: int - number being checked
    :return: bool - Is it an Armstrong number?
    """
    number_as_string = str(number)
    k = len(number_as_string)

    return number == sum(int(x) ** k for x in number_as_string)
