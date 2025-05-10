"""
Test with known values
"""

import unittest

import pseudoprimes


def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


class TestPrimes(unittest.TestCase):
    """
    Test with known values
    """

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
                int(
                    "0x1f55332c3a48b910f9942f6c914e58bef37a47ee45cb164a5b6b8d"
                    "1006bf59a059c21449939ebebfdf517d2e1dbac88010d7b1f141e997"
                    "bd6801ddaec9d05910f4f2de2b2c4d714e2c14a72fc7f17aa428d59c"
                    "531627f09",
                    16,
                )
            )
        )
        self.assertTrue(pseudoprimes.is_prime(10**2000 + 4561))

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

    def test_numbers_until_10k_primes(self) -> None:
        """
        The largest number in the file is 104 729.
        https://primes.utm.edu/lists/small/10000.txt
        """
        num = 0
        with open("tests/10_000_primes.txt", encoding="ascii") as file:
            for token in read_by_tokens(file):
                next_prime = int(token)
                while num < next_prime:
                    self.assertFalse(pseudoprimes.is_prime(num), num)
                    num += 1
                self.assertTrue(pseudoprimes.is_prime(num), num)
                num += 1

    def test_very_large_composite(self) -> None:
        self.assertFalse(
            pseudoprimes.is_prime(
                0x10000000000000000000000000000000000000000000000000000000000000001
            )
        )
        self.assertFalse(
            pseudoprimes.is_prime(
                int(
                    "0x24331969445e44f755d96270434eb673801a6748957f8d2eb38f28"
                    "a63154db04d61a8faa9c043abc6bc134dfeaca512344d8d3a6fc0f79"
                    "70855f7d86c2705910f4f2de2b2c4d714e2c14a72fc7f17aa428d59c"
                    "531627f09",
                    16,
                )
            )
        )
        self.assertFalse(pseudoprimes.is_prime((2**128 - 159) * (2**128 - 173)))
        self.assertFalse(pseudoprimes.is_prime((2**256 - 189) * (2**256 - 357)))

    def test_a014233_miller_rabin_composites(self) -> None:
        """
        https://oeis.org/A014233
        """
        composites = [
            2047,
            1373653,
            25326001,
            3215031751,
            2152302898747,
            3474749660383,
            341550071728321,
            3825123056546413051,
            318665857834031151167461,
            3317044064679887385961981,
        ]
        for candidate in composites:
            self.assertFalse(pseudoprimes.is_prime(candidate), candidate)

    def test_a217255_strong_lucas_pseudoprimes(self) -> None:
        """
        https://oeis.org/A217255
        """
        composites = [
            5459,
            5777,
            10877,
            16109,
            18971,
            22499,
            24569,
            25199,
            40309,
            58519,
            75077,
            97439,
            100127,
            113573,
            115639,
            130139,
            155819,
            158399,
            161027,
            162133,
            176399,
            176471,
            189419,
            192509,
            197801,
            224369,
            230691,
            231703,
            243629,
            253259,
            268349,
            288919,
            313499,
            324899,
        ]
        for candidate in composites:
            self.assertFalse(pseudoprimes.is_prime(candidate), candidate)

    def test_a217719_extra_strong_lucas_pseudoprimes(self) -> None:
        """
        https://oeis.org/A217719
        """
        composites = [
            989,
            3239,
            5777,
            10877,
            27971,
            29681,
            30739,
            31631,
            39059,
            72389,
            73919,
            75077,
            100127,
            113573,
            125249,
            137549,
            137801,
            153931,
            155819,
            161027,
            162133,
            189419,
            218321,
            231703,
            249331,
            370229,
            429479,
            430127,
            459191,
            473891,
            480689,
            600059,
            621781,
            632249,
            635627,
        ]
        for candidate in composites:
            self.assertFalse(pseudoprimes.is_prime(candidate), candidate)

    def test_adversarial_pseudoprime(self) -> None:
        """
        https://eprint.iacr.org/2018/749.pdf
        """
        p1 = 2**1344 * 0x0000000000000000000000000000083DDA18EB04A7597CA3
        p1 += 2**1152 * 0xC6BC877DF8A08EEC6725FA0832CBA270C42ADC358BC0CF50
        p1 += 2**960 * 0xC82CB10F2733C3FB8875231FC1498A7B14CB675FAC1BF3C5
        p1 += 2**768 * 0x127A76FC11E5D20E27940C95CEBA671FE1C4232250B74CBD
        p1 += 2**576 * 0xF8448C90321513324C0681AFB4BA003353B1AFB0F1E8B91C
        p1 += 2**384 * 0x60AF672A5A6F4D06DD0070A4BC74E425F3EAE90379E57754
        p1 += 2**192 * 0x82D26E80E247464A4BB817DFCF7572F89F8B9CACD059B584
        p1 += 0x0E4389C8AF84F6A6EA15A3EA5D62CB994B082731BA4CDE73
        n = p1 * (1013 * (p1 - 1) + 1) * (2053 * (p1 - 1) + 1)
        self.assertFalse(pseudoprimes.is_prime(n))

    def test_primes_just_less_than_8_bits(self) -> None:
        """
        https://primes.utm.edu/lists/2small/0bit.html
        """
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
        """
        https://oeis.org/A020225
        """
        nums = [4, 6, 8, 12, 16, 21, 24, 32, 48, 49, 66, 96, 105, 147, 176, 186, 231]
        nums += [245, 341, 344, 469, 481, 496, 561, 637, 645, 651, 833, 946, 949, 973]
        nums += [1056, 1065, 1068, 1105, 1128, 1729, 1813, 1891, 2046, 2047, 2465, 2701]
        nums += [2821, 2976, 3053, 3277, 3283, 3577, 4187]
        for k in nums:
            self.assertFalse(pseudoprimes.is_prime(97 ** (k - 1)), k)

    def test_next_prime(self) -> None:
        self.assertEqual(pseudoprimes.next_prime(0), 2)
        self.assertEqual(pseudoprimes.next_prime(2), 3)
        self.assertEqual(pseudoprimes.next_prime(3), 5)
        self.assertEqual(pseudoprimes.next_prime(5), 7)
        self.assertEqual(pseudoprimes.next_prime(8), 11)
        self.assertEqual(pseudoprimes.next_prime(24), 29)
        self.assertEqual(
            [(i, pseudoprimes.next_prime(i)) for i in range(10, 15)],
            [(10, 11), (11, 13), (12, 13), (13, 17), (14, 17)],
        )
        self.assertEqual(
            [(i, pseudoprimes.next_prime(i)) for i in range(65, 100, 6)],
            [(65, 67), (71, 73), (77, 79), (83, 89), (89, 97), (95, 97)],
        )
        self.assertEqual(pseudoprimes.next_prime(2**32 - 266), 2**32 - 209)

    def test_prev_prime(self) -> None:
        self.assertEqual(pseudoprimes.prev_prime(3), 2)
        self.assertEqual(pseudoprimes.prev_prime(8), 7)
        self.assertEqual(pseudoprimes.prev_prime(10), 7)
        self.assertEqual(pseudoprimes.prev_prime(100), 97)
        self.assertEqual(
            [(i, pseudoprimes.prev_prime(i)) for i in range(10, 15)],
            [(10, 7), (11, 7), (12, 11), (13, 11), (14, 13)],
        )
        self.assertEqual(pseudoprimes.prev_prime(2**64 - 190), 2**64 - 257)

    def test_prev_prime_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime(-10)
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime(1)
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime(2)

    def test_get_prime_small(self) -> None:
        results = set()
        for _ in range(100):
            prime = pseudoprimes.get_prime(2)
            self.assertIn(prime, (2, 3))
            results.add(prime)
        self.assertEqual(len(results), 2)

    def test_get_prime_large(self) -> None:
        results = set()
        for _ in range(10):
            prime = pseudoprimes.get_prime(1024)
            self.assertGreater(prime, 2**1023)
            self.assertLess(prime, 2**1024)
            results.add(prime)
        self.assertEqual(len(results), 10)

    def test_get_prime_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            pseudoprimes.get_prime(-10)
        with self.assertRaises(ValueError):
            pseudoprimes.get_prime(1)

    def test_next_prime_safe(self) -> None:
        """
        The first few safe primes are
        5, 7, 11, 23, 47, 59, 83, 107, 167, 179, 227
        """
        self.assertEqual(pseudoprimes.next_prime_safe(0), 5)
        self.assertEqual(pseudoprimes.next_prime_safe(3), 5)
        self.assertEqual(pseudoprimes.next_prime_safe(5), 7)
        self.assertEqual(pseudoprimes.next_prime_safe(8), 11)
        self.assertEqual(pseudoprimes.next_prime_safe(24), 47)
        self.assertEqual(pseudoprimes.next_prime_safe(179), 227)
        self.assertEqual(
            [(i, pseudoprimes.next_prime_safe(i)) for i in range(10, 15)],
            [(10, 11), (11, 23), (12, 23), (13, 23), (14, 23)],
        )
        self.assertEqual(
            [(i, pseudoprimes.next_prime_safe(i)) for i in range(65, 100, 6)],
            [(65, 83), (71, 83), (77, 83), (83, 107), (89, 107), (95, 107)],
        )
        self.assertEqual(pseudoprimes.next_prime_safe(2**32 - 266), 2**32 - 209)

    def test_prev_prime_safe(self) -> None:
        self.assertEqual(pseudoprimes.prev_prime_safe(6), 5)
        self.assertEqual(pseudoprimes.prev_prime_safe(10), 7)
        self.assertEqual(pseudoprimes.prev_prime_safe(100), 83)
        self.assertEqual(
            [(i, pseudoprimes.prev_prime_safe(i)) for i in range(10, 15)],
            [(10, 7), (11, 7), (12, 11), (13, 11), (14, 11)],
        )
        self.assertEqual(pseudoprimes.prev_prime_safe(2**64 - 190), 2**64 - 1469)

    def test_prev_prime_safe_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime_safe(-10)
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime_safe(1)
        with self.assertRaises(ValueError):
            pseudoprimes.prev_prime_safe(5)

    def test_get_prime_safe_small(self) -> None:
        results = set()
        for _ in range(100):
            prime = pseudoprimes.get_prime_safe(3)
            self.assertIn(prime, (5, 7))
            results.add(prime)
        self.assertEqual(len(results), 2)

    def test_get_prime_safe_large(self) -> None:
        results = set()
        for _ in range(5):
            prime = pseudoprimes.get_prime_safe(128)
            self.assertGreater(prime, 2**127)
            self.assertLess(prime, 2**128)
            results.add(prime)
        self.assertEqual(len(results), 5)

    def test_get_prime_safe_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            pseudoprimes.get_prime_safe(-10)
        with self.assertRaises(ValueError):
            pseudoprimes.get_prime_safe(2)


if __name__ == "__main__":
    unittest.main()
