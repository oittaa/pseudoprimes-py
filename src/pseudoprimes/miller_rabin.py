"""
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""
from typing import Sequence


def is_miller_rabin_prp(n: int, bases: Sequence[int]) -> bool:
    """
    Perform a Miller-Rabin strong pseudoprime test on n.

    Returns False if n is definitely composite, and True if n is a probable
    prime.
    """

    if n == 2:
        return True
    if n < 2 or n & 1 == 0:
        return False
    d, s = n >> 1, 1
    while d & 1 == 0:
        d, s = d >> 1, s + 1

    for a in bases:
        a = a % n
        if a != 0 and not _witness(a, d, n, s):
            return False
    return True


def _witness(a: int, d: int, n: int, s: int) -> bool:
    """
    Miller-Rabin strong pseudoprime test for one base.
    Return False if n is definitely composite, True if n is
    probably prime, with a probability greater than 3/4.
    """
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(1, s):
        x = pow(x, 2, n)
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False
