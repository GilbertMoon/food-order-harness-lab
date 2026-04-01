from typing import Union

Number = Union[int, float]


def add_numbers(a: Number, b: Number) -> Number:
    """Return the sum of two numbers.

    Examples:
        >>> add_numbers(2, 3)
        5
    """
    return a + b
