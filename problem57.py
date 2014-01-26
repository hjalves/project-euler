#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 57
Square root convergents
"""

#sqrt(2) = 1 + n / d
# n, d = d, 2*d+n
#     OR
#sqrt(2) = n / d
# n, d = 2*d+n, d + n

from math import log10

def sqrt2(it):
    n, d = 1, 1
    for i in range(it):
        n, d = 2*d+n, d + n
        yield n, d

def digits(n):
    return int(log10(n)+1)

print( sum(1 for n, d in sqrt2(1001) if digits(n) > digits(d)) )
