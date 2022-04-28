# Pseudoprimes

Test and find prime numbers.

```python
import pseudoprimes
pseudoprimes.is_prime(11)
>> True

pseudoprimes.next_prime(3)
>> 5

pseudoprimes.prev_prime(100)
>> 97
```

## Installation

```bash
pip install pseudoprimes
```

## Probabilistic or deterministic?

The used Miller–Rabin algorithm is deterministic for values until 3317044064679887385961981. Numbers larger than that are tested using a probabilistic primality test.
