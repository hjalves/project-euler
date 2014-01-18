#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 39
Integer right triangles
"""

from operator import itemgetter
from collections import Counter

# a + b + c = p
# a**2 + b**2 = c**2
# a = sqrt(c**2 - b**2)
# triangulo a+b>c, a+b+c<=1000 ==> maxc=500

def is_triplet(a, b, c):
    return a < b < c and a*a + b*b == c*c

def iterate_abc(maxc):
    f_a = lambda b,c: int((c*c - b*b)**0.5)
    return ((f_a(b, c), b, c) for c in range(maxc) for b in range(c))

def pyth_triplets(max):
    return ((a, b, c) for a, b, c in iterate_abc(max) if is_triplet(a, b, c))

count = Counter((a+b+c) for a,b,c in pyth_triplets(500) if a+b+c <= 1000)
print(max(count, key=lambda x:count[x]))
