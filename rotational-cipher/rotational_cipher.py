"""Functions relating to rotational ciphers"""


def rotate(text, key):
    """
    :param text: str - plaintext
    :param key: int - key or displacement
    :return: str - ciphertext
    """
    return "".join(
        letter
        if not letter.isalpha()
        else chr((ord(letter) - ord("A") + key) % 26 + ord("A"))
        if letter.isupper()
        else chr((ord(letter) - ord("a") + key) % 26 + ord("a"))
        for letter in text
    )
