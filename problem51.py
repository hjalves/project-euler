#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 51
Prime digit replacements
"""

from itertools import combinations

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

def candidate_pos(nl, maxd):
    return tuple(i for i, n in enumerate(nl)
                   if n in range(maxd+1) and i != len(nl)-1)

def test_primes(nl, pos):
    digits = range(1, 10) if 0 in pos else range(10)
    return sum(1 for d in digits if is_prime(join(replace(nl, pos, d))))

def nth_prime_replace(p, nth):
    nl = list(split(p))
    return (pos for pos in allcomb(candidate_pos(nl, 10-nth))
                if test_primes(nl, pos) >= nth)

def nth_prime_families(max, nth):
    return ((p, pos) for p in primes(max) for pos in nth_prime_replace(p, nth))

print(next(nth_prime_families(1000000, nth=8)))
