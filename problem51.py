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

def replace(nl, pos, digit):
    nl = list(nl)
    for p in pos:
        nl[p] = digit
    return nl

def allcomb(r):
    return (c for i in range(len(r)) for c in combinations(r, i+1))

def candidate_pos(nl):
    return tuple(i for i, n in enumerate(nl)
                   if n in (0, 1, 2) and i != len(nl)-1)

def test_primes(nl, pos):
    return sum(1 for digit in range(10)
                 if is_prime(join(replace(nl, pos, digit))))

def eight_prime_dig_replace(n):
    nl = list(split(n))
    return (pos for pos in allcomb(candidate_pos(nl))
                if test_primes(nl, pos) == 8)

def eight_prime_families(max):
    return ((p, pos) for p in primes(max) for pos in eight_prime_dig_replace(p))

print(next(eight_prime_families(1000000)))
