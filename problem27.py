#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 27
Quadratic primes
"""

from itertools import takewhile, count

def is_prime(n):
    assert n >= 0
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def formula(a, b, n):
    return n*n + a*n + b

def iter_formula(a, b):
    return (formula(a, b, i) for i in count())

def seq_primes(a, b):
    return list(takewhile(is_prime, iter_formula(a, b)))

l = [len(seq_primes(a, b)) for a in range(0, 1000) for b in range(0, 1000)]
