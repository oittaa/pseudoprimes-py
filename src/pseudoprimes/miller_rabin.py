"""
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""
BEST_SOLUTION = 3_317_044_064_679_887_385_961_981

# Returns exact according to https://miller-rabin.appspot.com/
_DETERMINISTIC_SOLUTIONS = (
    (341531, (9345883071009581737,)),
    (1050535501, (336781006125, 9639812373923155)),
    (350269456337, (4230279247111683200, 14694767155120705706, 16641139526367750375)),
    (55245642489451, (2, 141889084524735, 1199124725622454117, 11096072698276303650)),
    (
        7999252175582851,
        (2, 4130806001517, 149795463772692060, 186635894390467037, 3967304179347715805),
    ),
    (
        585226005592931977,
        (
            2,
            123635709730000,
            9233062284813009,
            43835965440333360,
            761179012939631437,
            1263739024124850375,
        ),
    ),
    (18446744073709551616, (2, 325, 9375, 28178, 450775, 9780504, 1795265022)),
    # https://ui.adsabs.harvard.edu/abs/2015arXiv150900864S
    (318_665_857_834_031_151_167_461, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)),
    (
        3_317_044_064_679_887_385_961_981,
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41),
    ),
)


def is_miller_rabin_prp(n: int) -> bool:
    """
    Perform a Miller-Rabin strong pseudoprime test on n.

    Returns False if n is definitely composite, and True if n is a probable
    prime.
    """
    if n == 2:
        return True
    if n < 2 or (n % 2) == 0:
        return False
    d, s = n >> 1, 1
    while d & 1 == 0:
        d, s = d >> 1, s + 1

    for best_solution, bases in _DETERMINISTIC_SOLUTIONS:
        if n < best_solution:
            break
    else:
        bases = (2,)
        #  bases = (2, random.randrange(3, n - 1))

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
