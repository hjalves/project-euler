#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 12
Highly divisible triangular number
"""

from itertools import count

def triangle_numbers():
    triangle = lambda i: i * (i+1) // 2
    return map(triangle, count())

def divisors(n):
    divs = ((i, n//i) for i in range(1, int(n**0.5)+1) if n % i == 0)
    return set(d for tup in divs for d in tup)

print(next(t for t in triangle_numbers() if len(divisors(t)) > 500))
