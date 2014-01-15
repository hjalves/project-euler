#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 23
Non-abundant sums
"""

MAX = 28123     # "it can be shown that all integers greater than 28123 can be
                # written as the sum of two abundant numbers"

def divisors(n):
    divs = ((i, n//i) for i in range(2, int(n**0.5)+1) if n % i == 0)
    return set(d for tup in divs for d in tup)

def divsum(n):
    return 1 + sum(divisors(n)) if n > 1 else 0

def is_abundant(n):
    return divsum(n) > n 

abundant = list(filter(is_abundant, range(MAX+1)))

sums = [False] * (MAX+1)
for i, a in enumerate(abundant):
    for b in abundant[i:]:
        if a+b > MAX:
            break
        sums[a+b] = True
print( sum(i for i, s in enumerate(sums) if not s) )

