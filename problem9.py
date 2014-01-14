#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 9
Special Pythagorean triplet
"""

def is_triplet(a, b, c):
    return a < b < c and a*a + b*b == c*c

def iterate_abc(maxc):
    f_a = lambda b,c: int((c*c - b*b)**0.5)
    return ((f_a(b, c), b, c) for c in range(maxc) for b in range(c))

def find_triplet(tsum):
    return ((a, b, c) for a, b, c in iterate_abc(tsum)
            if is_triplet(a, b, c) and a+b+c==tsum)

a, b, c = next(find_triplet(1000))
print(a*b*c)
