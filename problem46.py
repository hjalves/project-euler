#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 46
Goldbach's other conjecture
"""

from itertools import count, islice, filterfalse

def isprime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def oddcomposites():
    return filterfalse(isprime, count(3, 2))

def primes(max):
    return filter(isprime, range(max))

def twsquare(t):
    return round((t//2)**0.5)

def composite_prime_pairs(c):
    return ((p, twsquare(c-p)) for p in primes(c))

def sum_prime_twsq(c):
    return ((p, i) for p, i in composite_prime_pairs(c) if 2*i*i == c-p)

def false_conjecture():
    return (c for c in oddcomposites() if not next(sum_prime_twsq(c), None))

print(next(false_conjecture()))
