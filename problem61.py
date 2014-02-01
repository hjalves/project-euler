#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 61
Cyclical figurate numbers
"""

from collections import defaultdict
from functools import partial
from itertools import count, takewhile

def poligonal(p, n):
    assert p in range(3, 9)
    if p == 3:  return n * (n + 1) // 2
    if p == 4:  return n * n
    if p == 5:  return n * (3 * n - 1) // 2
    if p == 6:  return n * (2 * n - 1)
    if p == 7:  return n * (5 * n - 3) // 2
    if p == 8:  return n * (3 * n - 2)

def divdigits(n):
    return divmod(n, 100)

def polygonal_count(p):
    return (poligonal(p, n) for n in count(1))

def polygonal_l10k(p):
    return takewhile(lambda x: x < 10000, polygonal_count(p))

def polygonal_4dig(p):
    d = defaultdict(set)
    for a, b in map(divdigits, polygonal_l10k(p)):
        if a >= 10 and b >= 10:
            d[a].add(b)
    return d
        
def make_dict():
    return {p: polygonal_4dig(p) for p in range(3, 9)}

def build_cicles(d, ns, ps, rem):
    if not rem:
        if ns[0] in d[ps[-1]][ns[-1]]:
            yield ns, ps
    for p in rem:
        for n in d[p]:
            if not ps or n in d[ps[-1]][ns[-1]]:
                for x in build_cicles(d, ns + [n], ps + [p], rem - {p}):
                    yield x

def join_4digits(ns):
    return [a*100 + b for a, b in zip(ns, ns[1:]+ns[:1])]

cycles = build_cicles(make_dict(), [], [], set(range(3, 9)))
for ns, ps in cycles:
    numbers = join_4digits(ns)
    print(ns, ps, '\n', numbers, "sum:", sum(numbers))
