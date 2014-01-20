#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 32
Pandigital products
"""

from itertools import chain

def p14():    # only: 1 digits * 4 digits == 4 digits
    return ((a,b) for a in range(1, 10) for b in range(1000, 9999//a+1))

def p23():    # only: 2 digits * 3 digits == 4 digits
    return ((a,b) for a in range(10, 100) for b in range(100, 9999//a+1))

def piter():
    return chain(p14(), p23())

def digset(n):
    return set(map(int, str(n)))

def is_pandigital(a, b):
    return digset(a * b) | digset(a) | digset(b) == set(range(1, 10))

print(sum( set(a*b for a, b in piter() if is_pandigital(a, b)) ))
