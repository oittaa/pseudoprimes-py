"""
https://en.wikipedia.org/wiki/Baillie-PSW_primality_test
"""

from . import lucas, miller_rabin


def is_baillie_psw_prp(n: int) -> bool:
    """
    Baillie–PSW primality test.

    Arguments:
        {n} integer -- Number to test.
    Returns:
        True -- If {n} is (probably) a prime.
        False -- If {n} is not a prime.
    """
    return miller_rabin.is_miller_rabin_prp(n, (2,)) and lucas.is_extra_strong_lucas_prp(n)

    # Add a random M-R base
    # bases = (2, secrets.SystemRandom().randrange(3, n - 1))
    # return miller_rabin.is_miller_rabin_prp(n, bases) and lucas.is_extra_strong_lucas_prp(n)
