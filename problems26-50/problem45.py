#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 45
Triangular, pentagonal, and hexagonal
"""

from itertools import count

def hexagonal(n):
    return n * (2*n - 1)

def pentagonal(n):
    return n * (3*n-1) // 2

def pentagonal_inv(p):
    return int((24*p + 1)**0.5 + 1) // 6

def triangular(n):
    return n * (n + 1) // 2

def triangular_inv(t):
    return int((8*t + 1)**0.5 - 1) // 2

def is_pentagonal_triangular(p):
    return p == pentagonal(pentagonal_inv(p)) == triangular(triangular_inv(p))

g = filter(is_pentagonal_triangular, map(hexagonal, count(1)))
print(next(g))
print(next(g))
print(next(g))
