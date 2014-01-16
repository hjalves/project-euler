#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 27
Quadratic primes
"""

from itertools import takewhile, count

def is_prime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def formula(a, b, n):
    return n*n + a*n + b

def iter_formula(a, b):
    return (formula(a, b, i) for i in count())

def formula_primes(a, b):
    return list(takewhile(is_prime, iter_formula(a, b)))

def primelist(max):
    return list(filter(is_prime, range(max)))

def filter_a(b, min, max):
    return (a for a in range(min, max) if is_prime(1 + a + b))

# Observações:
# - b tem de ser um numero primo. f(0) = b = primo
# - a e b têm de obedecer à seguinte relação: f(1) = 1 + a + b = primo

l = ((a, b, len(formula_primes(a, b))) for b in primelist(max=1000)
                                       for a in filter_a(b, -999, 1000))
a, b, l = max(l, key=lambda x:x[2])
print(a, b, l)
print("a*b:", a*b)
