#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 52
Permuted multiples
"""

from itertools import count

def split(n):
    return map(int, str(n))

def test_multiply(num):
    s = set(split(num))
    return all(set(split(num * n)) == s for n in range(2, 7))

def digtest(d):
    return filter(test_multiply, range(10**(d-1)+2, 10**d//6+1, 3))

def multest():
    return (n for d in count(1) for n in digtest(d))

print(next(multest()))



