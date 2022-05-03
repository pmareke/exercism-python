import math
import string


def lookup(a, b, reverse=False):
    if math.gcd(a, 26) > 1:
        raise ValueError("a and m must be coprime.")

    lookup = "".join(
        chr(((ord(c) - ord("a")) * a + b) % 26 + ord("a"))
        for c in string.ascii_lowercase
    )

    if reverse:
        return str.maketrans(lookup, string.ascii_lowercase, string.whitespace)

    else:
        return str.maketrans(
            string.ascii_lowercase, lookup, string.whitespace + string.punctuation
        )


def encode(plain_text, a, b):
    encoded = plain_text.lower().translate(lookup(a, b))
    return " ".join(encoded[i : i + 5] for i in range(0, len(encoded), 5))


def decode(ciphered_text, a, b):
    return ciphered_text.lower().translate(lookup(a, b, reverse=True))
