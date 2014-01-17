#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 35
Circular primes
"""

from math import log10
from collections import Counter
from itertools import product, chain

def digits(n):
    return int(log10(n))+1 if n > 0 else 0

def rotations(n):
    ds = digits(n)
    return ((n % 10**i) * (10**(ds-i)) + (n // 10**i) for i in range(ds))

def isprime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def join(l):
    return sum(b * 10**p for p, b in enumerate(reversed(l)))

def iter1379(dig):
    return (join(l) for n in range(2, dig+1) for l in product(*[(1,3,7,9)]*n))

iter = chain(range(2, 10), iter1379(6))
primes = set(filter(isprime, iter))
s = set(p for p in primes if set(rotations(p)) <= primes)
print(len(s))
