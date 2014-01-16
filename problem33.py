#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 33
Digit canceling fractions
"""

from functools import reduce
from operator import mul

#from itertools import chain
#def contdig(d):  # 2-digits number that contains dig
#    return chain(range(10+d, 100, 10), range(d*10+1, d*10+10)) if d >= 1 else []
#def ltcomdig(d):    # less-than d and with a common digit from d
#    assert 10 <= d < 100
#    return set(n for n in chain(contdig(d//10), contdig(d%10)) if n < d)

def testdig(a, b, ai, bi):
    at, bt = divmod(a, 10), divmod(b, 10)
    return at[ai] == bt[bi] != 0 and bt[1-bi]*a == at[1-ai]*b != 0

def is_dcf(a, b):
    return any(testdig(a, b, ai, bi) for ai in (0, 1) for bi in (0, 1))

#def is_dcf_(a, b):
#    (ah, al), (bh, bl) = divmod(a, 10), divmod(b, 10)
#    return any((al == bl != 0 and bh*a == ah*b != 0,
#                al == bh != 0 and bl*a == ah*b != 0,
#                ah == bl != 0 and bh*a == al*b != 0,
#                ah == bh != 0 and bl*a == al*b != 0))

#def search_dcf():
#    return ((n, d) for d in range(10, 100) for n in range(d) if is_dcf(n, d))

def search_dcf():
    return ((n, d) for d in range(100) for n in range(d) if is_dcf(n, d))

num, den = zip(*search_dcf())
print(num, reduce(mul, num))
print(den, reduce(mul, den))
