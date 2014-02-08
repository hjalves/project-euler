#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 65
Convergents of e
"""

from fractions import Fraction
from itertools import count, islice

def convergent(seq):
    s = next(seq, None)
    f = lambda d: Fraction(1, d) if d else 0
    return s + f(convergent(seq)) if s else 0

def e_seq():
    yield 2
    for i in count(2, 2):
        yield 1; yield i; yield 1

def e_nth_convergent(n):
    return convergent(islice(e_seq(), n))

def digsum(num):
    return sum(map(int, str(num)))
    
print(digsum(e_nth_convergent(100).numerator))

