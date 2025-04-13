"""
Implementing a pig Latin translator
"""

from itertools import takewhile


def translate(text: str) -> str:
    """
    :param text: str - a text to be translated
    :return: str - translated text to pig latin
    """
    vowels = ("a", "e", "i", "o", "u")
    rule1_prefix_extra = ("xr", "yt")

    words = []

    for s in text.split(" "):
        # rule 1
        if any(s.startswith(x) for x in (*vowels, *rule1_prefix_extra)):
            words.append(s + "ay")
            continue

        # rule 4
        n = sum(
            1
            for _ in takewhile(
                (
                    lambda c: not c.startswith("y")
                    and all(not c.startswith(x) for x in vowels)
                ),
                s,
            )
        )
        if n > 0 and s[n] == "y":
            words.append(s[n:] + s[:n] + "ay")
            continue

        # rule 2
        n = sum(
            1
            for _ in takewhile((lambda c: all(not c.startswith(x) for x in vowels)), s)
        )
        # rule 3
        if s[n - 1] == "q" and s[n] == "u":
            n += 1
        words.append(s[n:] + s[:n] + "ay")

    return " ".join(words)
