#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 5
Smallest multiple
"""

from collections import Counter
from operator import mul
from functools import reduce

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes(max):
    return filter(is_prime, range(2, max+1))

def factors(n):
    return (p for p in primes(n) if n % p == 0)

def factorize(n):
    f = next(factors(n)) # lowest factor
    return [f] if f == n else [f] + factorize(n//f)

def factor_counter(num):
    return {i: Counter(factorize(i)) for i in range(2,num+1)}

def max_factors(fcount):
    c = Counter()
    for v in fcount.values():
        for k in v:
            if c[k] < v[k]:
                c[k] = v[k]
    return c

def smallest_multiple(n):
    factors = max_factors(factor_counter(n)).elements()
    return reduce(mul, factors)

print(smallest_multiple(20))
