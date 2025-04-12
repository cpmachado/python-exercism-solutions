"""
Consider how to interact with bob
"""


def response(hey_bob: str) -> str:
    """
    What would Bob say.

    :param hey_bob: str - interaction with bob
    :return: str - Bob's response
    """
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")

    is_yelling = any(x.isalpha() for x in hey_bob) and all(
        not x.isalpha() or x.isupper() for x in hey_bob
    )

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."
