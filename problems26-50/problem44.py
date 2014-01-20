#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 44
Pentagon numbers
"""

from itertools import count

def pentagonal(n):
    return n * (3*n-1) // 2

def pentagonal_inv(p):
    return int((24*p + 1)**0.5 + 1) // 6

def is_pentagonal(p):
    return p == pentagonal(pentagonal_inv(p))

def is_sum_dif_pentagonal(p, q):
    return is_pentagonal(p + q) and is_pentagonal(p - q)

def find_sum_dif_pentagonal():
    return ((i, j) for i in count(1) for j in reversed(range(1, i))
             if is_sum_dif_pentagonal(pentagonal(i), pentagonal(j)))

print(next(pentagonal(i)-pentagonal(j) for i, j in find_sum_dif_pentagonal()))

