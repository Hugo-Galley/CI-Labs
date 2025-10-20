"""Phantom package

Minimal package used by CI lab: exposes a few utility functions
"""

__all__ = [
    "add",
    "divide",
    "is_prime",
    "factorial",
    "gcd",
    "mean",
    "primes_in_range",
]

__version__ = "0.1.0"

from .math_utils import (
    add,
    divide,
    is_prime,
    factorial,
    gcd,
    mean,
    primes_in_range,
)  # noqa: F401
