#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 41
Pandigital prime
"""

from itertools import permutations

def join(nl):
    return sum(b * 10**p for p, b in enumerate(reversed(nl)))

def revpan(dig):
    return reversed(list(permutations(range(1, dig+1), dig)))

def isprime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

# eight numbers and nine numbers cannot be done: always dividable by 3
def pandigital_primes():
    for dig in reversed(range(2, 8)):
        for n in filter(isprime, map(join, revpan(dig))):
            yield n

print(next(pandigital_primes()))
