"""
Modified from SymPy
https://en.wikipedia.org/wiki/Lucas_pseudoprime
"""

import math
from typing import Tuple


def is_strong_lucas_prp(n: int) -> bool:
    """
    Strong Lucas compositeness test with Selfridge parameters.

    Returns
    False if n is definitely composite, and True if n is a strong Lucas
    probable prime.

    This is often used in combination with the Miller-Rabin test, and
    in particular, when combined with M-R base 2 creates the strong BPSW test.
    """
    if n == 2:
        return True
    if n < 2 or (n % 2) == 0 or is_square(n):
        return False

    D, P, Q = _lucas_selfridge_params(n)
    if D == 0:
        return False

    # remove powers of 2 from n+1 (= k * 2**s)
    k, s = n + 1, 0
    while k & 1 == 0:
        k, s = k >> 1, s + 1

    U, V, Qk = _lucas_sequence(n, P, Q, k)

    if U == 0 or V == 0:
        return True
    for _ in range(1, s):
        V = (V * V - 2 * Qk) % n
        if V == 0:
            return True
        Qk = pow(Qk, 2, n)
    return False


def jacobi_symbol(m: int, n: int) -> int:  # noqa: C901
    """
    Returns the Jacobi symbol (m / n).
    """
    if n < 0 or not n % 2:
        raise ValueError("n should be an odd positive integer")
    if m < 0 or m > n:
        m %= n
    if not m:
        return int(n == 1)
    if n == 1 or m == 1:
        return 1
    if math.gcd(m, n) != 1:
        return 0

    j = 1
    while m != 0:
        while m % 2 == 0 and m > 0:
            m >>= 1
            if n % 8 in [3, 5]:
                j = -j
        m, n = n, m
        if m % 4 == n % 4 == 3:
            j = -j
        m %= n
    return j if n == 1 else 0


def is_square(n: int) -> bool:
    """
    Return True if n == a * a for some integer a, else False.
    """
    return math.isqrt(n) ** 2 == n


def _lucas_selfridge_params(n: int) -> Tuple[int, int, int]:
    """
    Calculates the Selfridge parameters (D, P, Q) for n.
    """
    D = 5
    while True:
        g = math.gcd(abs(D), n)
        if g > 1 and g != n:
            return (0, 0, 0)
        if jacobi_symbol(D, n) == -1:
            break
        if D > 0:
            D = -D - 2
        else:
            D = -D + 2
    return (D, 1, (1 - D) // 4)


def _lucas_sequence(  # noqa: C901
    n: int, P: int, Q: int, k: int
) -> Tuple[int, int, int]:
    """
    Return the modular Lucas sequence (U_k, V_k, Q_k).
    Given a Lucas sequence defined by P, Q, returns the kth values for
    U and V, along with Q^k, all modulo n.  This is intended for use with
    possibly very large values of n and k, where the combinatorial functions
    would be completely unusable.
    The modular Lucas sequences are used in numerous places in number theory,
    especially in the Lucas compositeness tests and the various n + 1 proofs.
    """
    D = P * P - 4 * Q
    if n < 2:
        raise ValueError("n must be >= 2")
    if k < 0:
        raise ValueError("k must be >= 0")
    if D == 0:
        raise ValueError("D must not be zero")

    if k == 0:
        return (0, 2, Q)
    U = 1
    V = P
    Qk = Q
    b = k.bit_length()
    if Q == 1:
        # Optimization for extra strong tests.
        while b > 1:
            U = (U * V) % n
            V = (V * V - 2) % n
            b -= 1
            if (k >> (b - 1)) & 1:
                U, V = U * P + V, V * P + U * D
                if U & 1:
                    U += n
                if V & 1:
                    V += n
                U, V = U >> 1, V >> 1
    elif P == 1 and Q == -1:
        # Small optimization for 50% of Selfridge parameters.
        while b > 1:
            U = (U * V) % n
            if Qk == 1:
                V = (V * V - 2) % n
            else:
                V = (V * V + 2) % n
                Qk = 1
            b -= 1
            if (k >> (b - 1)) & 1:
                U, V = U + V, V + U * D
                if U & 1:
                    U += n
                if V & 1:
                    V += n
                U, V = U >> 1, V >> 1
                Qk = -1
    else:
        # The general case with any P and Q.
        while b > 1:
            U = (U * V) % n
            V = (V * V - 2 * Qk) % n
            Qk *= Qk
            b -= 1
            if (k >> (b - 1)) & 1:
                U, V = U * P + V, V * P + U * D
                if U & 1:
                    U += n
                if V & 1:
                    V += n
                U, V = U >> 1, V >> 1
                Qk *= Q
            Qk %= n
    return (U % n, V % n, Qk)
