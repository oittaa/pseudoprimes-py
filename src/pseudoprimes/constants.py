"""
Constants for internal use.
"""

# Returns exact according to https://miller-rabin.appspot.com/
DETERMINISTIC_SOLUTIONS = (
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

_P = [53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]
_P += [137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]
_P += [223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
_P += [307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389]
_P += [397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479]
_P += [487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587]
_P += [593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673]
_P += [677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773]
_P += [787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881]
_P += [883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
KNOWN_PRIMES_50_TO_1000 = tuple(_P)
del _P
