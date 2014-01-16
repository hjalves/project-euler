#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 35
Circular primes
"""

from math import log10

def digsize(n):
    return int(log10(n))+1 if n > 0 else 0

def rotations(n):
    ds = digsize(n)
    for i in range(ds):
        a, b = divmod(n, 10**i)
        yield b * (10**(ds-i))+ a

def is_prime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def circular_primes(max):
    primes = set(filter(is_prime, range(max)))
    for p in sorted(primes):
        if all(r in primes for r in rotations(p)):
            yield p

cp = list(circular_primes(max=1000000))
print(cp, len(cp))
