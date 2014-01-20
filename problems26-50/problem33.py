#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 33
Digit canceling fractions
"""

from functools import reduce
from operator import mul
from fractions import gcd

def testdig(a, b, ai, bi):
    at, bt = divmod(a, 10), divmod(b, 10)
    return at[ai] == bt[bi] != 0 and bt[1-bi]*a == at[1-ai]*b != 0

def is_dcf(a, b):
    return any(testdig(a, b, ai, bi) for ai in (0, 1) for bi in (0, 1))

def search_dcf():
    return ((n, d) for d in range(100) for n in range(d) if is_dcf(n, d))

num, den = zip(*search_dcf())
nmul, dmul = reduce(mul, num), reduce(mul, den)
print(dmul // gcd(nmul, dmul))
