import pytest

from Phantom.math_utils import add, divide, is_prime

from Phantom.math_utils import factorial, gcd, mean


def test_add_integers():
    assert add(1, 2) == 3


def test_add_floats():
    assert add(1.5, 2.25) == pytest.approx(3.75)


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (1, False),
        (0, False),
        (-5, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) is expected


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_gcd():
    assert gcd(54, 24) == 6
    assert gcd(-54, 24) == 6


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        mean([])
