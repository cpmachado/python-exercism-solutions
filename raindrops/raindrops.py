"""
Raindrop challenge function
"""


def convert(number: int) -> str:
    """
    Converts number through raindrop logic

    :param number: int - a given integer
    :return: str - raindrop logic
    """
    ret = ""
    if number % 3 == 0:
        ret += "Pling"
    if number % 5 == 0:
        ret += "Plang"
    if number % 7 == 0:
        ret += "Plong"

    if not ret:
        ret = str(number)

    return ret
