"""
https://oeis.org/A014233
https://primes.utm.edu/lists/2small/0bit.html
https://primes.utm.edu/lists/small/millions/
"""


import unittest

import pseudoprimes


def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


class TestPrimes(unittest.TestCase):
    """Test with known values"""

    def test_is_prime_known(self) -> None:
        self.assertTrue(pseudoprimes.is_prime(2))
        self.assertTrue(pseudoprimes.is_prime(3))
        self.assertTrue(pseudoprimes.is_prime(47))
        self.assertTrue(pseudoprimes.is_prime(32424781))
        self.assertTrue(
            pseudoprimes.is_prime(
                4547337172376300111955330758342147474062293202868155909489
            )
        )
        self.assertTrue(
            pseudoprimes.is_prime(
                643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153  # noqa: E501
            )
        )

    def test_is_prime_first_million_primes(self) -> None:
        with open("tests/primes1.txt", encoding="ascii") as file:
            for token in read_by_tokens(file):
                self.assertTrue(pseudoprimes.is_prime(int(token)))

    def test_not_prime(self) -> None:
        self.assertFalse(pseudoprimes.is_prime(0))
        self.assertFalse(pseudoprimes.is_prime(1))
        self.assertFalse(pseudoprimes.is_prime(-1))
        self.assertFalse(pseudoprimes.is_prime(341531))
        self.assertFalse(pseudoprimes.is_prime(32424581))
        self.assertFalse(pseudoprimes.is_prime(1050535501))
        self.assertFalse(pseudoprimes.is_prime(350269456337))
        self.assertFalse(pseudoprimes.is_prime(55245642489451))
        self.assertFalse(pseudoprimes.is_prime(7999252175582851))
        self.assertFalse(pseudoprimes.is_prime(585226005592931977))
        self.assertFalse(
            pseudoprimes.is_prime(
                4547337172376300111955330758342147474062293202868155909393
            )
        )

    def test_very_large_composite(self) -> None:
        self.assertFalse(
            pseudoprimes.is_prime(
                115792089237316195423570985008687907853269984665640564039457584007913129639937
            )
        )
        self.assertFalse(
            pseudoprimes.is_prime(
                743808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153  # noqa: E501
            )
        )
        self.assertFalse(pseudoprimes.is_prime((2**128 - 159) * (2**128 - 173)))
        self.assertFalse(pseudoprimes.is_prime((2**256 - 189) * (2**256 - 357)))

    def test_a014233(self) -> None:
        composites = [
            2047,
            1373653,
            25326001,
            3215031751,
            2152302898747,
            3474749660383,
            341550071728321,
            341550071728321,
            3825123056546413051,
            3825123056546413051,
            3825123056546413051,
            318665857834031151167461,
            3317044064679887385961981,
        ]
        for candidate in composites:
            self.assertFalse(pseudoprimes.is_prime(candidate))

    def test_just_less_than_8_bits(self) -> None:
        for k in [5, 15, 17, 23, 27, 29, 33, 45, 57, 59]:
            self.assertTrue(pseudoprimes.is_prime(2**8 - k))

    def test_just_less_than_16_bits(self) -> None:
        for k in [15, 17, 39, 57, 87, 89, 99, 113, 117, 123]:
            self.assertTrue(pseudoprimes.is_prime(2**16 - k))

    def test_just_less_than_32_bits(self) -> None:
        for k in [5, 17, 65, 99, 107, 135, 153, 185, 209, 267]:
            self.assertTrue(pseudoprimes.is_prime(2**32 - k))

    def test_just_less_than_64_bits(self) -> None:
        for k in [59, 83, 95, 179, 189, 257, 279, 323, 353, 363]:
            self.assertTrue(pseudoprimes.is_prime(2**64 - k))

    def test_just_less_than_128_bits(self) -> None:
        for k in [159, 173, 233, 237, 275, 357, 675, 713, 797, 1193]:
            self.assertTrue(pseudoprimes.is_prime(2**128 - k))

    def test_just_less_than_256_bits(self) -> None:
        for k in [189, 357, 435, 587, 617, 923, 1053, 1299, 1539, 1883]:
            self.assertTrue(pseudoprimes.is_prime(2**256 - k))

    def test_next_prime(self) -> None:
        self.assertEqual(pseudoprimes.next_prime(0), 2)
        self.assertEqual(pseudoprimes.next_prime(2), 3)
        self.assertEqual(pseudoprimes.next_prime(3), 5)
        self.assertEqual(pseudoprimes.next_prime(5), 7)
        self.assertEqual(pseudoprimes.next_prime(2**32 - 266), 2**32 - 209)

    def test_prev_prime(self) -> None:
        self.assertEqual(pseudoprimes.prev_prime(3), 2)
        self.assertEqual(pseudoprimes.prev_prime(10), 7)
        self.assertEqual(pseudoprimes.prev_prime(100), 97)
        self.assertEqual(pseudoprimes.prev_prime(2**64 - 190), 2**64 - 257)

    def test_prev_prime_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime(-10)
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime(1)
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime(2)


if __name__ == "__main__":
    unittest.main()
