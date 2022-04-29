"""
https://en.wikipedia.org/wiki/Lucas_pseudoprime
"""


import unittest

from pseudoprimes import lucas


class TestLucas(unittest.TestCase):
    """Test with known values"""

    def test_is_strong_lucas_prp(self) -> None:
        self.assertTrue(lucas.is_strong_lucas_prp(2))
        self.assertTrue(lucas.is_strong_lucas_prp(3))
        self.assertFalse(lucas.is_strong_lucas_prp(9))
        self.assertFalse(lucas.is_strong_lucas_prp(1))
        self.assertFalse(lucas.is_strong_lucas_prp(15))

    def test_jacobi_symbol(self) -> None:
        self.assertEqual(lucas.jacobi_symbol(45, 77), -1)
        self.assertEqual(lucas.jacobi_symbol(60, 121), 1)
        self.assertEqual(lucas.jacobi_symbol(0, 3), 0)
        self.assertEqual(lucas.jacobi_symbol(1, 3), 1)
        self.assertEqual(lucas.jacobi_symbol(3, 9), 0)
        with self.assertRaises(ValueError):
            lucas.jacobi_symbol(4, 2)

    def test_lucas_sequence(self) -> None:
        n = 10**2000 + 4561
        self.assertEqual(lucas._lucas_sequence(n, 3, 1, n // 2), (0, 2, 1))
        self.assertEqual(lucas._lucas_sequence(n, 3, 1, 0), (0, 2, 1))
        with self.assertRaises(ValueError):
            lucas._lucas_sequence(0, 0, 0, 0)
        with self.assertRaises(ValueError):
            lucas._lucas_sequence(n, 3, 1, -1)
        with self.assertRaises(ValueError):
            lucas._lucas_sequence(n, 2, 1, n // 2)


if __name__ == "__main__":
    unittest.main()
