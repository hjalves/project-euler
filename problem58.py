#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 58
Spiral primes
"""

from itertools import count

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes(max):
    return filter(is_prime, range(2, max))

def diagonals(l):
    return range(l**2, l**2-(l-1)*4, -(l-1))

def diagonal_numbers(l):
    return 1 + 4*(l-1)//2

def primes_diagonal(l):
    return sum(1 for d in diagonals(l) if is_prime(d))

def memoize(f):
    dx = {}
    return lambda *a: dx[a] if a in dx else dx.setdefault(a, f(*a))

@memoize
def spiral_primes(l):
    return spiral_primes(l-2) + primes_diagonal(l) if l > 1 else 0

def diagonal_fraction(l):
    return spiral_primes(l), diagonal_numbers(l)

def prime_ratio_below_10():
    for l in count(3, 2):
        n, d = diagonal_fraction(l)
        if n / d < 0.10:
            return l

print(prime_ratio_below_10())
