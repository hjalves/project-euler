#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 49
Prime permutations
"""

from collections import defaultdict
from itertools import combinations

def split(n):
    return map(int, str(n))

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes(min, max):
    return filter(is_prime, range(min, max))

def pairs(l):
    return combinations(l, 2)

def sequences3(l):
    return ((a, b, b+b-a) for a, b in pairs(l) if b+b-a in l)

def digit_prime_dict(start, end):
    d = defaultdict(list)
    for p in primes(start, end):
        s = tuple(sorted(set(split(p))))
        d[s].append(p)
    return d

def prime_perm_sequences3(start=1000, end=10000):
    dp = digit_prime_dict(start, end)
    return (s for v in dp.values() for s in sequences3(v))

def catseq(l):
    return int("".join(map(str, l)))

print(*map(catseq, prime_perm_sequences3()), sep='\n')


