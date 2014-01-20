#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 37
Truncatable primes
"""

from math import log10

def isprime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def buildnum(num=0):
    if isprime(num):
        yield num
    elif num != 0:
        return
    # numbers ending in 0,4,6,8 cannot be primes
    for dig in (1, 2, 3, 5, 7, 9):
        for n in buildnum(10*num + dig):
            yield n

def trunctest(num):
    log = int(log10(num))
    return isprime(num) and (log == 0 or trunctest(num % 10**log))

def truncprimes():
    return (n for n in buildnum() if n > 9 and trunctest(n))

print(sum(truncprimes()))
