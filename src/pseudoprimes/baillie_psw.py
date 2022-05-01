"""
https://en.wikipedia.org/wiki/Baillie-PSW_primality_test
"""

from .lucas import is_extra_strong_lucas_prp
from .miller_rabin import is_miller_rabin_prp


def is_baillie_psw_prp(n: int) -> bool:
    """
    Baillie–PSW primality test.

    Arguments:
        {n} integer -- Number to test.
    Returns:
        True -- If {n} is (probably) a prime.
        False -- If {n} is not a prime.
    """
    return is_miller_rabin_prp(n, (2,)) and is_extra_strong_lucas_prp(n)

    # Add a random M-R base
    # bases = (2, secrets.SystemRandom().randrange(3, n - 1))
    # return is_miller_rabin_prp(n, bases) and is_extra_strong_lucas_prp(n)
