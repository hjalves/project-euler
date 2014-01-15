#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 25
1000-digit Fibonacci number
"""

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

def have_ndig(num, dig):
    return num >= 10**(dig-1)

fib1000 = (i for i, n in enumerate(fibonacci(), 1) if have_ndig(n, 1000))
print(next(fib1000))
