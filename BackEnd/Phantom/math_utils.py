"""Small math utilities for CI lab.

Functions:
- add(a, b): return a + b
- divide(a, b): return a / b, raises ZeroDivisionError on zero
- is_prime(n): simple deterministic primality check for n >= 2
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def divide(a: Number, b: Number) -> float:
    """Divide a by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def is_prime(n: int) -> bool:
    """Return True if n is a prime number (n >= 2)."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def factorial(n: int) -> int:
    """Return n! for n >= 0. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        # Encore
        # J'ajoute un commentaire de e
        a, b = b, a % b
    return a


def mean(values: list[Number]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def primes_in_range(start: int, end: int) -> list[int]:
    """Return a list of primes in [start, end] (inclusive).

    This function is intentionally left without direct tests to simulate
    an uncovered function for CI coverage checks.
    """
    return [n for n in range(max(2, start), end + 1) if is_prime(n)]
