"""
https://oeis.org/A014233
https://primes.utm.edu/lists/2small/0bit.html
https://primes.utm.edu/lists/small/millions/
"""


import unittest
from unittest.mock import patch

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
        self.assertTrue(pseudoprimes.is_prime(32_424_781))
        self.assertTrue(pseudoprimes.is_prime(2_147_483_647))
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
                self.assertTrue(pseudoprimes.is_prime(int(token)), token)

    def test_not_prime(self) -> None:
        self.assertFalse(pseudoprimes.is_prime(0))
        self.assertFalse(pseudoprimes.is_prime(1))
        self.assertFalse(pseudoprimes.is_prime(-1))
        self.assertFalse(pseudoprimes.is_prime(341_531))
        self.assertFalse(pseudoprimes.is_prime(32_424_581))
        self.assertFalse(pseudoprimes.is_prime(1_050_535_501))
        self.assertFalse(pseudoprimes.is_prime(350_269_456_337))
        self.assertFalse(pseudoprimes.is_prime(55_245_642_489_451))
        self.assertFalse(pseudoprimes.is_prime(7_999_252_175_582_851))
        self.assertFalse(pseudoprimes.is_prime(585_226_005_592_931_977))
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
            self.assertFalse(pseudoprimes.is_prime(candidate), candidate)

    def test_primes_just_less_than_8_bits(self) -> None:
        for k in [5, 15, 17, 23, 27, 29, 33, 45, 57, 59]:
            self.assertTrue(pseudoprimes.is_prime(2**8 - k), k)

    def test_primes_just_less_than_16_bits(self) -> None:
        for k in [15, 17, 39, 57, 87, 89, 99, 113, 117, 123]:
            self.assertTrue(pseudoprimes.is_prime(2**16 - k), k)

    def test_primes_just_less_than_32_bits(self) -> None:
        for k in [5, 17, 65, 99, 107, 135, 153, 185, 209, 267]:
            self.assertTrue(pseudoprimes.is_prime(2**32 - k), k)

    def test_primes_just_less_than_64_bits(self) -> None:
        for k in [59, 83, 95, 179, 189, 257, 279, 323, 353, 363]:
            self.assertTrue(pseudoprimes.is_prime(2**64 - k), k)

    def test_primes_just_less_than_128_bits(self) -> None:
        for k in [159, 173, 233, 237, 275, 357, 675, 713, 797, 1193]:
            self.assertTrue(pseudoprimes.is_prime(2**128 - k), k)

    def test_primes_just_less_than_256_bits(self) -> None:
        for k in [189, 357, 435, 587, 617, 923, 1053, 1299, 1539, 1883]:
            self.assertTrue(pseudoprimes.is_prime(2**256 - k), k)

    def test_pseudoprimes_base_97(self) -> None:
        """https://oeis.org/A020225"""
        nums = [4, 6, 8, 12, 16, 21, 24, 32, 48, 49, 66, 96, 105, 147, 176, 186, 231]
        nums += [245, 341, 344, 469, 481, 496, 561, 637, 645, 651, 833, 946, 949, 973]
        nums += [1056, 1065, 1068, 1105, 1128, 1729, 1813, 1891, 2046, 2047, 2465, 2701]
        nums += [2821, 2976, 3053, 3277, 3283, 3577, 4187]
        for k in nums:
            self.assertFalse(pseudoprimes.is_prime(97 ** (k - 1)), k)

    @patch("pseudoprimes.pseudoprimes._KNOWN_PRIMES", (2,))
    def test_carmichael_number(self) -> None:
        """Removing most known primes forces a non‐trivial factor test"""
        self.assertFalse(pseudoprimes.is_prime(561))

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

    def test_gen_prime(self) -> None:
        self.assertIn(pseudoprimes.gen_prime(2), (2, 3))
        results = set()
        for _ in range(10):
            prime = pseudoprimes.gen_prime(1024)
            self.assertGreaterEqual(prime, 2**1023)
            self.assertLess(prime, 2**1024)
            results.add(prime)
        self.assertEqual(len(results), 10)

    def test_gen_prime_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            pseudoprimes.gen_prime(-10)
        with self.assertRaises(ValueError):
            pseudoprimes.gen_prime(1)


if __name__ == "__main__":
    unittest.main()
