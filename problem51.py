#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 51
Prime digit replacements
"""

from itertools import combinations
from collections import Counter

def prime_sieve(size):
    sieve = [0, 0] + [1] * (size-2)
    for i, isprime in enumerate(sieve):
        if isprime:
            for j in range(i+i, size, i):
                sieve[j] = 0
    return sieve

psieve = prime_sieve(size=1000000)

def is_prime(n):
    return bool(psieve[n])

def primes(max):
    return filter(is_prime, range(2, max))

def split(n):
    return map(int, str(n))
    
def join(nl):
    return sum(b * 10**p for p, b in enumerate(reversed(nl)))

def replace(sl, positions, char='*'):
    sl = list(sl)
    for p in positions:
        sl[p] = char
    return ''.join(sl)

def comb(n):
    return (c for i in range(1, n+1) for c in combinations(range(n), i))

def replace_digit(sl, original, replacement):
    sl = list(sl)
    for i, d in enumerate(sl):
        if d == original:
            sl[i] = replacement
    return sl

def test_replacements(sl, digit):
    count = 0
    for d in range(10):
        if is_prime(join(replace_digit(sl, digit, d))):
            count += 1
    return count

def eight_prime_family(n):
    sl = list(split(n))
    for d in set(sl):
        if d in (0, 1, 2) and test_replacements(sl, d) == 8:
            return True
    return False

for p in primes(1000000):
    if eight_prime_family(p):
        print(p)
        exit(0)
