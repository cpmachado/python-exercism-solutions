"""Functions relating to isograms"""


def is_isogram(string: str) -> bool:
    """
    :param string: str - a word
    :return: bool - is isogram
    """
    l = "".join(char for char in string.lower() if char.isalpha())
    return all(s not in l[i + 1 :] for i, s in zip(range(len(string)), l))
