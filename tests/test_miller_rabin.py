"""
https://en.wikipedia.org/wiki/Lucas_pseudoprime
"""


import unittest

from pseudoprimes import miller_rabin


class TestMillerRabin(unittest.TestCase):
    """Test with known values"""

    def test_is_miller_rabin_prp(self) -> None:
        self.assertTrue(miller_rabin.is_miller_rabin_prp(2))
        self.assertTrue(miller_rabin.is_miller_rabin_prp(3))
        self.assertFalse(miller_rabin.is_miller_rabin_prp(9))
        self.assertFalse(miller_rabin.is_miller_rabin_prp(1))


if __name__ == "__main__":
    unittest.main()
