# Pseudoprimes

Test and find prime numbers.

```python
>>> import pseudoprimes
>>> pseudoprimes.is_prime(11)
True
>>> pseudoprimes.is_prime(1022117)
False
>>> pseudoprimes.gen_prime(128)  # 128-bit prime
181872728983755108091298489166590324849
>>> pseudoprimes.next_prime(3)
5
>>> pseudoprimes.prev_prime(100)
97
```

## Installation

```bash
pip install pseudoprimes
```

## Probabilistic or deterministic?

The used Miller–Rabin algorithm[^1] is deterministic for values up to 3,317,044,064,679,887,385,961,981. Numbers larger than that are tested using a probabilistic primality test.

[^1]: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants
