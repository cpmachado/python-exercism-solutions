"""Functions relating to pangram"""

from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    """
    :param sentence: str - A given sentence
    :return: bool - Is is a pangram?
    """
    return all(letter in set(sentence.lower()) for letter in ascii_lowercase)
