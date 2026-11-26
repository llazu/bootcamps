import math


class NegativeValueError(ValueError):
    pass


def calculate_square_root(n):
    """Return the square root of n, or raise NegativeValueError."""
    if n < 0:
        raise NegativeValueError(f"{n} must be greater than 0")
    return math.sqrt(n)

print(calculate_square_root(9))

calculate_square_root(-9)

