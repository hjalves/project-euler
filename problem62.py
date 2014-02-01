#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 62
Cubic permutations
"""

from collections import Counter, defaultdict
from itertools import count

def digcount(n):
    return Counter(map(int, str(n)))

def digcount_tup(n):
    return tuple(digcount(n)[i] for i in range(10))

def n_permutations_cube(n):
    l = defaultdict(list)
    for c in map(lambda x: x**3, count()):
        dc = digcount_tup(c)
        l[dc].append(c)
        if len(l[dc]) == n:
            yield l[dc]

print(next(n_permutations_cube(5)))
