"""
Test and find prime numbers.
"""

import secrets
from . import lucas
from . import miller_rabin

_RAND = secrets.SystemRandom()

__P = [53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]
__P += [137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]
__P += [223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
__P += [307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389]
__P += [397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479]
__P += [487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587]
__P += [593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673]
__P += [677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773]
__P += [787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881]
__P += [883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
_KNOWN_PRIMES = tuple(__P)
del __P


def is_prime(n: int) -> bool:
    """
    Test if n is a prime number (True) or not (False). For n < 2^81 the
    answer is definitive; larger n values have a small probability of actually
    being pseudoprimes.

    For small numbers, a set of deterministic Miller-Rabin tests are performed
    with bases that are known to have no counterexamples in their range.
    Finally if the number is larger than 2^81, a strong BPSW test is
    performed. While this is a probable prime test and it is believed that
    counterexamples exist, currently there are no known counterexamples.

    https://en.wikipedia.org/wiki/Baillie-PSW_primality_test

    Arguments:
        {n} integer -- Number to test.
    Returns:
        True -- If {n} is (probably) a prime.
        False -- If {n} is not a prime.
    """
    if n in (2, 3, 5):
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
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
    if n <= 23001:
        return pow(2, n, n) == 2 and n not in (7957, 8321, 13747, 18721, 19951)

    for p in _KNOWN_PRIMES:
        if n % p == 0:
            return False

    return miller_rabin.is_miller_rabin_prp(n) and (
        n < miller_rabin.MAX_DETERMINISTIC or lucas.is_strong_lucas_prp(n)
    )


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


def gen_prime(bits: int) -> int:
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
    while True:
        value = _RAND.randrange(2 ** (bits - 1), 2**bits)
        if is_prime(value):
            return value
