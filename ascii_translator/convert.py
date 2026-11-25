"""Pure conversion logic, no GUI imports so it can be tested anywhere. Author: WR"""


def text_to_ascii(text: str) -> str:
    """Return the decimal code of every character, separated by spaces."""
    return " ".join(str(ord(char)) for char in text)


def ascii_to_text(codes: str) -> str:
    """Turn space-separated decimal codes back into text.

    Raises ValueError with the offending token when a code is not a number
    or is outside the Unicode range.
    """
    chars = []
    for token in codes.split():
        try:
            chars.append(chr(int(token)))
        except (ValueError, OverflowError) as error:
            raise ValueError(token) from error
    return "".join(chars)
