"""Fuctions relating to ISBN-10"""


def is_valid(isbn):
    """
    :param isbn: str - a possible ISBN-10
    :return: bool - Is is a ISBN-10?
    """
    clean = list(isbn.replace("-", "").lower())
    if clean and clean[-1] == "x":
        clean[-1] = "10"
    return (
        len(clean) == 10
        and all(digit.isdigit() for digit in clean)
        and sum(int(digit) * k for digit, k in zip(clean, range(10, 0, -1))) % 11 == 0
    )
