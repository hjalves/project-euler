#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 61
Cyclical figurate numbers
"""

from functools import partial
from itertools import count

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


#def makematrix(p):
#    for x in map(partial(poligonal, p), count(1)):
#        if x >= 10000:
#            return m

def test():
    for p in range(3, 9):
        for i in range(1, 10):
            print(poligonal(p, i), end=' ')
        print()

import numpy as np
a = np.zeros((6,6))
b = np.zeros((6,6))
c = np.zeros((6,6))

a[0,2] = 1
a[1,3] = 1
a[4,3] = 1

b[2,5] = 1
b[3,2] = 1
b[1,4] = 1

c[2,1] = 1
c[5,2] = 1

print(a.T*b)

