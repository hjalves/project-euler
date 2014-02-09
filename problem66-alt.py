#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 66
Diophantine equation
"""

from itertools import count

def xsquare(d, y):
    return 1 + d * y*y

def is_square(x):
    return int(x**.5)**2 == x

def find_y_solutions(d, max):
    return (y for y in range(1, max) if is_square(xsquare(d, y)))

l = []
for d in range(2, 1000):
    if not is_square(d):
        first_y = next(find_y_solutions(d, max=10000000), None)
        if not first_y:
            l.append(d)
        print(d, first_y)
print(l)
