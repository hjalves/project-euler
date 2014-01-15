#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 21
Amicable numbers
"""

def divisors(n):
    divs = ((i, n//i) for i in range(2, int(n**0.5)+1) if n % i == 0)
    return set(d for tup in divs for d in tup)

def divsum(n):
    return 1 + sum(divisors(n)) if n > 1 else 0

def amicable_nums(n):
    for i in range(n):
        ds1 = divsum(i)
        if ds1 != i and divsum(ds1) == i:
            yield i

print(sum(amicable_nums(10000)))
