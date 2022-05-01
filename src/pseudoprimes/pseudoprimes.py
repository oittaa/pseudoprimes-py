"""
Test and find prime numbers.
"""

import secrets
from typing import Union

from . import baillie_psw, constants, miller_rabin

_RAND = secrets.SystemRandom()


def is_prime(n: int) -> bool:
    """
    Test if n is a prime number (True) or not (False). For n ~2^81 the
    answer is definitive; larger n values have a small probability of actually
    being pseudoprimes.

    For small numbers, a set of deterministic Miller-Rabin tests are performed
    with bases that are known to have no counterexamples in their range.
    Finally if the number is larger than ~2^81, a strong BPSW test is
    performed. While this is a probable prime test and it is believed that
    counterexamples exist, currently there are no known counterexamples.

    https://en.wikipedia.org/wiki/Baillie-PSW_primality_test

    Arguments:
        {n} integer -- Number to test.
    Returns:
        True -- If {n} is (probably) a prime.
        False -- If {n} is not a prime.
    """
    if (result := _small_prime_test(n)) in (True, False):
        return result

    # Deterministic Miller-Rabin
    for best_solution, bases in constants.MR_DETERMINISTIC_SOLUTIONS:
        if n < best_solution:
            return miller_rabin.is_miller_rabin_prp(n, bases)

    # Baillie-PSW
    return baillie_psw.is_baillie_psw_prp(n)


def _small_prime_test(n: int) -> Union[bool, None]:
    """
    The point here is just to speedily handle small numbers and many
    composites. It is completely optional.

    Arguments:
        {n} integer -- Number to test.
    Returns:
        True -- If {n} is a prime.
        False -- If {n} is not a prime.
        None -- If {n} is unknown.
    """
    if n in (2, 3, 5):
        return True
    if n < 2 or n & 1 == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False
    if n < 49:
        return True
    if (
        (n % 7) == 0
        or (n % 11) == 0
        or (n % 13) == 0
        or (n % 17) == 0
        or (n % 19) == 0
        or (n % 23) == 0
        or (n % 29) == 0
        or (n % 31) == 0
        or (n % 37) == 0
        or (n % 41) == 0
        or (n % 43) == 0
        or (n % 47) == 0
    ):
        return False
    if n < 2809:
        return True
    if n < 31417:
        return pow(2, n, n) == 2 and n not in (7957, 8321, 13747, 18721, 19951, 23377)

    # Testing with known primes under 1000 speeds up the average test time by
    # 50% on 2048 bit numbers.
    for p in constants.KNOWN_PRIMES_50_TO_1000:
        if n % p == 0:
            return False

    return None


def next_prime(n: int) -> int:
    """
    Returns the next prime number greater than n.
    Arguments:
        {n} integer -- Integer number
    Returns:
        integer -- The next prime number greater than n.
    """
    if n < 2:
        return 2
    if n < 7:
        return {2: 3, 3: 5, 4: 5, 5: 7, 6: 7}[n]
    nn = 6 * (n // 6)
    if nn == n:
        n += 1
        if is_prime(n):
            return n
        n += 4
    elif n - nn == 5:
        n += 2
        if is_prime(n):
            return n
        n += 4
    else:
        n = nn + 5
    while True:
        if is_prime(n):
            return n
        n += 2
        if is_prime(n):
            return n
        n += 4


def prev_prime(n: int) -> int:
    """
    Returns the previous prime number less than n. n must be greater than 2.
    Arguments:
        {n} integer -- Integer number
    Raises:
        ValueError -- Wrong value for {n} parameter, must be greater than 2.
    Returns:
        integer -- The previous prime number less than n.
    """
    if n < 3:
        raise ValueError(
            "prev_prime() expects parameter n to be greater than 2. "
            "Given: " + str(n) + "."
        )
    if n < 8:
        return {3: 2, 4: 3, 5: 3, 6: 5, 7: 5}[n]
    nn = 6 * (n // 6)
    if n - nn <= 1:
        n = nn - 1
        if is_prime(n):
            return n
        n -= 4
    else:
        n = nn + 1
    while True:
        if is_prime(n):
            return n
        n -= 2
        if is_prime(n):
            return n
        n -= 4


def get_prime(bits: int) -> int:
    """
    Returns a prime. bits is the desired length of the prime.
    Arguments:
        {bits} integer -- Integer number
    Raises:
        ValueError -- Wrong value for {bits} parameter, must be greater than 1.
    Returns:
        integer -- The generated prime.
    """
    if bits < 2:
        raise ValueError(
            "gen_prime() expects parameter bits to be greater than 1. "
            "Given: " + str(bits) + "."
        )
    if bits == 2:
        return _RAND.randrange(2, 4)
    while True:
        value = _RAND.randrange(1 << (bits - 1), 1 << bits) | 1
        if is_prime(value):
            return value
