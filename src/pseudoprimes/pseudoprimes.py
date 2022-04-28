"""
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test
"""

# Returns exact according to http://primes.utm.edu/prove/prove2_3.html
_DETERMINISTIC_SOLUTIONS = (
    (1_373_653, (2, 3)),
    (9_080_191, (31, 73)),
    (4_759_123_141, (2, 7, 61)),
    (1_122_004_669_633, (2, 13, 23, 1662803)),
    (2_152_302_898_747, (2, 3, 5, 7, 11)),
    (3_474_749_660_383, (2, 3, 5, 7, 11, 13)),
    (341_550_071_728_321, (2, 3, 5, 7, 11, 13, 17)),
    # https://doi.org/10.1090%2FS0025-5718-2014-02830-5
    (3_825_123_056_546_413_051, (2, 3, 5, 7, 11, 13, 17, 19, 23)),
    # https://ui.adsabs.harvard.edu/abs/2015arXiv150900864S
    (318_665_857_834_031_151_167_461, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)),
    (
        3_317_044_064_679_887_385_961_981,
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41),
    ),
)

__P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
__P += [71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
__P += [149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223]
__P += [227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
__P += [307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383]
__P += [389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463]
__P += [467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569]
__P += [571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647]
__P += [653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743]
__P += [751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839]
__P += [853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941]
__P += [947, 953, 967, 971, 977, 983, 991, 997]
_KNOWN_PRIMES = tuple(__P)
del __P


def is_prime(n: int, precision_for_huge_n: int = 16) -> bool:
    """
    A return value of False means n is certainly not prime. A return value of
    True means n is a prime unless it's a huge number, then it's just very
    likely a prime.
    Arguments:
        {n} integer -- Number to test.
        {precision_for_huge_n} integer -- Number or.
    Returns:
        True -- If {n} is (probably) a prime.
        False -- If {n} is not a prime.
    """
    if n in _KNOWN_PRIMES:
        return True
    if n < 2 or any((n % p) == 0 for p in _KNOWN_PRIMES):
        return False
    d, s = n >> 1, 1
    while d & 1 == 0:
        d, s = d >> 1, s + 1

    for best_solution, bases in _DETERMINISTIC_SOLUTIONS:
        if n < best_solution:
            return all(_witness(a, d, n, s) for a in bases)

    # otherwise
    return all(_witness(a, d, n, s) for a in _KNOWN_PRIMES[:precision_for_huge_n])


def _witness(a: int, d: int, n: int, s: int) -> bool:
    x = pow(a, d, n)
    while s:
        y = (x * x) % n
        if y == 1 and x != 1 and x != n - 1:
            return False
        x = y
        s = s - 1
    if y != 1:
        return False
    return True


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
    number = n + 1 if n % 2 == 0 else n + 2
    while True:
        if is_prime(number):
            return number
        number += 2


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
    if n == 3:
        return 2
    number = n - 1 if n % 2 == 0 else n - 2
    while True:
        if is_prime(number):
            return number
        number -= 2
