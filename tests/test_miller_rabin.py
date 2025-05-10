"""
https://en.wikipedia.org/wiki/Lucas_pseudoprime
"""

import unittest

from pseudoprimes import miller_rabin


class TestMillerRabin(unittest.TestCase):
    """Test with known values"""

    def test_is_miller_rabin_prp_small_numbers(self) -> None:
        """
        Small numbers.
        """

        self.assertTrue(miller_rabin.is_miller_rabin_prp(2, [2]))
        self.assertTrue(miller_rabin.is_miller_rabin_prp(3, (2,)))
        self.assertFalse(miller_rabin.is_miller_rabin_prp(9, (2,)))
        self.assertFalse(miller_rabin.is_miller_rabin_prp(1, (2,)))

    def test_carmichael_number(self) -> None:
        """
        Carmichael numbers.
        """
        self.assertFalse(miller_rabin.is_miller_rabin_prp(561, (2,)))
        self.assertFalse(miller_rabin.is_miller_rabin_prp(8911, (2,)))


if __name__ == "__main__":
    unittest.main()
