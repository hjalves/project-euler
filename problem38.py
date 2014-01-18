#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 38
Pandigital multiples
"""

from math import log10

def split(n):
    return map(int, str(n))

def join(nl):
    return sum(b * 10**p for p, b in enumerate(reversed(nl)))

def product_cat(num):
    s, n = [], 1
    while len(s) < 9:
        s.extend(split(num * n))
        n += 1
    return s

def is_pandigital(nl):
    return len(nl) == 9 and set(nl) == set(range(1, 10))

print(max(join(p) for p in map(product_cat, range(10000)) if is_pandigital(p)))
